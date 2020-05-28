"""
给定字符串J 代表石头中 宝石 的类型，和字符串 S代表你拥有的石头。 

S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的 石头 中有多少是 宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jewels-and-stones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for stone in S:
            if stone in J:
                count += 1
        return count

    def numJewelsInStones2(self, J: str, S: str) -> int:
        return len([ch for ch in S if ch in J])


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    s1 = Solution()
    print(s1.numJewelsInStones2(J, S))