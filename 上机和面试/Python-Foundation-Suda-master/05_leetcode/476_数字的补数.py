"""
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

"""
class Solution:
    def findComplement(self, num: int) -> int:
        # 48ms 23% 字符串方式处理
        num_str = bin(num)
        result = ['0','b']
        for ch in num_str[2:]:
            if ch == '0':
                result.append('1')
            else:
                result.append('0')
        return int(''.join(result), 2)

    def findComplement2(self, num: int) -> int:
        # 40ms 48% 数学计算 num和补数相加 1111111
        return 2**(len(bin(num))-2)-num-1




if __name__ == "__main__":
    s = Solution()
    print(s.findComplement3(5))