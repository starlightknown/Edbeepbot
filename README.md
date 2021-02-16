# Edbeepbot - An open source bot which retweets #Eddiehub and replies with Eddie Quotes
# Please do read CONTRIBUTING.md if you want to contribute to this project
## @Edbeepbot on twitter
<a href="https://twitter.com/Edbeepbot" target="_blank"><img src="https://cdn2.iconfinder.com/data/icons/social-media-2199/64/social_media_isometric_6-twitter-512.png" height="120px" width="120px" alt="Twitter" align="center"></a>
<a href="https://github.com/kcoder63/"><img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="built with Love"></a><br>
# Twitter Retweet Bot using Python & Tweepy
A Python-built Twitter retweet bot using Tweepy. Searches and retweets based on hashtag or keyword. Can do multiple keywords, or hashtags.

What You Need && Need to Know
----------

* [Tweepy](http://www.tweepy.org/) - An easy-to-use Python library for accessing the Twitter API.

`pip3 install tweepy`

* Make sure you fully understand [Twitter's Rules on Automation](https://support.twitter.com/articles/76915). Play nice. Don't spam! 

Instructions
----------

* Out of general OS hygiene, create a new directory to contain all of your retweet bot files.

`mkdir retweet-bot`

* Create a new [Twitter Application](https://apps.twitter.com/app/new). This is where you'll generate your keys, tokens, and secrets.
* Fill in your keys, tokens, and secrets.
* Check comments in main.py to tweak the retweet bot to your liking.
* The example demonstrates a single hashtag value, but you can tweak the code to search multiple hashtags. Example:

 `Search = "BOT"` This will search bot in tweets and retweet it. You can use words of your choice.
 You can add your collection of Eddie Quotes to quotes.py.
* Run your eddiebot.py script. Enjoy! 

`python3 main.py`

