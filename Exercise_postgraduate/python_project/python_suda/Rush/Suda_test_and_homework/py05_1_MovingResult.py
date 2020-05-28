"""
小明将学生排队  学号小到大排一排  然后进行多次调整     
一次调整可能让一名同学出队 向前或先后移动一段距离再入队

例： 学生人数8人
0）初始 1，2，3，4，5，6，7，8
1）第一次调整 3号向后移动2   1，2，4，5，3，6，7，8
"""
class Solution():
    def MovingResult(self, m, lst):
        """
        m: 学生的数量
        lst: 每一个元素是一个元组 元组的第一个元素是学号 第二个是移动的数量 负数表示向前
        返回一个列表 按照顺序存储了当前位置上学生的学号
        """
        nums = [i for i in range(1, m+1)]
        nlen = len(lst)
        for i in range(nlen):
            op = lst[i]
            t = op[0]
            idx = nums.index(op[0])
            if op[1] > 0:
                for j in range(idx+1, idx + op[1]+1):
                    # print('nums[j] -> nums[j-1]', nums[j], nums[j-1])
                    nums[j-1] = nums[j]
            else:
                for j in range(idx-1, idx+op[1]-2, -1):
                    # print('nums[j] -> nums[j+1]', nums[j], nums[j+1])
                    nums[j+1] = nums[j]
           
            nums[idx + op[1]] = t 
            # print('nums:', nums)
        return nums

    def MovingResult2(self, m, lst):
        res = [i+1 for i in range(m)]
        for order in lst:
            index = res.index(order[0])
            stu = res.pop(index)
            index += order[1]
            if 0 <= index < m:
                res.insert(index, stu)
            elif order[1] > 0:
                res.append(stu)
            elif order[1] < 0:
                res.insert(0, stu)
        return res 
s = Solution()
print(s.MovingResult(m = 8, lst = [(3, 2), (8, -3), (3, -2)]))
print(s.MovingResult2(m = 8, lst = [(3, 2), (8, -3), (3, -2)]))