import tweepy

from keys import api_key, api_secret_key, access_token, access_token_secret

import time


def auth():
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

api = auth() 
me = api.me()

search = 'EddieHub'
nrTweets = 500

for tweeet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('tweet retweeted')
        tweeet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break