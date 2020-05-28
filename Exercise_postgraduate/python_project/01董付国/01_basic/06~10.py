def func6():
    num = int(input('输入一个三位数整数:'))
    sum = 0
    while num != 0:
        num, mod = divmod(num, 10)
        sum += mod
    print(sum)

def func7():
    x1,y1,x2,y2,x3,y3 = eval(input("x1,y1,x2,y2,x3,y3:"))
    def dis(x1,y1,x2,y2):
        return ((x1-x2)**2+(y1-y2)**2)**0.5

    side1 = dis(x1,y1,x2,y2)
    side2 = dis(x1,y1,x3,y3)
    side3 = dis(x3,y3,x2,y2)
    s = sum((side1,side2,side3))/2
    area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
    print(area)

if __name__ == "__main__":
    # func6()
    func7()
    pass