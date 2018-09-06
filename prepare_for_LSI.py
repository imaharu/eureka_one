import ast
import re

def Classification_result(company): # ２値分類のみ対応
    if re.search(r'岩波文庫|岩波書店', company):
        return 1
    elif re.search(r'ちくま文庫|筑摩書房', company):
        return 0
    return -1

def LSI_data(file):
    with open(file,'r') as lines:
        documents = []
        for line in lines:
            # str -> dict
            str_line = ast.literal_eval(line)
            document = []
            if Classification_result(str_line['company']) == -1:
                continue
            for word in str_line['sentences'].split():
                document.append(word)
            documents.append(document)
        return documents

from gensim import corpora
from gensim import models

def create_LSI(documents):
    dic = corpora.Dictionary(documents)

    # no_below (int, optional) – Keep tokens which are contained in at least no_below documents.
    # no_above (float, optional) – Keep tokens which are contained in no more than no_above documents (fraction of total corpus size, not an absolute number).
    # keep_n (int, optional) – Keep only the first keep_n most frequent tokens.
    # keep_tokens (iterable of str) – Iterable of tokens that must stay in dictionary after filtering.
    dic.filter_extremes(no_below = 4, no_above = 0.3)
    bow_corpus = [dic.doc2bow(d) for d in documents]

    dic.save_as_text('train/dic.txt')
    tfidf_model = models.TfidfModel(bow_corpus,normalize=False) # L1正規化
    # tfidf_model = models.TfidfModel(bow_corpus) # L2正規化
    tfidf_corpus = tfidf_model[bow_corpus]
    tfidf_model.save('train/tfidf_model.model')

    lsi_model = models.LsiModel(tfidf_corpus, id2word = dic, num_topics = 200)
    lsi_model.save('train/lsi_model.model')