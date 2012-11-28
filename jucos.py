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

def reply_tweet(listin1, listin2):
    newest_id = API.GetUserTimeline()[0].id
    tl = API.GetFriendsTimeline(since_id=newest_id)
    for tweet in reply_pattern(tl):
        reply = '@' + tweet.user.screen_name + ' ' + random.choice(listin1).decode('utf-8')
        try:
            API.PostUpdate(reply, in_reply_to_status_id=tweet.id)
        except twitter.TwitterError:
            pass

    for tweet in jucos_pattern(tl):
        reply = '@' + tweet.user.screen_name + ' ' + random.choice(listin2).decode('utf-8')
        try:
            API.PostUpdate(reply, in_reply_to_status_id=tweet.id)
        except twitter.TwitterError:
            pass

def post_tweet(listin):
    if random.random() < 0.01:
        post = random.choice(listin)
        API.PostUpdate(post)

REPLY = 'reply.txt'
REPLY_JUCOS = 'reply_jucos.txt'
TWEET = 'tweet.txt'

reply_list = [line.strip() for line in open(REPLY)]
reply_jucos_list = [line.strip() for line in open(REPLY_JUCOS)]
tweet_list = [line.strip() for line in open(TWEET)]

reply_tweet(reply_list, reply_jucos_list)
post_tweet(tweet_list)
