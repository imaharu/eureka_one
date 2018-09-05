from get_data import *
from create_dict import *
from create_complete_corpus import *
from prepare_for_LSI import *

from gensim import corpora
from gensim import models

import tensorflow as tf
import numpy as np

# get_simple_data('iwanami.txt')
# get_dict('uniq_complete.corpus.iwanami','uniq_complete.corpus.tikuma')
# create_complete_corpus('uniq_complete.corpus.iwanami','uniq_complete.corpus.tikuma')

# 名詞のリストになった記事群

documents = LSI_data("uniq_coplete_data/uniq_coplete_all_corpus")
print(documents)

# dic = corpora.Dictionary(documents)
# print(dic)
# # no_below (int, optional) – Keep tokens which are contained in at least no_below documents.
# # no_above (float, optional) – Keep tokens which are contained in no more than no_above documents (fraction of total corpus size, not an absolute number).
# # keep_n (int, optional) – Keep only the first keep_n most frequent tokens.
# # keep_tokens (iterable of str) – Iterable of tokens that must stay in dictionary after filtering.
# dic.filter_extremes(no_below = 2, no_above = 0.8)
# print(dic)
# bow_corpus = [dic.doc2bow(d) for d in documents]
# dic.save_as_text('FILEPATH/livedoordic.txt')

# tfidf_model = models.TfidfModel(bow_corpus)
# tfidf_corpus = tfidf_model[bow_corpus]
# tfidf_model.save('FILEPATH/tfidf_model.model')

# 23312の辞書

# depth = 23312
# sess = tf.Session()

# with open('delete_model') as lines:
#     for line in lines:
#         line = line.split(',')
#         sentence = np.array(line[2].split())
#         sentence = tf.one_hot(sentence, depth)

#         print(sess.run(sentence))
#         break