import tweepy
import json
from datetime import datetime, timedelta
from s3_module import *
import pandas as pd
import os
import os.path


def helper(dir):
    count = 0
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            count += 1
    return count


def tweet_to_df(tweet):
    """take raw tweet receveid from stream into dataframe.
    """

    count = helper("./data")

    dict_ = {}
    dict_["text"] = tweet.text
    dict_["user"] = tweet.user.description
    dict_["user_location"] = tweet.user.location
    dict_["screem_name"] = tweet.user.screen_name
    dict_["account_date_cr"] = tweet.user.created_at
    dict_["nb_followers"] = tweet.user.followers_count
    dict_["profile_color"] = tweet.user.profile_background_color
    dict_["tweet_id"] = tweet.id_str
    dict_["tweet_date"] = tweet.created_at
    dict_["nb_retweeted"] = tweet.retweet_count
    dict_["tweet coordinates"] = tweet.coordinates

    tweet_data = pd.DataFrame(dict_, index=[0])
    return tweet_data.to_csv(f"C:/Users/info/Desktop/projects/tweetanalyser/data/{count+1}.csv")


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        # print(f"{tweet.user.name}:{tweet.text}")
        print(tweet)
        print("_"*80)
        tweet_to_df(tweet)
        # upload_file(dict_)

    def on_error(self, status):
        print("Error detected")


# Authenticate to Twitter
auth = tweepy.OAuthHandler("stJusTSACYyU5lMy*****",
                           "0wIWRZXxS45X814EH***")

auth.set_access_token("1378006195034853377-8hpe1xq0**",
                      "IgPePoo3BmT3KplFD7abTKMnjd***")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["data science"], languages=["en"])
