"""
王老虎的朋友周大牛约王老虎下周一起去看展览，
但王老虎每周的1、3、5有课必须上课，
请帮王老虎判断他能否接受周大牛的邀请，
如果能返回True；如果不能则返回False,如果输入不合法返回None。
用数字1到7表示从星期一到星期日。
"""

class Solution:
    available = [1,3,5]
    def judge(self,  num: int):
        if num not in range(1,8):   # 判断是否在1~7 含头不含尾
            return "None"
        elif num in self.available:
            return "True"
        else:
            return "False"

if __name__ == "__main__":
    s1=Solution()
    while True:
        try:
            num=int(input("请输入一个整数"))
            print(s1.judge(num))
        except:
            break