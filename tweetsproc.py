import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import re
from datetime import datetime
from geopy.geocoders import Nominatim
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer


data = pd.read_csv("data/1.csv")
data1 = pd.read_csv("data/2.csv")
data2 = pd.read_csv("data/3.csv")
data3 = pd.read_csv("data/4.csv")
data4 = pd.read_csv("data/5.csv")

frames = [data, data1, data2, data3, data4]
result = pd.concat(frames)

stopwords = stopwords.words('english')
stopwords = list(stopwords)


def word(text):
    """Function to get list of words ignoring stopwords."""
    words = []
    text = re.sub(r'[?|$|.|!-/]', r'', text.lower())
    for word in text.split():
        if word.startswith(("http", "@", "#")):
            continue
        if word not in stopwords:
            words.append(word)
    return words


def get_cities_country(df, column_name):
    try:
        df["city"] = df[column_name].apply(lambda x: str(x).split(",")[0])
    except Exception as e:
        pass
    return True


def get_lat_log(df, column_name):
    geolocator = Nominatim(user_agent="mohammed")
    df["latitude"] = df[column_name].apply(
        lambda x: geolocator.geocode(x).latitude)
    df["longitude"] = df[column_name].apply(
        lambda x: geolocator.geocode(x).longitude)
    return True

# this function is for dash viz.
# def getTweetsPerCity(df):
    #_dict = dict(df.groupby(["city"])["text"].count())
    # return _dict


def freq(_list):

    # gives set of unique words
    unique_words = set(_list)
    _dict = dict()

    for words in unique_words:
        _dict[words] = _list.count(words)
    return _dict


def get_sentiment(text):
    blob_object = TextBlob(text, analyzer=NaiveBayesAnalyzer())
    analysis = blob_object.sentiment
    if analysis.p_pos > 0.5:
        return "positive"
    else:
        return "negative"


def proccess_tweets(df):
    df["word_list"] = df["text"].apply(lambda x: word(x))
    get_cities_country(df, "user_location")
    get_lat_log(df, "city")
    df["sentiment"] = df["text"].apply(lambda x: get_sentiment(x))
    df["freq"] = df["word_list"].apply(lambda x: freq(x))
    return df.to_csv(f"C:/Users/info/Desktop/projects/tweetanalyser/data/tweets_clean.csv")
