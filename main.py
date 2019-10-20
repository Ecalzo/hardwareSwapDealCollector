from config_set import config_set
from deal_collector import DealCollector
import time
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description='print something')
    parser.add_argument('-RID', '--CLIENT_ID', metavar='ID', type=str, nargs=1)
    parser.add_argument('-RSCRT', '--CLIENT_SECRET', metavar='SCRT', type=str,
                        nargs=1)
    parser.add_argument('-RUN', '--REDDIT_USERNAME', metavar='UN', type=str,
                        nargs=1)
    parser.add_argument('-RPW', '--REDDIT_PASSWORD', metavar='PW', type=str,
                        nargs=1)
    parser.add_argument('--twilio', type=bool, nargs=1)
    parser.add_argument('-C', '--CONFIG', metavar='cfg', type=bool, nargs=1)
    parser.add_argument('-k', '--keywords', action='append', type=str)
    args = parser.parse_args()

    print('setting config vars')
    if not args.CONFIG:
        config_set(args.CLIENT_ID[0],
                   args.CLIENT_SECRET[0],
                   args.REDDIT_USERNAME[0],
                   args.REDDIT_PASSWORD[0])
    else:
        from config import (CLIENT_ID,
                            CLIENT_SECRET,
                            REDDIT_USERNAME,
                            REDDIT_PASSWORD)
        config_set(CLIENT_ID,
                   CLIENT_SECRET,
                   REDDIT_USERNAME,
                   REDDIT_PASSWORD)
    if args.twilio:
        twilio_set = True
        from config import (TWILIO_SID,
                            TWILIO_AUTH,
                            TWILIO_NUMBER,
                            MY_NUMBER)
        config_set(TWILIO_SID=TWILIO_SID,
                   TWILIO_AUTH=TWILIO_AUTH,
                   TWILIO_NUMBER=TWILIO_NUMBER,
                   MY_NUMBER=MY_NUMBER)
    else:
        twilio_set = False

    print('Initializing DealCollector')
    deal_bot = DealCollector(args.keywords, twilio_set=args.twilio)
    while True:
        deal_bot.check_for_deals()
        time.sleep(5 * 60)


if __name__ == '__main__':
    main()
