import os


def config_set(CLIENT_ID='',
               CLIENT_SECRET='',
               REDDIT_USERNAME='',
               REDDIT_PASSWORD='',
               TWILIO_SID='',
               TWILIO_AUTH='',
               TWILIO_NUMBER='',
               MY_NUMBER=''):
    # set env variables, so we do not save in plaintext
    if CLIENT_ID:
        os.environ['CLIENT_ID'] = CLIENT_ID
        os.environ['CLIENT_SECRET'] = CLIENT_SECRET
        os.environ['REDDIT_USERNAME'] = REDDIT_USERNAME
        os.environ['REDDIT_PASSWORD'] = REDDIT_PASSWORD
    if TWILIO_SID:
        os.environ['TWILIO_SID'] = TWILIO_SID
        os.environ['TWILIO_AUTH'] = TWILIO_AUTH
        os.environ['TWILIO_NUMBER'] = TWILIO_NUMBER
        os.environ['MY_NUMBER'] = MY_NUMBER
    return True
