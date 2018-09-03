def get_simple_data(file_path):
    with open(file_path) as lines:
        infos = []
        for line in lines:
            cols  = line.split(',')
            info = {
                'title' :  cols[1], # タイトル
                'company' : cols[33] # 出版社
            }
            infos.append(info)
            print(infos)
            break

def show_data_label():
    with open('aozora_word_list_utf8.csv') as lines:
        for line in lines:
            line_split = line.split(',')
            for i, name in enumerate(line_split):
                print(i, name)
            break

def delete_text_line_count():
    with open('utf8_delete_text.txt', 'w') as f:
        with open('utf8_all.csv') as lines:
            for line in lines:
                cols  = line.split(',')
                if int(cols[1]) <= 100:
                        print("line", line)
                        f.write(line)

delete_text_line_count()