"""
当前路径下有一个文本文件Names.txt
包含了按照字典排序的名字
编写一个程序，当用户自己给定一个名字，
按照字典序将其插入到正确的位置
如果这个名字已经存在于文件中，则不要插入。

难点：文件的插入
"""

def read_names(filename="ch7_58_Names.txt"):
    f = open(filename, 'r')
    name_list = list(map(lambda x: x.strip(),f.readlines()))
    f.close()
    return name_list

def insert_name(name_list:list, newname):
    i = 0
    for name in name_list:
        if name < newname:
            i += 1
            continue
        elif name == newname:
            return
        else:
            break
    name_list.insert(i, newname)

def write_names(name_list, filename="ch7_58_new_word.txt"):
    f = open(filename, 'w')
    for name in name_list:
        f.write(name+'\n')
    f.close()

if __name__ == "__main__":
    name_list = read_names()
    print(name_list)
    newname = input("please input a new name:")
    insert_name(name_list, newname)
    print(name_list)
    write_names(name_list)