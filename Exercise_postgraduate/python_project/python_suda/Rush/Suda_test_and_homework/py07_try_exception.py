# 实现PM2.5空气质量问题提醒程序，接收用户输入的PM2.5值，合法的值为0-500之间的整数，
# 如果PM2.5小于35，打印“空气质量优，建议户外运动”；
# 如果PM2.5的值在35到75之间（包括35）打印“空气质量良好，建议适度户外运动”；
# 如果PM2.5的值大于75（包括75），打印“空气污染，请小心！”
# 利用异常处理用户输入不合法的情况，当用户输入不合法时（输入非整数、输入0-500之外的数值）让用户重新输入。

class IllegalInteger(Exception):
    """
    自定义异常类
    """
    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num 

def main():
    while True:
        try:
            PM = int(input('input PM2.5: '))
            if not (0 < PM <= 500):
                raise IllegalInteger(PM)        
        except ValueError:
            print("请输入一个整数")
        except IllegalInteger as x:
            print('PM:{0} 不在0-500之间'.format(x.num))
        else:
            if PM < 35:
                print("优良")
            elif PM < 75:
                print('良好')
            else:
                print('差劲')
            break
if __name__ == "__main__":
    main()