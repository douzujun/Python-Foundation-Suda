# 对下列文字进行词频统计，再按照词频和字典顺序排序
# 词频主关键字 字典顺序是次关键字 字典顺序不考虑大小写
string = """
Python includes two operations for sorting.
The method sort() in the built-in list data type
rearranges the items in the underlying list into
ascending order, much like merge.sort(). In contrast,
the built-in function sorted() leaves the underlying
list alone; instead, it returns a new list containing
the items in ascending order.
"""
# string = string.replace('\n', ' ')    # 一次只能转换一个
# 生成翻译表
trans_table = ''.maketrans('.,\n()', '     ')
string = string.translate(trans_table)
str_list = string.split()

str_dict = dict()
for word in str_list:
    str_dict[word] = str_dict.get(word, 0) + 1

# print(str_dict)
str_list = sorted(str_dict, key=lambda s: s.lower())
str_list.sort(key=lambda s: str_dict[s], reverse=True)

i = 0
for word in str_list:
    print('%s:%d\t'%(word, str_dict[word]), end='')
    i += 1
    if i % 5 == 0:
        print('')
