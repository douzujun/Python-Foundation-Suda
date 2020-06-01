"""
集合 S 包含从1到 n 的整数。
不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，
导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。
你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-mismatch
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 288ms 39%  使用数组标记每个数字是否访问到
        flag = [False]*len(nums)
        ans = [0, 0]
        for num in nums:
            if flag[num-1]:
                ans[0] = num
            else:
                flag[num-1] = True
        ans[1] = flag.index(False)+1
        return ans




if __name__ == "__main__":
    S = Solution()
    nums = [1,2,2,4]
    print(S.findErrorNums(nums))