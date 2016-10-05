from lxml import html
import requests
import time
import datetime
import random
import pylab
from matplotlib.patches import Ellipse
import praw
from prawoauth2 import PrawOAuth2Mini
from tokens import app_key, app_secret, access_token, refresh_token, scopes
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

tracktime = time.time() #datetime when it was initialized so it doesn't post on old content 

user_agent = "Drunken PRAWL"
user_name = "DrunkWhenSober"
reddit_client = praw.Reddit(user_agent=user_agent)
oauth_helper = PrawOAuth2Mini(reddit_client, app_key='cnCoU2zAAb6IEA',
                              app_secret='-8F3XR-_-In7LENvBj7YKnmTG9s', access_token='isCMLVCkYF2RaTBm5mgBEYRoQ50',
                              scopes=scopes, refresh_token='44644420-0vrXSISDaSu3ThXYEhwldIj80gg')
already_done = set()
comment_count = []
plt.ion()
fig = plt.figure(figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0,50), ylim=(0,5000))

plt.xlabel("Time")
plt.ylabel("Number of Comments")

def loop():
    oauth_helper.refresh()
    
    submissions = reddit_client.get_subreddit('all').get_hot(limit=100)
    
    range_height = 200;
    for posts in submissions:
        if posts.id not in already_done:
            comment_count.append(posts.num_comments)
            ax.plot(comment_count)
            if(posts.ups > 2000 and posts.num_comments > 750):
                ax.annotate(posts.title[:50]+"...", xy=(len(comment_count) - 1, posts.num_comments), xycoords='data',
                            xytext=(0, range_height), textcoords='offset points',
                            size=10, bbox=dict(boxstyle="round4", fc="w"),  
                            arrowprops=dict(arrowstyle="-|>",
                            connectionstyle="arc3,rad=.2",
                            fc="w"))
                range_height = range_height - 20
                if(range_height < 10):
                    range_height = 200
            already_done.add(posts.id)
            plt.pause(0.0000    1)
        else:
            time.sleep(200)

while True:
    try:
        loop()
    except praw.errors.OAuthInvalidToken:
        # token expired, refresh 'em!
        oauth_helper.refresh()
