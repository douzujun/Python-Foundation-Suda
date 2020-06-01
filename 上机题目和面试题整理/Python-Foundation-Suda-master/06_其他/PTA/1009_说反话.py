"""
给定一句英语，编写程序，将句中的所有单词颠倒输出。

测试输入包含一个测试用例，在一行内给出总长度不超过 80 的字符串。
字符串由若干单词和若干空格组成，其中单词是由英文字母（大小写有区分）组成的字符串，
单词之间用 1 个空格分开，输入保证句子末尾没有多余的空格。
"""

if __name__ == "__main__":
    while True:
        try:
            eng_str = input()
            word_list = eng_str.split()
            # drow_tsil = list(map(lambda word: ''.join(reversed(word)),word_list))
            word_list.reverse()
            print(' '.join(word_list))
        except:
            break