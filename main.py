from get_data import *
from create_dict import *
from prepare_for_LSI import *

from gensim import corpora
from gensim import models
import numpy as np

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler

documents = LSI_data("increase_data/increase.all")

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

with open("increase_data/increase.all",'r') as lines:
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

train_num = 100
accuracy_scores = 0
precision_scores = 0
recall_scores = 0
f1_scores = 0
sc=StandardScaler()
sc.fit(X)

for j in range(1):
    accuracy_scores = 0
    precision_scores = 0
    recall_scores = 0
    f1_scores = 0
    for i in range(train_num):
        X_std=sc.transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=0.2)
        y_train = np.reshape(y_train,(-1))
        y_test = np.reshape(y_test,(-1))
        clf = svm.SVC(C=1.7, kernel="rbf")
        clf.fit(X_train, y_train)
        
        accuracy_scores += accuracy_score(y_test, clf.predict(X_test)) # 正解率
        precision_scores += precision_score(y_test, clf.predict(X_test)) # 精度
        recall_scores += recall_score(y_test, clf.predict(X_test)) # 検出率
        f1_scores += f1_score(y_test, clf.predict(X_test)) # F値
        # print(accuracy_scores)

    print("------------------")
    print("正解率", accuracy_scores / train_num)
    print("精度", precision_scores / train_num)
    print("検出率", recall_scores / train_num)
    print("F値", f1_scores / train_num)
    print("------------------")