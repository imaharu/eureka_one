import ast
def LSI_data(file):
    with open(file,'r') as lines:
        documents = []
        i = 0
        for line in lines:
            # str -> dict
            i += 1
            str_line = ast.literal_eval(line)
            document = []
            for word in str_line['sentences'].split():
                document.append(word)
            documents.append(document)
            if i == 3:
                break
        return documents