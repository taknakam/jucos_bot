#!/usr/bin/env python
# -*- coding: utf-8 -*-

import twitter
import os
import re
import random
from time import sleep

CONSUMER_KEY = 'n3vSvKuSflbWReWJdd14Q'
CONSUMER_SECRET = 'C3yE36ixNwJKLA6bSnlYpxG4Dv8HXBK8qSGPKySISDk'
OAUTH_TOKEN = '599641427-sMeSS2jQNzQ1U2UJanml8sBfLA1cZmBOZ5jJqa4O'
OAUTH_TOKEN_SECRET = 'MlWKKkH6aorG7Fsmm7TadsxRNksf4vQMwrPoaoWE'

api = twitter.Api(
    consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    access_token_key = OAUTH_TOKEN,
    access_token_secret = OAUTH_TOKEN_SECRET)

def createdict(filenamein):
    file = open(filenamein)
    list = file.readlines()
    dict = [x for x in list]
    file.close()
    return dict

def replytweet(dictin, filenamesincein):
    file = open(filenamesincein, "r+")
    since = file.readline()
    tl = api.GetFriendsTimeline(since_id=int(since))
    for tweet in tl:
        file.seek(0)
        file.write(str(tweet.id))
        if jucos.search(tweet.text) or jusco.search(tweet.text) is not None:
            if tweet.user.screen_name!="jucos_bot":
                reply = "@" + tweet.user.screen_name + u' ジャコス行くの！？'
                # print reply
                api.PostUpdate(reply, in_reply_to_status_id=tweet.id)
    file.close()
        
def posttweet(dictin):
    if random.random() < 0.01:
        post = random.choice(dictin)
        # print post
        api.PostUpdate(post)
    
filename = "tweet.txt"
filenamesince = "tweetid.txt"
jucos = re.compile(u'ジャコス')
jusco = re.compile(u'ジャスコ')

dict = createdict(filename)
replytweet(dict, filenamesince)
posttweet(dict)
