import tweepy as twitter
import keys
import time, datetime
import random 
from quotes import quotes
import os

auth = twitter.OAuthHandler(keys.api_key, keys.api_secret_key)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = twitter.API(auth)

MAX_INTERACTION = 20 
MAX_VIEWED_STATUS = 200
MEDIA = "media"

def get_random_image_from_folder(folder):
    """Returns a random file from folder and the amount of files in the folder.
    It's up the user to check (or not) if the return file is actually an
    image.
    """
    media_list = []
    for dirpath, dirnames, files in os.walk(folder):
        for f in files:
            media_list.append(os.path.join(dirpath, f))
    media = random.choice(media_list)
    return media, len(media_list)

def twitter_bot(hashtag, delay):
    print(f"\n{datetime.datetime.now()}\n")
    interaction = 0
    for tweet in twitter.Cursor(api.search, q=hashtag, rpp=10).items(MAX_VIEWED_STATUS):
        if interaction==MAX_INTERACTION:
            break
        try:
            
            tweet_id = dict(tweet._json)["id"]
            tweet_text = dict(tweet._json)["text"]
            random_quote = random.choice(quotes)
            media, amount_media_available = get_random_image_from_folder(MEDIA)

            print("id: " + str(tweet_id))
            print("text: " + str(tweet_text))
            print("Random quote: " + random_quote)
            print("-------------------------")

            api.retweet(tweet_id)
            api.create_favorite(tweet_id)
            media = api.media_upload(media)
            api.update_status(status="", media_ids=[media.media_id], in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
            
            interaction += 1
            time.sleep(delay)

        except twitter.TweepError as error:
            print(error.reason)

while True:
    twitter_bot("#eddiehub", 5)
    time.sleep(60*60*2)
