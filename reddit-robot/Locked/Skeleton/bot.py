
import praw
from prawoauth2 import PrawOAuth2Mini
from tokens import app_key, app_secret, access_token, refresh_token, scopes


user_agent = "Drunken PRAWL"
reddit_client = praw.Reddit(user_agent=user_agent)
oauth_helper = PrawOAuth2Mini(reddit_client, app_key='MY_KEY',
                              app_secret='MY_SECRET_KEY', access_token='ACCESS_TOKEN',
                              scopes=scopes, refresh_token='REFRESH_TOKEN')
already_done = set()

def loop():
    oauth_helper.refresh()
    for comment in reddit_client.get_comments('DrunkenPrawl'):
        if 'im drunk' in comment.body.lower() and comment.id not in already_done:
            print('Time to shitpost')
            comment.reply('Give me your height, weight, and sex (like this: **5\'8", 150 lb, Male**). I\'ll tell you how much you *probably* had!')
            already_done.add(comment.id)
while True:
    try:
        loop()
    except praw.errors.OAuthInvalidToken:
        # token expired, refresh 'em!
        oauth_helper.refresh()
