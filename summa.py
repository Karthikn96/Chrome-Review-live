import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import numpy as np
import string
import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import wordnet
import streamlit.components.v1 as stc


st.title("Question 1 Part 2")
