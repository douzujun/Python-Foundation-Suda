"""
字典 用户输入键 输出值
若键不存在，则输出您输入的键不存在
"""

dict1 = {}

if __name__ == "__main__":
    while True:
        try:
            key = input("请输入键：")
            if key in dict1:
                print("值为", dict1[key])
            else:
                value = input("您输入的键不存在，请输入该键要对应的值：")
                dict1[key] = value
        except:
            break