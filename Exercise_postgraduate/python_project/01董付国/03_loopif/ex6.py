"""
x<0         0
0<=x<5      x
5<=x<10     3x-5
10<=x<20    0.5x-2
20<=x       0
"""

def divfunc(x):
    if x < 10:
        if x>=5:
            return 3*x-5
        elif x>=0:
            return x
        else:
            # x<0
            return 0
    elif x < 20:
        return 0.5*x -2
    else:
        # 20<=2
        return 0