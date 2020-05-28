# 自定义异常类


class StrExcept (Exception):    # 对应字符串输入错误
    pass


class MathExcept (Exception):   # 对应数值输入异常
    pass


while True:
    try:
        x = input('please input your name(2-20 character):')
        if len(x) < 2 or len(x) > 20:
            raise StrExcept
        y = int(input('please input your age( 18-60 ):'))
        if y < 18 or y > 60:
            raise MathExcept
        z = int(input('please input your salary for month( >800):'))
        if z < 800:
            raise MathExcept
        print('姓名:', x)
        print('年龄:', y)
        print('年收入:', z*12)
        break
    except StrExcept:
        print('name error')
    except MathExcept:
        print('number error')
    except Exception as e:
        print('input error', e)





