"""
某种外星语也使用英文小写字母，但可能顺序 order 不同。
字母表的顺序（order）是一些小写字母的排列。

给定一组用外星语书写的单词 words，以及其字母表的顺序 order，
只有当给定的单词在这种外星语中按字典序排列时，
返回 true；否则，返回 false。
"""

class Solution:
    def isAlienSorted(self, words: list, order: str) -> bool:
        # 52ms  45.43%
        ch_dict = {ch: index for index, ch in enumerate(order)}
        if len(words) <= 1:
            return True
        else:
            i = 0
            while i < len(words) - 1:
                w1, w2 = words[i], words[i+1]
                for j in range(min(len(w1),len(w2))):
                    if w1[j] == w2[j]:
                        # 字符相同比较w1 w2下一位
                        continue
                    elif ch_dict[w1[j]] > ch_dict[w2[j]]:
                        # 不符合字典序
                        return False
                    else:
                        # 字符不同 但符合字典序
                        break
                else:
                    if len(w1) > len(w2):
                    # 长度重合部分完全一致 长的在前不符合字典序
                        return False
                i += 1
            else:
                # 两两比较皆符合条件
                return True

    def isAlienSorted2(self, words: list, order: str) -> bool:
        # 40ms 84.69%  优化了结构 关于word长度小于1 用range即可
        ch_dict = {ch: index for index, ch in enumerate(order)}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            for j in range(min(len(w1),len(w2))):
                if w1[j] != w2[j]:
                    if ch_dict[w1[j]] > ch_dict[w2[j]]:
                        # 不符合字典序
                        return False
                    # 字符不同 但符合字典序
                    break
            else:
                if len(w1) > len(w2):
                # 长度重合部分完全一致 长的在前不符合字典序
                    return False
            i += 1

        return True
                        

if __name__ == "__main__":
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    s = Solution()
    print(s.isAlienSorted2(words, order))