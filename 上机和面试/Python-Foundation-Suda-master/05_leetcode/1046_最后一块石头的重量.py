"""
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块最重的石头，然后将它们一起粉碎。
假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被 完全粉碎；
如果 x != y，那么重量为 x 的石头将会 完全粉碎 ，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/last-stone-weight
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            y = stones.pop(0)
            x = stones.pop(0)
            if x == y:
                continue
            else:
                stones.append(y-x)
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0


if __name__ == '__main__':
    stones = [1, 425, 63, 4, 13]
    s1 = Solution()
    print(s1.lastStoneWeight(stones))
