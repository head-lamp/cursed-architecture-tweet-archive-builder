import tweepy
from pprint import pprint
from dotenv import load_dotenv
import getopt
import os
import json

#import argparse
#parser = argparse.ArgumentParser(description='Download some tweet data for the Cursed Architecture twitter account')
#parser.add_argument('--output', help='output tweetmetadata.json')
#args = parser.parse_args()



load_dotenv()

access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
screen_name='CursedArchitect'
users = api.lookup_users([],[screen_name])
alltweets = []
new_tweets = api.user_timeline(screen_name=screen_name, count=200)
alltweets.extend(new_tweets)
oldest = alltweets[-1].id - 1
while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

json_tweets = []
for tweet in alltweets:
    json_tweets.append(tweet._json)
print(json.dumps(json_tweets))
