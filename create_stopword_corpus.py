def create_stopword():
    with open('important_data/stopword.txt', 'r') as words:
        stopwords = []
        for word in words:
            stopwords.append(word.replace('\n',''))
        return stopwords