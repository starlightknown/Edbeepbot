# EDBEEPBOT 

### An open source bot which retweets '#Eddiehub' and replies with Eddie Quotes and Images

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
## [@Edbeepbot](https://twitter.com/Edbeepbot) on Twitter

<img src="twitter.png">
<a href="https://twitter.com/Edbeepbot" target="_blank"><img src="https://cdn2.iconfinder.com/data/icons/social-media-2199/64/social_media_isometric_6-twitter-512.png" height="120px" width="120px" alt="Twitter" align="center"></a>
<a href="https://github.com/kcoder63/"><img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="Built with Love"></a><br>

## Twitter Reply-Retweet Bot using Python & Tweepy
A Python-built Twitter retweet bot using Tweepy. Searches and retweets based on hashtag or keyword. Can do multiple keywords, or hashtags.

What You Need && Need to Know
----------

* [Tweepy](http://www.tweepy.org/) - An easy-to-use Python library for accessing the Twitter API.

`pip3 install tweepy`

* Make sure you fully understand [Twitter's Rules on Automation](https://support.twitter.com/articles/76915). Play nice. Don't spam! 
* Please do read [CONTRIBUTING.md](https://github.com/kcoder63/Edbeepbot/blob/main/CONTRIBUTING.md) if you want to contribute to this project.

Instructions
----------

* Out of general OS hygiene, create a new directory to contain all of your retweet bot files.

`mkdir edbeepbot`

* Create a new [Twitter Application](https://apps.twitter.com/app/new). This is where you'll generate your keys, tokens, and secrets.
* Fill in your keys, tokens, and secrets in `keys.py`
* The example demonstrates a single hashtag value, but you can tweak the code to search multiple hashtags. Example:

 `Search = "BOT"` This will search bot in tweets and retweet and reply to it. You can use words, images and quotes of your choice.
 You can add your collection of Eddie Quotes to `quotes.py`.
* Run your `main.py` script. Enjoy! 

`python3 main.py`


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://jaid.tech/"><img src="https://avatars.githubusercontent.com/u/33520257?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Jai Kumar Dewani</b></sub></a><br /><a href="https://github.com/kcoder63/Edbeepbot/commits?author=jai-dewani" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Vyvy-vi"><img src="https://avatars.githubusercontent.com/u/62864373?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Vyom Jain</b></sub></a><br /><a href="#question-vyvy-vi" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/adityaraute"><img src="https://avatars.githubusercontent.com/u/43912470?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Aditya Raute</b></sub></a><br /><a href="https://github.com/kcoder63/Edbeepbot/issues?q=author%3Aadityaraute" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://linkedin.com/in/patel-himanshu"><img src="https://avatars.githubusercontent.com/u/44549418?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Himanshu Patel</b></sub></a><br /><a href="https://github.com/kcoder63/Edbeepbot/commits?author=patel-himanshu" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
