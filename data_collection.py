from re import search
import tweepy
import json
import pandas as pd

# Keys as defined by the Twitter API
# Use dev.twitter.com to create an app and set up the keys
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

# Using the Twitter 1.1 API. 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

search_term = "riotscienceclub"

public_tweets = []  

tweets = api.search_tweets(search_term)

for tweet in tweets:
    try:
        public_tweets.append(json.dumps(tweet._json))
    except Exception as te:
        print(te)
        continue

df = pd.json_normalize(public_tweets)
df.to_csv('riot1.csv')