"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 44ms 51%
        if len(strs) == 0:
            return ""
        length = 0
        pub = []
        while length < len(strs[0]):
            pub.append(strs[0][length])
            for word in strs[1:]:
                if length<len(word) and word[length] == pub[length]:
                    continue
                else:
                    pub.pop()
                    return ''.join(pub)
            length += 1
        return ''.join(pub)

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        # 28ms 98%
        if len(strs) == 0:
            return ''
        s = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(s) != 0 :
                s = s[:-1]
        return s

                    


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix2(["flower","flow","flight"]))