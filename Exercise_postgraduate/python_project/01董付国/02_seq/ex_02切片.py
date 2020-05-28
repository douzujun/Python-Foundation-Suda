"""
用户输入一个列表和2个整数作为下标
然后输出列表中介于2个下标之间的元素组成的子列表

"""

num_list = eval(input("输入[1,2,3,4,5]形式的列表:"))
start, end = map(int, input("输入空格分开的两个整数：").split())
print(num_list[start:end+1])