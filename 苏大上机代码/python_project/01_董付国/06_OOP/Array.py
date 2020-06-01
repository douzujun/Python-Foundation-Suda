

class ArrayType:
    """数组中的所有元素必须是数字"""

    @staticmethod
    def __is_number(n):
        if (not isinstance(n, int)) and \
                (not isinstance(n, float)) and \
                (not isinstance(n, complex)):
            return False
        else:
            return True

    def __init__(self, *args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__is_number(arg):
                    print("所有元素必须是数字。")
                    return
            self.__value = list(args)

    def __add__(self, n):
        """
        :param n: number or ArrayType
        :return: ArrayType add n or ArrayType andd ArrayType
        """
        if self.__is_number(n):
            rt = ArrayType()    # 创建一个新的Array类 用于返回
            for v in self.__value:
                rt.__value.append(v+n)  # 成员函数可以访问私有数据成员
            return rt
        elif isinstance(n, ArrayType):
            if len(self) == len(n):
                rt = ArrayType()
                # for v1, v2 in self.__value, n.__value:
                for v1, v2 in zip(self.__value, n.__value):
                    rt.__value.append(v1+v2)
                return rt
            else:
                print("ArrayType仅长度相等才可相加")
                return
        else:
            print("仅支持ArrayType及数字。")
            return

    def __sub__(self, other):
        if self.__is_number(other):
            rt = ArrayType()
            for v in self.__value:
                rt.__value.append(v+other)
            return rt
        elif isinstance(other, ArrayType):
            if len(self) == len(other):
                rt = ArrayType()
                for v1, v2 in zip(self.__value, other.__value):
                    rt.__value.append(v1 - v2)
                return rt
            else:
                print("ArrayType仅长度相等才可相减")
                return
        else:
            print("仅支持ArrayType及数字。")
            return

    def __len__(self):
        return len(self.__value)

    def __str__(self):
        return str(self.__value)