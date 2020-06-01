# a simple exception program

k = 0
while k < 3:
    try:
        x = int(input('please input first interger:'))
        y = int(input('please input second interger:'))
        print('x/y', x/y)
    # except ValueError:
    #     print('please input a interger! ')
    # except ZeroDivisionError:
    #     print('Division can\'t be zero!')
    except(ValueError, ZeroDivisionError)as e:
        print('please input a none-zero interger! ', e)
    else:
        print('no error!')
    finally:
        print('')
    k += 1





'''
    输入非整数会有 ValueError
    输入0会有 ZeroDivisionError
    
'''