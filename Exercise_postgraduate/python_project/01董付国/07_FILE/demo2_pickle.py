import pickle


def pdump():
    global f
    n = 4
    i = 1300
    a = 99.2
    dic = {'1': 'a', '2': 'b'}
    try:
        pickle.dump(n, f)
        pickle.dump(i, f)
        pickle.dump(a, f)
        pickle.dump(dic, f)
    except Exception as e:
        print(e)
    finally:
        f.flush()


def pload():
    global f
    f.seek(0)
    n = pickle.load(f)
    i = 1
    while i < n:
        x = pickle.load(f)
        print(x)
        i = i + 1


if __name__ == '__main__':
    global f
    f = open('pickle.dat', 'wb+')
    pdump()
    pload()
    f.close()

