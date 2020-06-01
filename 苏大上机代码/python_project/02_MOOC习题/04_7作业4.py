"""
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词

"""

class Solution:
    line1 = set('qwertyuiop')
    line2 = set('asdfghjkl')
    line3 = set('zxcvbnm')
    def findWords(self, words: list) -> list:
        result_list = []
        for word in words:
            word_set = set(word.lower())
            if word_set < self.line1 or word_set < self.line2 or word_set < self.line3:
                result_list.append(word)
        return result_list

if __name__ == "__main__":
    word_list = input("请在一行输入所有单词，空格分开：").split()
    s1 = Solution()
    print(s1.findWords(word_list))
