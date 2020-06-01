# 求x与y的最大公约数 使用assert 语句来约束x、y取值大于1的正整数


while True:
    try:
        x = int(input('input x :'))
        y = int(input('input y :'))
        assert x > 1 and y > 1, 'x与y的取值必须大于1'   # 断言
        a = x
        b = y
        if a < b:
            a,b = b,a
        while b!=0:
            temp = a%b
            a=b
            b=temp
        else:
            print('%s和%s的最大公约数为:%s'%(x,y,a))
            break
    except Exception as e:
        print('捕捉到异常:\n',e)