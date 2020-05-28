"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 60ms
        temp = x ^ y # 异或
        bin_str = bin(temp)
        return bin_str.count('1')

    def hammingDistance2(self, x: int, y: int) -> int:
        # 44ms
        o = x ^ y # 异或
        count = 0
        while o != 0:
            o, mod = divmod(o, 2)
            if mod:
                count += 1
        return count

    def hammingDistance3(self, x: int, y: int) -> int:
        # 28ms 在取异或的过程中计算
        num = 0
        res = []
        while x != 0 or y != 0:
            res.append((x%2, y%2))
            x //= 2
            y //= 2
        for xii, yii in res:
            if xii != yii:
                num += 1 
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.hammingDistance2(123, 234))