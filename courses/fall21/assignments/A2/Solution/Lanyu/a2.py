import pandas as pd
import nltk
import re
import numpy as np
import math
from collections import Counter
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix,f1_score, precision_score,recall_score, accuracy_score
from sklearn.preprocessing import normalize

nltk.download('punkt')
nltk.download('wordnet') 


def preprocess(text):
  text = str(text)
  text = text.lower()
  urls = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
  text = re.sub(urls, '', text)
  text = re.sub(r'\d+', '', text)
  text = re.sub(r'[@#][^\s]+', '', text)
  text = re.sub(r'[^\w\s]', '', text)
  text = " ".join(text.split())
  
  tokens = word_tokenize(text)
  text = " ".join([i for i in tokens if not i in ENGLISH_STOP_WORDS])

  lemmatizer=WordNetLemmatizer()
  tokens = word_tokenize(text)
  text = " ".join([lemmatizer.lemmatize(i)for i in tokens])
  
  return text

def doc_freq(word):
  c = 0
  try:
    c = DF[word]
  except:
    pass
  return c

def calculate_tfidf(tweets):
  tf_idf = {}
  doc = 0
  N = len(tweets)
  for i in range(N):
    tokens = word_tokenize(tweets[i])
    counter = Counter(tokens)
    words_count = len(tokens)
    for token in np.unique(tokens):
      tf = counter[token]/words_count
      df = doc_freq(token)
      idf = np.log((N+1)/(df+1))
      tf_idf[doc, token] = tf*idf
    doc += 1
  return tf_idf

def gen_vector(tokens):
  Q = np.zeros((len(total_vocab)))
  counter = Counter(tokens)
  words_count = len(tokens)
  
  for token in np.unique(tokens):
      
      tf = counter[token]/words_count
      df = doc_freq(token)
      idf = math.log((N+1)/(df+1))
      try:
          ind = total_vocab.index(token)
          Q[ind] = tf*idf
      except:
          pass
  return Q
if __name__ == '__main__':
  df_train = pd.read_csv("./data/tweets_train.csv", index_col=0)
  df_val = pd.read_csv("./data/tweets_validation.csv", index_col=0)
  df_test = pd.read_csv("./data/tweets_test.csv", index_col=0)

  df_train['tweet_clean'] = df_train.apply(lambda row: preprocess(row['tweet']), axis=1)
  df_test['tweet_clean'] = df_test.apply(lambda row: preprocess(row['tweet']), axis=1)
  df_val['tweet_clean'] = df_val.apply(lambda row: preprocess(row['tweet']), axis=1)

  # Task 1
  vocab = {}
  DF = {}
  tweets = df_train['tweet_clean']
  N = len(tweets)
  for i in range(len(tweets)):
    tokens = word_tokenize(tweets[i])
    for w in tokens:
          try:
              vocab[w].add(i)
          except:
              vocab[w] = {i}
  for i in vocab:
      DF[i] = len(vocab[i])

  tf_idf = calculate_tfidf(tweets)
  total_vocab_size = len(DF)
  print(f"Total Vocab Size: {total_vocab_size}")

  # Task 2
  D = np.zeros((N, total_vocab_size))
  total_vocab = [x for x in DF]
  for i in tf_idf:
    try:
      ind = total_vocab.index(i[1])
      D[i[0]][ind] = tf_idf[i]
    except:
        pass

  

  tweets_train = df_train['tweet_clean']
  tweets_val = df_val['tweet_clean']
  tweets_test = df_test['tweet_clean']
  y_train = df_train['label_binary']
  y_val = df_val['label_binary']

  tfidf_train = D 
  N_val = len(tweets_val)
  N_test = len(tweets_test)
  tfidf_val = []
  tfidf_test = []

  for i in range(N_val):
    tokens = word_tokenize(tweets_val[i])
    v = gen_vector(tokens)
    tfidf_val.append(v)

  for i in range(N_test):
    tokens = word_tokenize(tweets_test[i])
    v = gen_vector(tokens)
    tfidf_test.append(v)

  tfidf_val = np.vstack(tfidf_val)
  tfidf_test = np.vstack(tfidf_test)
  

  # Task 3
  tfidf_train = normalize(tfidf_train, norm='l2')
  tfidf_val = normalize(tfidf_val, norm='l2')
  tfidf_test = normalize(tfidf_test, norm='l2')

  model = LogisticRegression(random_state=123).fit(tfidf_train, y_train)
  # model = MultinomialNB().fit(tfidf_train, y_train)
  # model = RandomForestClassifier(random_state=123).fit(tfidf_train, y_train)
  prediction = model.predict_proba(tfidf_val) 
  prediction_int = prediction[:,1] >= 0.45 
  prediction_int = prediction_int.astype(np.int)

  cf_matrix =confusion_matrix(y_val, prediction_int)
  tn, fp, fn, tp = confusion_matrix(y_val, prediction_int).ravel()
  print("Precision: {:.2f}%".format(100 * precision_score(y_val, prediction_int)))
  print("Recall: {:.2f}%".format(100 * recall_score(y_val, prediction_int)))
  print("F1 Score: {:.2f}%".format(100 * f1_score(y_val, prediction_int)))
  print("accuracy_score : {:.2f}%".format(100 * accuracy_score(y_val, prediction_int)))

