
def func1():
    values = (0, 1)
    candidates = [(A, B, C, D, E) for A in values
                for B in values
                for C in values
                for D in values
                for E in values]



def func2():
    # A:not A not C
    # B:B or D
    # C:A not B
    # D:not B
    # true * 1
    for winner in ('A','B','C','D'):
        t = 0
        if winner != 'A' and winner != 'C':
            t +=1
        if winner == 'B' or winner == 'D':
            t+=1
        else:   # B错误
            t+=1
        if winner == 'A':
            t +=1
        if t == 1:
            print(winner)
            break

if __name__ == "__main__":
    func2()