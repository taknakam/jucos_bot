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

def id_pattern(fl):
    rst = set()
    for user in fl:
        rst.add(user.id)
    return rst

def unfollow_user():
    follower = API.GetFollowers()
    following = API.GetFriends()
    dist = id_pattern(following) - id_pattern(follower)
    for uid in dist:
        API.DestroyFriendship(uid)

if __name__ == "__main__":
    unfollow_user()
