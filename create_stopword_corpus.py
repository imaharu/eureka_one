def create_stopword():
    with open('stopword.txt', 'r') as words:
        stopwords = []
        for word in words:
            stopwords.append(word.replace('\n',''))
        return stopwords