# 捕获所有异常
k = 0
while k < 3:
    try:
        x = int(input('please input first interger:'))
        y = int(input('please input second interger:'))
        print('x/y', x/y)
    except Exception as e:
    # except :
        print('InputError')
    else:
        print('no error!')
    finally:
        print('')
    k += 1

