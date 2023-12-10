import pandas as pd
import numpy as np
import math
from collections import Counter
import re

df = pd.read_csv('annotated_articles.csv')

articles = df.iloc[:, :2]
categories = df.iloc[:, 4]

def tokenize(document):
    words = [re.sub(r'[^a-zA-Z0-9]+', '', word.lower()) for word in document.split()]
    return words


def calculate_tf(data):
    tf_matrix = []
    for document in data:
        tf_vector = Counter(tokenize(document))
        tf_matrix.append(tf_vector)
    return tf_matrix

def calculate_idf(data):
    word_doc_count = Counter()
    for document in data:
        words = set(tokenize(document))
        word_doc_count.update(words)

    idf_values = {}
    total_docs = len(data)
    for word, doc_count in word_doc_count.items():
        idf_values[word] = math.log(total_docs / (doc_count + 1))

    return idf_values

tf_matrix = calculate_tf(articles.iloc[:, 0])

idf_values = calculate_idf(articles.iloc[:, 0])

tfidf_matrix = []
for tf_vector in tf_matrix:
    tfidf_vector = {word: tf * idf_values.get(word, 0) for word, tf in tf_vector.items()}
    tfidf_matrix.append(tfidf_vector)

df_tfidf = pd.DataFrame(tfidf_matrix).fillna(0)

df_tfidf['category'] = categories.values
average_tfidf_by_category = df_tfidf.groupby('category').mean()

top_words_by_category = {}
for category in average_tfidf_by_category.index:
    top_words = average_tfidf_by_category.loc[category].nlargest(10).index.tolist()
    top_words_by_category[category] = top_words

for category, top_words in top_words_by_category.items():
    print(f'Top words in category "{category}": {", ".join(top_words)}')
