"""
小明将学生排队  学号小到大排一排  然后进行多次调整
一次调整可能让一名同学出队 向前或先后移动一段距离再入队

例： 学生人数8人
0）初始 1，2，3，4，5，6，7，8
1）第一次调整 3号向后移动2   1，2，4，5，3，6，7，8
"""


class Solution:
    def MovingResult(self, m, lst):
        """
        m: 学生的数量
        lst: 每一个元素是一个元组 元组的第一个元素是学号 第二个是移动的数量 负数表示向前
        返回一个列表 按照顺序存储了当前位置上学生的学号
        """
        result = [i+1 for i in range(m)]
        for order in lst:
            index = result.index(order[0])
            stu = result.pop(index)
            index += order[1]
            if 0 <= index < m:
                result.insert(index, stu)
            elif order[1] > 0:
                result.append(stu)
            elif order[1] < 0:
                result.insert(stu, 0)
        return result

if __name__ == "__main__":
    m = 8
    lst = [(3, 2), (8, -3), (3, -2)]
    s = Solution()
    print(s.MovingResult(m, lst))
