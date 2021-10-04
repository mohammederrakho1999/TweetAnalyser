import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import re
from datetime import datetime


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


result["word_list"] = result["text"].apply(lambda x: word(x))
get_cities_country(result, "user_location")
