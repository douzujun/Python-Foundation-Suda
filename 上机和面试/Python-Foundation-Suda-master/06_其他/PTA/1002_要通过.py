"""
读入的字符串满足下列条件，系统就输出“答案正确”，否则输出“答案错误”

1. 字符串中必须仅有 P、 A、 T这三种字符，不可以包含其它字符；

2. 任意形如 xPATx 的字符串都可以获得“答案正确”，
其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；

3. 如果 aPbTc 是正确的，那么 aPbATca 也是正确的，
其中 a、 b、 c 均或者是空字符串，或者是仅由字母 A 组成的字符串。

输入格式：
每个测试输入包含 1 个测试用例。
第 1 行给出一个正整数 n (<10)，是需要检测的字符串个数。
接下来每个字符串占一行，字符串长度不超过 100，且不包含空格。
输出：
每个字符串的检测结果占一行，如果该字符串可以获得“答案正确”，则输出 YES，否则输出 NO。
"""
# PA判断s


def check_pat(pat_list):
    result_list = []
    for pat in pat_list:
        status = 0
        a1 = a2 = a3 = 0
        for ch in pat:
            if status == 0:
                if ch == 'A':
                    a1 += 1
                elif ch == 'P':
                    status = 1
                else:
                    result_list.append('NO')
                    break
            elif status == 1:
                if ch == 'A':
                    a2 += 1
                elif ch == 'T':
                    status = 2
                else:
                    result_list.append('NO')
                    break
            elif status == 2:
                if ch == 'A':
                    a3 += 1
                else:
                    result_list.append('NO')
                    break
        else:
            if a2 == 0 or status!=2:
                result_list.append('NO')
            elif a1 * a2 == a3:
                result_list.append('YES')
            else:
                result_list.append('NO')
    return result_list

if __name__ == "__main__":
    while True:
        try:
            pat_list = []
            n = int(input())
            for _ in range(n):
                pat_list.append(input())

            result_list = check_pat(pat_list)
            for result in result_list:
                print(result)
        except:
            break