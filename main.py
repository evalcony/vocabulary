import os
import random
import string

# 默认每次显示单词数量
default_num = 10

def split():
    lines = read_file('/words-repo/tofel-words.txt')

    # 排序
    lines.sort(key=str.lower)

    r = []
    cur_alpha = 'a'

    for l in lines:
        if l[0] != cur_alpha:
            if len(r) != 0:
                write_file('tofel/', cur_alpha+'.txt', r)
            cur_alpha = l[0]
            r = []
        r.append(l)
    cur_alpha = r[0][0]
    write_file('tofel/', cur_alpha+'.txt', r)
         

def read_file(filename):
    lines = []
    root_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(root_dir+filename):
        return []
    with open(root_dir+filename, 'r') as file:
        for line in file:
            lines.append(line.replace("\n",""))
    return lines

def write_file(prefix, finename, lines):
    print('写入文件:', finename)
    root_dir = os.path.dirname(os.path.abspath(__file__))
    path = root_dir+'/words-repo/split/'+prefix
    # 防止路径不存在
    if not os.path.exists(path):
        os.makedirs(path)
    dir_file_path = path + '/' + finename
    if not os.path.exists(dir_file_path):
        open(dir_file_path, 'w').close()
    with open(dir_file_path, 'w') as f:
        for m in lines:
            f.write(m+'\n')

"""获取1-26随机数,并转化为英文字母"""
def get_random_letter():
  # 生成1-26的随机整数
  rand_int = random.randint(1, 26)
  # 将随机整数转换为英文字母
  # 通过随机整数索引英文字母字符串,获取对应字母
  rand_letter = string.ascii_uppercase[rand_int-1]
  
  return rand_letter

def get_rand_word():
    filename = get_random_letter() + '.txt'
    lines = read_file('/words-repo/split/tofel/'+filename)
    if len(lines) == 0:
        print('')
        return
    cache = set()
    for i in range(default_num):
        idx = random.randint(1, len(lines))
        if idx in cache:
            i = i-1
            continue
        else:
            cache.add(idx)

        w = lines[idx-1]
        print(w)

if __name__ == '__main__':
    get_rand_word()
