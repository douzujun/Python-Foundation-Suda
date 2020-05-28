import re

# 匹配长度5~20的字符串，以字母开头能带下划线和句点 第二个字符必须是.
pattern1 = '^[a-zA-Z]{1}\.([a-zA-Z0-9._]){4,18}$'
r1 = re.compile(pattern1)

pattern2 = r'^[a-zA-Z]{1}\.([a-zA-Z0-9._]){4,18}$'
r2 = re.compile(pattern2)

while True:
    try:
        st = input("input a string ")
        if r1.match(st):
            print("r1 match")
        else:
            print("r1 dismatch")
        if r2.match(st):
            print("r2 match")
        else:
            print("r2 dismatch")
    except:
        break