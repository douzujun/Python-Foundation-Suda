# -*- coding: utf-8 -*-

class Root:
    __total = 0
    def __init__(self, v):
        self.__value = v
        Root.__total += 1
        
    def show(self):
        print('self.__value:', self.__value)
        print('Root.__total:', self.__total)
        
    @classmethod
    def classShowTotal(cls): # 类方法
        print(cls.__total)
        
    @staticmethod
    def staticShowTotal():
        print(Root.__total)
    
t = Root(3)
t.classShowTotal()  # 通过对象来调用类方法

t.staticShowTotal()

t.show()



