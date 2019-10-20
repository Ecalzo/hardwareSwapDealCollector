import praw
import os
import csv
from twilio.rest import Client


class DealCollector:

    def __init__(self, keywords=[], twilio_set=False):
        self.subreddit = 'hardwareswap'
        self.keywords = keywords
        self.twilio_set = twilio_set
        self.client = self.get_twilio_client()
        self.post_dict = {}
        self.logged_in = False
        self.reddit = self.bot_login()

    def bot_login(self):
        try:
            print("logging in: ", os.getenv("reddit_username"))
            reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                                 client_secret=os.getenv("CLIENT_SECRET"),
                                 user_agent='hardware swap deal collector',
                                 username=os.getenv("REDDIT_USERNAME"),
                                 password=os.getenv("REDDIT_PASSWORD"))
            print("logged in!")
            self.logged_in = True
        except Exception as e:
            print(e)
            print("Login failed")
            self.logged_in = False
        return reddit

    def append_to_csv(self, post_id):
        url = self.post_dict[post_id]['url']
        title = self.post_dict[post_id]['title']
        with open('deals.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([post_id, url, title])
        return True

    def get_twilio_client(self):
        if self.twilio_set:
            twilio_sid = os.getenv('TWILIO_SID')
            twilio_auth = os.getenv('TWILIO_AUTH')
            client = Client(twilio_sid, twilio_auth)
            return client
        else:
            print('no twilio account info provided')

    def send_text(self, collected_urls):
        if self.twilio_set:
            twilio_number = os.getenv('TWILIO_NUMBER')
            my_number = os.getenv('MY_NUMBER')
            client = self.client
            urls = '\n\n'.join(collected_urls)
            message = client.messages.create(from_=twilio_number,
                                             body=urls,
                                             to=my_number)
        else:
            pass

    def collect_posts(self, post_list):
        posts = 0
        collected_urls = []
        for post in post_list:
            post_id = str(post.id)
            if post_id not in self.post_dict:
                url = str(post.url)
                title = str(post.title)
                self.post_dict[post_id] = {}
                self.post_dict[post_id]['url'] = url
                self.post_dict[post_id]['title'] = title
                # add to csv
                self.append_to_csv(post_id)
                print('post of interest:', url)
                posts += 1
                collected_urls.append(url)
        if posts > 0:
            print(posts, 'new post(s) appended to deals.csv')
            self.send_text(collected_urls)
        return True

    def check_for_deals(self):
        if len(self.keywords) == 0:
            return 'empty keywords list'
        r = self.reddit
        s = self.subreddit
        keywords = self.keywords
        post_list = []
        for post in r.subreddit(s).new():
            title = str(post.title)
            for key in keywords:
                if key.lower() in title.lower():
                    post_list.append(post)
        self.collect_posts(post_list)
        return True
