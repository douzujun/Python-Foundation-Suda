"""
给定两个字符串，你需要从这两个字符串中找出 最长的特殊序列 。

最长特殊序列定义如下：该序列 为 某字符串独有 的 最长子序列 （即不能是其他字符串的子序列）。

子序列 可以通过 删去字符串中的某些 字符 实现，但不能改变剩余字符的 相对顺序。

空序列 为所有 字符串的子序列，任何字符串为其自身的子序列。

输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。

"""
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        if n != m:
            return max(m, n)
        elif a == b:
            return -1
        else:
            return n



if __name__ == "__main__":
    s = Solution()
    a = 'abcd'
    b = 'bcd'
    print(s.findLUSlength(a, b))