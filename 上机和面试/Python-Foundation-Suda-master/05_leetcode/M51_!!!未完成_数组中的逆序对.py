"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。
"""


class Solution:
    def reversePairs(self, nums: list) -> int:
        if len(nums) <= 1:
            return 0

        nums_sorted = nums
        ans, size = 0, 2
        while size <= len(nums):
            

            for i in range(len(nums)//size):
                list1 = nums_sorted[i*size: i*size + size//2]
                list2 = nums_sorted[i*size + size//2: (i+1)*size]
                ans += self.merge(list1, list2, nums_sorted, i*size)
            size *= 2
        else:
            list1 = nums_sorted[0:size//2]
            list2 = nums_sorted[size//2:]
            ans += self.merge(list1,list2,nums_sorted,0)
        return ans

    def merge(self, list1, list2, nums_sorted, start):
        # 合并且清点逆序
        index1, index2 = 0, 0
        count = 0
        temp = 1
        while index1 < len(list1) and index2 < len(list2):
            if list1[index1] > list2[index2]:
                nums_sorted[start] = list2[index2]
                index2 += 1
                count = count*temp + 1
                temp = 1
            elif list1[index1] <= list2[index2]:
                nums_sorted[start] = list1[index1]
                index1 += 1
                if index1 < len(list1) and list1[index1]>list2[index2]:
                    temp += 1
            start += 1
        else:
            if index1 < len(list1):
                count += len(list2)* (len(list1)-index1 -1)

            while index1 < len(list1):
                nums_sorted[start] = list1[index1]
                index1 += 1
                start += 1
            while index2 < len(list2):
                nums_sorted[start] = list2[index2]
                index2 += 1
                start += 1
        print(list1, list2, count)
        return count

    def reversePairs2(self, nums: list) -> int:
        # !!!
        n = len(nums)
        if n <= 1:
            return 0
        mid = n // 2
        left = nums[:mid]
        right = nums[mid:]
        result = self.reversePairs(left) + self.reversePairs(right)
        
        # union left and right
        left.sort()
        right.sort()
        index = 0
        for j in range(len(right)):
            while index < len(left) and left[index] <= right[j]:
                index += 1
            else:
                result += (len(left) - index)
        return result



if __name__ == "__main__":
    # test = [4,5,2,3]
    test = [233,2000000001,234,2000000006,235,2000000003,236,2000000007,237,2000000002,2000000005,233,233,233,233,233,2000000004]
    s = Solution()
    print(s.reversePairs(test))
    print(test)
    # mer_list = [0] * 4
    # print(s.merge([6,7], [4,5], mer_list, 0))
    # print(mer_list)
