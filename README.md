# Edbeepbot - A bot which retweets #Eddiehub 
# Twitter Retweet Bot using Python & Tweepy
A Python-built Twitter retweet bot using Tweepy. Searches and retweets based on hashtag or keyword. Can do multiple keywords, or hashtags.

What You Need && Need to Know
----------

* [Tweepy](http://www.tweepy.org/) - An easy-to-use Python library for accessing the Twitter API.

`pip install tweepy`

* Make sure you fully understand [Twitter's Rules on Automation](https://support.twitter.com/articles/76915). Play nice. Don't spam! 

Instructions
----------

* Out of general OS hygiene, create a new directory to contain all of your retweet bot files.

`mkdir retweet-bot`

* Create a new [Twitter Application](https://apps.twitter.com/app/new). This is where you'll generate your keys, tokens, and secrets.
* Fill in your keys, tokens, and secrets.
* Check comments in retweet.py to tweak the retweet bot to your liking.
* The example demonstrates a single hashtag value, but you can tweak the code to search multiple hashtags. Example:

 `q='%23apples%20OR%20%23oranges' will search #apples OR #oranges`
* Run your retweet.py script. Enjoy! 

`python retweet.py`

