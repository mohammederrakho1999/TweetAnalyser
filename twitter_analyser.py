import tweepy
import json
from datetime import datetime, timedelta


# auth = tweepy.OAuthHandler("stJusTSACYyU5",
#                          "0wIWRZXxS45X814EHlaF")

# auth.set_access_token("1378006195034853377-8hpe1x",
#                     "IgPePoo3BmT3KplFD7abT")


# api = tweepy.API(auth, wait_on_rate_limit=True,
# wait_on_rate_limit_notify=True)


#timeline = api.home_timeline()
# for tweet in timeline:
#print(f"{tweet.user.name} said {tweet.text}")

def tweet_to_df(tweet):
    """take raw tweet receveid from stream into dataframe.
    """
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
    return dict_


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        # print(f"{tweet.user.name}:{tweet.text}")
        print(tweet)
        print("_"*80)
        dict_ = tweet_to_df(tweet)
        print(dict_)

    def on_error(self, status):
        print("Error detected")


# Authenticate to Twitter
auth = tweepy.OAuthHandler("stJusTSACYyU",
                           "0wIWRZXxS45X814EHlaFWEtrtHxUBIaB")

auth.set_access_token("1378006195034853377-8hpe1xq0",
                      "IgPePoo3BmT3KplFD7abTKMnjd9n")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["data science"], languages=["en"])
