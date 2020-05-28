# -*- coding: utf-8 -*-

# 字母表中字幕出现的次数 >= 单词的字幕出现次数
def contains(charCount, wordCount):
    print(charCount, wordCount)
    for key in wordCount.keys():
        print(charCount.get(key, 0) , wordCount.get(key))
        if charCount.get(key, 0) < wordCount.get(key):
            return False
    return True

def solve(words, chars):
    from collections import Counter
    charCount = dict(Counter(chars))
    res = 0
    wlen = len(words)
    for i in range(0, wlen):
        wordCount = dict(Counter(words[i]))
        if contains(charCount, wordCount):
            res += 1
    return res


print(solve(['cat', 'bt', 'hat', 'tree'], 'atach'))
print(solve(['hello', 'world', 'soochow'], 'welldonehoneyr'))