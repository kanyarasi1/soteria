import os
import json
import csv
import sys
import datetime as dt
from credentials import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy
from tweepy import OAuthHandler, API


def authorize():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


api = API(authorize())


def get_tweets(user):
    query = "@" + user
    csvFile = open('tweets.csv', 'a')
    csvWriter = csv.writer(csvFile)
    today = dt.date.today()
    week_ago = today - dt.timedelta(days=7)

    # Fetching the mentions of the user over one week
    for tweet in tweepy.Cursor(api.search, q=query, count=10,
                               lang="en",
                               since=week_ago).items():
        print(tweet.text)
        csvWriter.writerow([tweet.text.encode('utf-8')])
