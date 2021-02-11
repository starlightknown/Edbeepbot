import tweepy as twitter
import keys
import time, datetime
import random 
from quotes import quotes

auth = twitter.OAuthHandler(keys.api_key, keys.api_secret_key)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = twitter.API(auth)


def twitter_bot(hashtag, delay):
    while True:
        print(f"\n{datetime.datetime.now()}\n")

        for tweet in twitter.Cursor(api.search, q=hashtag, rpp=10).items(10):
            try:
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]
                random_quote = random.choice(quotes)

                print("id: " + str(tweet_id))
                print("text: " + str(tweet_text))
                print("Random quote: " + random_quote)
                print("-------------------------")

                api.retweet(tweet_id)
                api.update_status(status=random_quote, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)

            except twitter.TweepError as error:
                print(error.reason)
        time.sleep(delay)


twitter_bot("#eddiehub", 10)