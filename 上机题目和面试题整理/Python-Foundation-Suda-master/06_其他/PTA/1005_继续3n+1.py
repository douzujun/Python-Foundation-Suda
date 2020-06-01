"""
对任何一个正整数 n，如果它是偶数，那么把它砍掉一半；
如果它是奇数，那么把 (3n+1) 砍掉一半。
这样一直反复砍下去，最后一定在某一步得到 n=1。

验证卡拉兹猜想的时候，为了避免重复计算，可以记录下递推过程中遇到的每一个数。
例如对 n=3 进行验证的时候，我们需要计算 3、5、8、4、2、1，
则当我们对 n=5、8、4、2 进行验证的时候，就可以直接判定卡拉兹猜想的真伪，
我们称 5、8、4、2 是被 3“覆盖”的数。
我们称一个数列中的某个数 n 为“关键数”，如果 n 不能被数列中的其他数字所覆盖。

现在给定一系列待验证的数字，我们只需要验证其中的几个关键数，
就可以不必再重复验证余下的数字。你的任务就是找出这些关键数字，
并按从大到小的顺序输出它们。

输入：
第 1 行给出一个正整数 K (<100)，
第 2 行给出 K 个互不相同的待验证的正整数 n (1<n≤100)的值，
数字间用空格隔开。
输出：
每个测试用例的输出占一行，按从大到小的顺序输出关键数字。
数字间用 1 个空格隔开，但一行中最后一个数字后没有空格。
"""

def keynum(num_list):
    key_dict = {i:True for i in num_list}
    for num in num_list:
        # 有可能成为keynum
        if not key_dict[num]:
            continue
        while num != 1:
            if num%2 == 0:
                num //= 2
            else:
                num = (3*num +1 )//2
            
            if num in key_dict:
                key_dict[num] = False
    return sorted(filter(lambda x: key_dict[x], key_dict), reverse=True)

def print_list(num_list):
    for num in num_list[:-1]:
        print(num, end=' ')
    if len(num_list):
        print(num_list[-1])


if __name__ == "__main__":
    while True:
        try:
            input()
            num_list = list(map(int, input().split()))
            num_list = keynum(num_list)
            print_list(num_list)
        except:
            break