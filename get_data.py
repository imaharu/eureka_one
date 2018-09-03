import subprocess
def get_simple_data(file_path):
    with open('utf8_delete_over50.txt', 'r') as f:
        with open(file_path) as lines:
            infos = []
            for line in lines:
                cols  = line.split(',')
                info = {
                    'title' :  cols[1], # タイトル
                    'company' : cols[33] # 出版社
                }
                cmd = "cat utf8_delete_over50.txt | grep %s" % cols[55]
                try:
                    res = subprocess.check_output(cmd, shell=True).decode('utf8')
                except:
                    print("Error.")
                print(res)
                break

def reconfigure_separte_to_oneLine(num):
    return num

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