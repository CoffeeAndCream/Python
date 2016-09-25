from lxml import html
import requests
import time
import praw
from prawoauth2 import PrawOAuth2Mini
from tokens import app_key, app_secret, access_token, refresh_token, scopes

user_agent = "Drunken PRAWL"
reddit_client = praw.Reddit(user_agent=user_agent)
oauth_helper = PrawOAuth2Mini(reddit_client, app_key='cnCoU2zAAb6IEA',
                              app_secret='-8F3XR-_-In7LENvBj7YKnmTG9s', access_token='isCMLVCkYF2RaTBm5mgBEYRoQ50',
                              scopes=scopes, refresh_token='44644420-0vrXSISDaSu3ThXYEhwldIj80gg')
already_done = set()
yUrl = ""
def loop():
    oauth_helper.refresh()
    page = requests.get("https://www.youtube.com/results?search_query=" + str("jazz+music"))
    tree = html.fromstring(page.content)
    yUrl = tree.xpath('//*[@id="results"]/ol/li/ol/li/div/div/div[1]/a/@href')
    nUrl = 'https://www.youtube.com' + str(yUrl[0])
    for comment in reddit_client.get_comments('DrunkenPrawl'):
       if 'YOUTUBE BOT PLEASE HELP!' in comment.body and comment.id not in already_done:
           print('Time to shitpost')
           comment_p = str(comment)
           comment_p = comment_p[24:]
           page = requests.get("https://www.youtube.com/results?search_query=" + str(comment_p))
           tree = html.fromstring(page.content)
           yUrl = tree.xpath('//*[@id="results"]/ol/li/ol/li/div/div/div[1]/a/@href')
           nUrl = 'https://www.youtube.com' + str(yUrl[0]) + '\n\nhttps://www.youtube.com' + str(yUrl[1])+ '\n\nhttps://www.youtube.com' + str(yUrl[2])
           comment.reply(nUrl)
           already_done.add(comment.id)
while True:
    try:
        loop()
    except praw.errors.OAuthInvalidToken:
        # token expired, refresh 'em!
        oauth_helper.refresh()