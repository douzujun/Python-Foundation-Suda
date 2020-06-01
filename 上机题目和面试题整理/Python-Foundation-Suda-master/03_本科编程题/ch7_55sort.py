"""
55.【文件】当前路径下有文本文件 Numbers.txt，文件中的每一行都是一个浮
点数，编写程序读取出所有的浮点数。要求：
a) 从小到大排序，将排序后的结果写到当前路径下新生成的一个文本文件
Sort.txt 中，每个数占一行。
b) 求出这些数字的均值、方差，将结果写到当前路径下新生成的一个文本
文件 Sort.txt 中，每个数占一行。
c) 要求生成的文本文件 Sort.txt 中同时包含排序和均值、方差的结果。

"""
def read_num(filename="ch7_55_Numbers.txt"):
    f = open(filename, 'r')
    num_list = list(map(float, f.readlines()))
    return num_list


def sort_num(num_list: list):
    num_list.sort()

def comput_avg_cov(num_list):
    avg = sum(num_list)
    cov = sum([(num - avg)**2 for num in num_list])/len(num_list)
    return avg, cov

def save_result(filename="ch7_55_Sort.txt", **kwarg):
    f = open(filename, 'a+')
    for _, v in kwarg.items():
        if isinstance(v,list):
            for i in v:
                f.write(str(i)+'\n')
        else:
            f.write(str(v)+'\n')
    f.write('\n')

    f.close()


if __name__ == "__main__":
    num_list = read_num()

    sort_num(num_list)
    save_result(num_list=num_list)

    a,c = comput_avg_cov(num_list)
    print(a,c)
    save_result(avg=a, cov=c)