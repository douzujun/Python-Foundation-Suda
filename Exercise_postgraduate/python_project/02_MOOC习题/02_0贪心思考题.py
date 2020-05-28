# 奶茶店促销
# 10元一杯 3杯送1或5杯送2
# 小强带了N元钱（N>=0)
# 请问小强最多可以买多少杯

# 3送1 3/4*10一杯 5送2 5/7*10 优先5送2

if __name__ == "__main__":
    n = int(input("小强有多少钱："))
    num = n // 10   # 原价能购买的杯数
    total = num
    if num // 5:
        total += num//5 *2
        num = num % 5
    if num // 3:
        total += num//3
    print("小明最多可以买{}杯奶茶".format(total))
