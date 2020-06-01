"""
如果单词列表（words）中的一个单词包含牌照（licensePlate）中所有的字母，
那么我们称之为完整词。在所有完整词中，最短的单词我们称之为 最短完整词。

单词在匹配牌照中的字母时 不区分大小写 ，比如牌照中的 "P" 依然可以匹配单词中的 "p" 字母。

我们保证 一定存在 一个最短完整词。当有多个单词都符合最短完整词的匹配条件时取单词列表中 最靠前 的一个。

牌照中可能包含 多个相同 的字符，比如说：对于牌照 "PP"，单词 "pair" 无法匹配，但是 "supper" 可以匹配。

"""

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list) -> str:
        # 80 ms  79.08%
        # plate_dict = {}
        # for ch in licensePlate:
        #     if ch.isalpha():
        #         t = ch.lower()
        #         plate_dict[t] = plate_dict.get(t, 0) + 1

        # 使用re和collections  76ms 85%
        import re
        import collections
        license_ = licensePlate.lower()                 #大写 -> 小写
        license = re.findall(r'[a-z]', license_)        #选取牌照中的字母
        plate_dict = collections.Counter(license)              #统计牌照中的字母个数
        
        complete_word = ''
        for word in words:
            for key, value in plate_dict.items():
                if word.lower().count(key) < value:
                    break   # 词不完整
            else:
                if not complete_word:
                    complete_word = word
                elif len(complete_word) > len(word):
                    complete_word = word
                
        return complete_word

    def shortestCompletingWord2(self, licensePlate: str, words: list) -> str:
        import re
        import collections
        license_ = licensePlate.lower()                 #大写 -> 小写
        license = re.findall(r'[a-z]', license_)        #选取牌照中的字母
        dic = collections.Counter(license)              #统计牌照中的字母个数
        words.sort(key=len)                             #words按单词长度排序
        for word in words:
            if collections.Counter(word) & dic == dic:
                return word
        return -1

if __name__ == "__main__":
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    s = Solution()
    print(s.shortestCompletingWord(licensePlate, words))