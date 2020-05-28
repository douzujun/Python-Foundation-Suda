# -*- coding: utf-8 -*-

# 数组类，支持数组与数字之间的四则运算
# 数组之间的 加法运算，内积运算和大小比较
# 数组元素访问和修改 
# 成员测试
class MyArray:
    __value = []
    __size = 0
    
    # 判断是否是数字
    def __IsNumber(self, n):
        if (not isinstance(n, int)) and \
           (not isinstance(n, float)) and \
           (not isinstance(n, complex)):
               return False
        else:
            return True
          
    # 初始化
    def __init__(self, *args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__IsNumber(arg):
                    print('All elements must be numbers')
                    return
            self.__value = list(args)
        
    # 数组中每个元素都与数字n相加，或两个数组相加
    def __add__(self, n):
        if self.__IsNumber(n):
            b = MyArray()
            for v in self.__value:
                b.__value.append(v + n)
            return b
        elif isinstance(n, MyArray):
            if len(n.__value) == len(self.__value):
                c = MyArray()
                for i, j in zip(self.__value, n.__value):
                    c.__value.append(i + j)
                return c
            else:
                print('Length not equal')
        else:
            print('Not supported')
            
    # 数组中每个元素都与数字n相减，返回新数组
    def __sub__(self, n):
        if not self.__IsNumber(n):
            print("not number")
            return
        b = MyArray()
        for v in self.__value:
            b.__value.append(v - n)
        return b
    
    # 数组中每个元素都与数字n相乘
    def __mul__(self, n):
        if not self.__IsNumber(n):
            print("not number")
            return 
        b = MyArray()
        for v in self.__value:
            b.__value.append(v * n)
        return b
    
    # 数组中每个元素都与数字n相除，返回新数组
    def __truediv__(self, n):
        if not self.__IsNumber(n):
            print("Not number")
            return
        b = MyArray()
        for v in self.__value:
            b.__value.append(v / n)
        return b
    
    # 整除
    def __floordiv__(self, n):
        if not self.__IsNumber(n):
            print("Not number")
            return
        b = MyArray()
        for v in self.__value:
            b.__value.append(v // n)
        return b
        
    # 取余
    def __mod__(self, n):
        if not self.__IsNumber(n):
            print("Not number")
            return
        b = MyArray()
        for v in self.__value:
            b.__value.append(v % n)
        return b
    
    # 求长度
    def __len__(self):
        return len(self.__value)
    
    # 追加元素
    def append(self, v):
        if not self.__IsNumber(v):
            print("Not number")
            return
        self.__value.append(v)
        
    # 获取指引位置的元素值
    def __getitem__(self, index):
        if self.__IsNumber(index) and 0 <= index < len(self.__value):
            return self.__value[index]
        else:
            print("Index out of range.")
        
    # 设置指定位置的元素值
    def __setitem__(self, index, v):
        if not self.__IsNumber(v):
            print(v, ' is not a number')
        elif (not isinstance(index, int)) or index < 0 or index >= len(self.__value):
            print("Index type error or out of range")
        else:
            self.__value[index] = v
            
    # ==
    def __eq__(self, v):
        if not isinstance(v, MyArray):
            print(v, ' must be an instance of MyArray.')
            return False
        if self.__value == v.__value:
            return True
        return False
    
    # <
    def __lt__(self, v):
        if not isinstance(v, MyArray):
            print(v, ' must be an instance of MyArray.')
            return False
        if self.__value < v.__value:
            return True
        return False
    
    # 直接使用对象作为语句时调用该函数
    def __repr__(self):
        return repr(self.__value)
    
    # print()函数输出对象时，调用该函数
    def __str__(self):
        return str(self.__value)
    
if __name__=='__main__':
    x = MyArray(1,2,3,4,5,6)
    y = MyArray(6,5,4,3,2,1)
    print(x + 1)
    print(x + y)
    print(x - 5)
    
    print(x * 3)
    
    x.append(7)
    print(x)
    
    x[1] = 999
    print(x[1])
    print(x)

    print(x // 2)       
    
    print(x < y)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
                
    