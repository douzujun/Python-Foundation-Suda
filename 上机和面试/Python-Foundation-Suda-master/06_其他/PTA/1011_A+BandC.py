"""
给定[-2^31,2^31]内的三个整数，A、B、C判断A+B是否大于C
4
1 2 3
2 3 4
2147483647 0 2147483646
0 -2147483648 -2147483647

Case #1: false
Case #2: true
Case #3: true
Case #4: false

"""

if __name__ == "__main__":
    T = int(input())
    case_list = []
    for i in range(T):
        case_list.append(tuple(map(int, input().split())))
    temp = 1
    for case in case_list:
        result = 'Case #'+str(temp)+': '
        result += 'true' if case[0]+case[1]>case[2] else 'false'
        print(result)
        temp += 1