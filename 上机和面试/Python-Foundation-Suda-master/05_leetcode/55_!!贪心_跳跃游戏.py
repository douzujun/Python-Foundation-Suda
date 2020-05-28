"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。
"""
class Solution:
    def canJump(self, nums: list) -> bool:
        # DFS 超时
        self.visited = [False] * len(nums)
        self.nums = nums
        return self.DFS(0)
        
    def DFS(self, start):
        self.visited[start] = True
        if start == len(self.nums) - 1:
            return True
        Neighbor = [start + i for i in range(1, self.nums[start] + 1) if 0 <= start + i < len(self.nums)]
        Neighbor.extend([start - i for i in range(1, self.nums[start] + 1) if 0 <= start - i < len(self.nums)])
        for nb in Neighbor:
            if not self.visited[nb]:
                if self.DFS(nb):
                    return True
        else:
            self.visited[start] = False
            return False

    def canJump2(self, nums:list) -> bool:
        """
        思路：尽可能到达最远位置（贪心）。 如果能到达某个位置，那一定能到达它前面的所有位置。
        方法：初始化最远位置为0，然后遍历数组，如果当前位置能到达，
        并且当前位置+跳数>最远位置，就更新最远位置。最后比较最远位置和数组长度。
        复杂度：时间复杂度O(n)，空间复杂度O(1)。
        作者：mo-lan-4
        """
        max_jump = 0    # 当前能到达的最远处
        for i, jump in enumerate(nums):
            if max_jump >= i and i + jump > max_jump:   
            # 如果当前位置是到达的，且当前位置可跳到更远的位置
                max_jump = i + jump
        return max_jump >= i
        

if __name__ == "__main__":
    test = [2, 3, 1, 1, 4]
    s = Solution()
    print(s.canJump2(test))