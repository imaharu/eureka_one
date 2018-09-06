from get_data import *
from create_dict import *
from prepare_for_LSI import *

from gensim import corpora
from gensim import models

import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np
import os

# get_simple_data('iwanami.txt')
# get_dict('uniq_complete.corpus.iwanami','uniq_complete.corpus.tikuma')
# create_complete_corpus('uniq_complete.corpus.iwanami','uniq_complete.corpus.tikuma')

documents = LSI_data("uniq_coplete_data/uniq_all_corpus")
# create_LSI(documents)

dic = corpora.Dictionary.load_from_text('train/dic.txt')

bow_corpus = [dic.doc2bow(d) for d in documents]

tfidf_model = models.TfidfModel(bow_corpus)

tfidf_corpus = tfidf_model[bow_corpus]

lsi_model = models.LsiModel.load('train/lsi_model.model')
lsi_corpus = lsi_model[tfidf_corpus]

X = []

for lsi in lsi_corpus:
    x = []
    for tuples in lsi:
        x.append(tuples[1])
    X.append(x)

with open("uniq_coplete_data/uniq_all_corpus",'r') as lines:
    y = []
    for line in lines:
        # str -> dict
        str_line = ast.literal_eval(line)
        if Classification_result(str_line['company']) == -1:
            continue
        if re.search(r'岩波文庫|岩波書店', str_line['company']):
            y.append([1])
        else:
            y.append([0])

sc=StandardScaler()
sc.fit(X)

k = 0
for i in range(500):
    X_std=sc.transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=0.2)
    y_train=np.reshape(y_train,(-1))
    y_test=np.reshape(y_test,(-1))
    clf = SGDClassifier() # 平均 0.851444444444
    # clf = svm.SVC(kernel='rbf')
    clf.fit(X_train, y_train)
    k += np.mean(clf.predict(X_test) == y_test)
    print(np.mean(clf.predict(X_test) == y_test))

print("平均", k / 500)