import subprocess
from create_stopword_corpus import *
stopwords = create_stopword()

def get_simple_data(file_path):
    with open(file_path) as lines:
        infos = []
        i = 0
        for line in lines:
            i = i + 1
            cols  = line.split(',')
            info = {
                'title' :  cols[1], # タイトル
                'company' : cols[28] # 出版社
            }

            info.setdefault('sentences', '<unk>')
            cmd = "cat test50.txt | grep %s" % cols[55] # utf8_delete_over50.txt test50.txt
            try:
                get_same_book_data_from_corpus = subprocess.check_output(cmd, shell=True).decode('utf8')
            except:
                print("Shell Error.")
            get_same_book_data_from_corpus = get_same_book_data_from_corpus.split('\n')
            sentence = reconfigure_separte_to_oneLine(get_same_book_data_from_corpus)
            info["sentences"] = sentence
            print(info)
            print("---------------")
            if i == 1:
                break

def reconfigure_separte_to_oneLine(get_same_book_data_from_corpus):
    sentence = []
    for line_corpus in get_same_book_data_from_corpus:
        if line_corpus:
            # mecabの基本形をとっている
            if line_corpus.split(',')[-3] not in stopwords: sentence.append(line_corpus.split(',')[-3])
    return ' '.join(sentence)

def show_data_label():
    with open('aozora_word_list_utf8.csv') as lines:
        for line in lines:
            line_split = line.split(',')
            for i, name in enumerate(line_split):
                print(i, name)
            break

def delete_text_line_count():
    with open('utf8_delete_over50.txt', 'w') as f:
        with open('utf8_all.csv') as lines:
            for line in lines:
                cols  = line.split(',')
                if int(cols[1]) <= 50:
                    print("line", line)
                    f.write(line)