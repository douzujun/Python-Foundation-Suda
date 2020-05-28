"""
实现PM2.5空气质量问题提醒程序，接收用户输入的PM2.5值，合法的值为0-500之间的整数，
如果PM2.5小于35，打印“空气质量优，建议户外运动”；
如果PM2.5的值在35到75之间（包括35），打印“空气质量良好，建议适度户外运动”；
如果PM2.5的值大于75（包括75），打印“空气污染，请小心！”

利用 异常处理 用户输入不合法的情况，当用户输入不合法时（输入非整数、输入0-500之外的数值）让用户重新输入。
"""


class IllegalInteger(BaseException):
    """
    自定义异常类 接收一个PM值
    """
    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num


def main():
    while True:
        # 异常发生时，输出异常信息后会重新进行输入
        try:
            PM = int(input("请输入当前的PM2.5值："))
            if not (0 < PM <= 500):
                # 触发自定义异常
                raise IllegalInteger(PM)
        except ValueError:
            print("请输入一个整数")
        except IllegalInteger as x:
            print('IllegalInteger:输入的PM值为{}不在0~500的范围'.format(x.num))
        else:
            # 未有异常发生则直接打印结果
            if PM < 35:
                print("空气质量优，建议户外运动")
            elif PM < 75:
                print("空气质量良好，建议适度户外运动")
            else:
                print("空气污染，请小心！")
            break


if __name__ == "__main__":
    main()
