import praw
from prawoauth2 import PrawOAuth2Server
from tokens import app_key, app_secret, scopes

user_agent = 'Drunken Prawler: teaching me computer stuff' 
reddit_client = praw.Reddit(user_agent=user_agent)
oauthserver = PrawOAuth2Server(reddit_client, app_key='cnCoU2zAAb6IEA',
                               app_secret='-8F3XR-_-In7LENvBj7YKnmTG9s', state=user_agent,
                               scopes=scopes)
# start the server, this will open default web browser
# asking you to authenticate        
oauthserver.start()
tokens = oauthserver.get_access_codes()
print(tokens)

