"""
运行用户输入4位整数作为年份，判断其是否为闰年。
被400整除是，能被4整除却不能被100整除是
"""


def judge(year):
    if year%4 == 0:
        if year % 100==0 and year % 400!=0:
            return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    year = int(input("请输入一个年份:"))
    print(judge(year))
