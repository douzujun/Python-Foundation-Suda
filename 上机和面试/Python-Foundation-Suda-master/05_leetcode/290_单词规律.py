"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， 
pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着 双向连接的对应规律。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # 32ms 88.48%
        str_sp = str.split(' ')
        if len(pattern) != len(str_sp):
            return False
        pattern_dict = {}
        for ch, word in zip(pattern, str_sp):
            if ch in pattern_dict:
                # 是否符合ch -> word映射
                if pattern_dict[ch] != word:
                    return False
            elif word in pattern_dict.values():
                # 已经有其他ch映射到word
                return False
            else:
                pattern_dict[ch] = word
        return True


if __name__ == "__main__":
    S = Solution()
    pattern = "abba"
    st = "dog cat cat dig"
    print(S.wordPattern(pattern, st))