from google_play_scraper import app, reviews, Sort, reviews_all
import pandas as pd
pd.options.mode.chained_assignment = None

import numpy as np
seed = 0
np.random.seed(seed)

import matplotlib.pyplot as plt
import seaborn as sns

import datetime as dt
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

from wordcloud import WordCloud
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from google_play_scraper import app, reviews_all, Sort

scrapreview = reviews_all(
    'com.finaccel.android',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=3500
)
# Menyimpan ulasan dalam file CSV
import csv

with open('ulasan_kredivo.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scrapreview:
        writer.writerow([review['content']])
app_reviews_df = pd.DataFrame(scrapreview)
app_reviews_df.shape
app_reviews_df.head()
app_reviews_df.to_csv('ulasan_kredivo.csv', index=False)