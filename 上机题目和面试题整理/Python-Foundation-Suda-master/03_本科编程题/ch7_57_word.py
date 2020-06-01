"""
当前路径下有文本文件 word.txt 中包含了 20 个英文单词，编写一
个程序，删除文件中所有不以元音开头的单词。结果保存在当前路径下新生
成的 new_word.txt 中。
"""

target = 'aeiouAEIOU'

if __name__ == "__main__":
    f = open('ch7_57_word.txt', 'r')
    word_list = f.read().split()
    f.close()

    for word in word_list[::]:
        if word[0] not in target:
            word_list.remove(word)
    
    f = open('ch7_57_newword.txt', 'w')
    for word in word_list:
        f.write(word+'\n')
    f.close()