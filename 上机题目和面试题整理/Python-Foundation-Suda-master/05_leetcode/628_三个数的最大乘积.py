"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

"""
class Solution:
    def maximumProduct(self, nums: list) -> int:
        # 392ms  33.44%
        # 找到最大的3个和最小的四个数后暴力枚举
        from itertools import permutations as pr
        max_three, min_four = [], []
        target = []
        if len(nums) > 7:
            for num in nums:
                max_three.append(num)
                min_four.append(num)
                max_three.sort(reverse=True)
                min_four.sort()
                if len(max_three) > 3:
                    max_three.pop()
                if len(min_four) > 4:
                    min_four.pop()
            target.extend(max_three)
            target.extend(min_four)
        else:
            target = nums

        print(target)
        ans_max = target[0] * target[1] * target[2]
        for couple in pr(target, 3):
            # print(couple)
            temp = couple[0]*couple[1]*couple[2]
            ans_max = max(temp, ans_max)
        return ans_max
                
    def maximumProduct2(self, nums):
        # 324ms 66%
        # 排序后考虑3大 2大1小
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])


if __name__ == "__main__":
    test = [1,2,-3,4]
    s= Solution()
    print(s.maximumProduct(test))