from get_data import *
from create_dict import *
from create_complete_corpus import *
import tensorflow as tf
import numpy as np
# get_simple_data('iwanami.txt')
# get_dict('uniq_complete.corpus.iwanami','uniq_complete.corpus.tikuma')
# create_complete_corpus('uniq_complete.corpus.iwanami','uniq_complete.corpus.tikuma')
# 23312の辞書

depth = 23312
sess = tf.Session()

with open('delete_model') as lines:
    for line in lines:
        line = line.split(',')
        sentence = np.array(line[2].split())
        sentence = tf.one_hot(sentence, depth)

        print(sess.run(sentence))
        break