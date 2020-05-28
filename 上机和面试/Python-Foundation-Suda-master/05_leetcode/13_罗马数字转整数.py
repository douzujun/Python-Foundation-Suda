"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
数字        数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。
12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中 小的数字在大的数字 的右边。但也存在特例，
例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        # 64ms 48% 遍历字符串
        switch = {'I':1, 'V':5, 'X': 10,'L':50, 'C':100,'D':500, 'M':1000}
        ans, index = 0, 0
        while index < len(s):
            if s[index] not in ('I', 'X', 'C') or index == len(s)-1:
                ans += switch[s[index]]
            elif switch[s[index]] < switch[s[index+1]]:
                # 当前的是IXC 且其后的字符比他大
                    ans += switch[s[index+1]] - switch[s[index]]
                    index += 1
            else:
                # 不是特殊情况
                ans += switch[s[index]]
            index += 1
        return ans

    def romanToInt2(self, s: str) -> int:
        # 68ms
        # 切片的话可以不担心 切片索引不存在 此时会返回存在的部分
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))

    def romanToInt3(self, s: str) -> int:
        # 56ms 72%
        # 不需2一起处理 后方大则减去当前部分
        Roman2Int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Int = 0

        for index in range(len(s) - 1):
            if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
                Int -= Roman2Int[s[index]]
            else:
                Int += Roman2Int[s[index]]

        return Int + Roman2Int[s[-1]]


if __name__ == "__main__":
    test = "MCMXCIX"
    s = Solution()
    print(s.romanToInt(test))