import MeCab
import ast

def create_dict_each_file(file, dictionary):
    m = MeCab.Tagger ("-Owakati")
    with open(file) as iwanami_lines:
        for iwanami_line in iwanami_lines:
            # str -> dict
            iwanami_line = ast.literal_eval(iwanami_line)
            title_mecab = m.parse(iwanami_line['title'])
            for tilte in title_mecab.strip().split(" "):
                if dictionary.get(tilte) == None:
                    dictionary[tilte] = 1
                else:
                    dictionary[tilte] += 1
            words = iwanami_line['sentences'].split()
            for word in words:
                if dictionary.get(word) == None:
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1
    return dictionary

def get_dict(iwanami_file, tikuma_file):
    dictionary = {}
    dictionary = create_dict_each_file(iwanami_file, dictionary)
    dictionary = create_dict_each_file(tikuma_file, dictionary)
    with open('dict.txt' ,'w') as f:
        for word, num in dictionary.items():
            word = str(word)
            num = str(num)
            f.write(word + " " + num + "\n")