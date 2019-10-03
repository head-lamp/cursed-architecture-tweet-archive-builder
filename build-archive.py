import tweepy
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")

# cursed_architect_user_id=1038689885933068288

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
screen_name='CursedArchitect'
users = api.lookup_users([],[screen_name])
alltweets = []
latest_tweets = api.user_timeline(screen_name=screen_name, count=200)
#print(dir(latest_tweets[0]))
#pprint(latest_tweets[0])
print(latest_tweets[0].entities['media'][0]['media_url_https'])
#print(users)
