#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import twitter

CONSUMER_KEY = 'n3vSvKuSflbWReWJdd14Q'
CONSUMER_SECRET = 'C3yE36ixNwJKLA6bSnlYpxG4Dv8HXBK8qSGPKySISDk'
OAUTH_TOKEN = '599641427-sMeSS2jQNzQ1U2UJanml8sBfLA1cZmBOZ5jJqa4O'
OAUTH_TOKEN_SECRET = 'MlWKKkH6aorG7Fsmm7TadsxRNksf4vQMwrPoaoWE'

API = twitter.Api(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token_key=OAUTH_TOKEN,
    access_token_secret=OAUTH_TOKEN_SECRET
)

def jucos_pattern(tl):
    """
    Yield tweets that are not posted by 'jucos_bot'
    and contain 'ジャコス' or 'ジャスコ'.
    """
    for tweet in tl:
        if ((tweet.user.screen_name != 'jucos_bot') and
            (u'ジャコス' in tweet.text or u'ジャスコ' in tweet.text)):
            yield tweet

def reply_pattern(tl):
    """
    Yield tweets that are not posted by 'jucos_bot'
    and contain '@jucos_bot'
    """
    for tweet in tl:
        if ((tweet.user.screen_name != 'jucos_bot') and
            (u'@jucos_bot' in tweet.text)):
            yield tweet

def reply_tweet():
    newest_id = API.GetUserTimeline()[0].id
    # newest_id = max(tl, key=lambda x: x.id).id
    tl = API.GetFriendsTimeline(since_id=newest_id)
    for tweet in reply_pattern(tl):
        reply = u'@' + tweet.user.screen_name + u' ええー……っ'
        print reply
        try:
            API.PostUpdate(reply, in_reply_to_status_id=tweet.id)
        except twitter.TwitterError:
            pass
    for tweet in jucos_pattern(tl):
        reply = u'@' + tweet.user.screen_name + u' ジャコス行くの！！？'
        print reply
        try:
            API.PostUpdate(reply, in_reply_to_status_id=tweet.id)
        except twitter.TwitterError:
            pass

def post_tweet(listin):
    if random.random() < 0.05:
        post = random.choice(listin)
        print post
        API.PostUpdate(post)

FILENAME = 'tweet.txt'

tweet_list = [line.strip() for line in open(FILENAME)]
reply_tweet()
post_tweet(tweet_list)
