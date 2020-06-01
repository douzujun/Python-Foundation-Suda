"""
如果一个数值字符串顺读和倒读完全一样，称该字符串是回文字
符串，比如’12321’和’1331’都是回文字符串，’123’则不是。编写
一个函数使用递归来判断一个数值字符串是否是回文
"""

def judge_string(ju_str):
    if len(ju_str) == 1:
        return True
    else:
        if ju_str[0] != ju_str[-1]:
            return False
        else:
            return judge_string(ju_str[1:-1])
        
if __name__ == "__main__":
    s = input()
    print(judge_string(s))