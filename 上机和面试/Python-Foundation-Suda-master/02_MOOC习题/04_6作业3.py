"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，
同时仍保留空格和单词的初始顺序。

输入: "Let's take LeetCode contest"

输出: "s'teL ekat edoCteeL tsetnoc" 

注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        org_list = s.split()
        new_list = []
        for word in org_list:
            drow = ''.join(reversed(list(word)))
            new_list.append(drow)
        return new_list



if __name__ == "__main__":
    s1 = Solution()
    org_str = input("please input an english string:")
    print(s1.reverseWords(org_str))