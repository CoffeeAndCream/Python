import praw
from prawoauth2 import PrawOAuth2Server
 
user_agent = 'DrunkenPrawler'
reddit_client = praw.Reddit(user_agent=user_agent)
 
scopes = ['identity', 'read', 'submit']
oauthserver = PrawOAuth2Server(reddit_client, 'cnCoU2zAAb6IEA', '-8F3XR-_-In7LENvBj7YKnmTG9s',
                                state=user_agent, scopes=scopes)
                                
oauthserver.start()

tokens = oauthserver.get_access_codes()


import re
import time
import praw
from prawoauth2 import PrawOAuth2Mini
from tokens import app_key, app_secret, access_token, refresh_token



UA = 'ListFormatFixer praw demo, Created by /u/shaggorama'


def check_condition(c):
    text = c.body
    tokens = text.split()
    if "1)" in tokens and "2)" in tokens:
        return True

def bot_action(c, verbose=True, respond=False):
    fixed = re.sub(r'(\n?)([0-9]+)(\))', r'\n\n\2.', c.body)

    if verbose:
        print c.body.encode("UTF-8")
        print "\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"
        print fixed.encode("UTF-8")

    if respond:
        head = "Hi! Let me try to beautify the list in  your comment:\n\n"
        tail = "\n\nI am a bot. You can provide feedback in my subreddit: /r/ListFormatFixer"
        c.reply(head + fixed + tail)


user_agent = 'DrunkWhenSober. Contact me at /u/DrunkWhenSober or /r/DrunkenPrawl'
r = praw.Reddit(UA)
reddit_client = praw.Reddit(user_agent=user_agent)

oauth_helper = PrawOAuth2Mini(reddit_client, app_key='cnCoU2zAAb6IEA',
                               app_secret='-8F3XR-_-In7LENvBj7YKnmTG9s',
                               access_token=access_token,
                               refresh_token=refresh_token, scopes=scopes)
while True:
    for c in praw.helpers.comment_stream(r, 'DrunkenPrawl'):
        if check_condition(c):
            # set 'respond=True' to activate bot responses. Must be logged in.
            bot_action(c, respond=True)

    time.sleep(5)
    oauth_helper.refresh()
            