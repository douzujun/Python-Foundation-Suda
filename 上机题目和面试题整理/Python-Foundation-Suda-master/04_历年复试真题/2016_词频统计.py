r"""
2016
要求：
文本文件 input.txt 由若干英文单词和分隔符(空格，回车，换行)构成. 根据如下说明编写程序统计不同单词出现
的次数(频度). 将统计结果按出现频度从高到低排序，并将出现频度大于 5 的单词及其频度输出到文件 output.txt
中. 文件格式如下所示：
WinEdt, 31
1. 多个连续的分隔符被视为一个分隔符
2. 单词大小写敏感
3. 每个单词的长度不超过20个字符
4. 单词的数量未知
"""


def read_str(filename="2016_input.txt"):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    content = ' '.join(lines)   # 连接不同行
    return content

def count_word(content):
    # 字典实现
    freq_dict = {}
    str_list = content.split()
    for word in str_list:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    # 集合实现
    # word_set = list(set(content))
    # count = []
    # for word in word_set:
    #     count.append(content.count(word))
    # word_count_list = list(zip(word_set, count))
    # word_count_list.sort(key = lambda x : x[1], reverse = True)

    return freq_dict

def output_file(freq:dict, filename="2016_output.txt"):
    f = open(filename, 'w')
    word_list = list(filter(lambda x: True if freq[x]>5 else False, freq.keys()))
    word_list.sort(key=lambda x:freq[x], reverse=True)  # 频度从大到小排序
    for word in word_list:
        f.write('{0},{1}\n'.format(word, freq[word]))
    f.close()

if __name__ == "__main__":
    content = read_str()
    freq_dict = count_word(content)
    output_file(freq_dict)
    