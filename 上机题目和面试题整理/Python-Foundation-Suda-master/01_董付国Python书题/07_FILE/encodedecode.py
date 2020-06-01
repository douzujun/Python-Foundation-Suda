with open('GBK.txt', 'rb') as f:
    b1 = f.read()
    print("GBK bytes:", b1)
    s1 = b1.decode('GBK')
    print("GBK text:", s1)
    b2 = s1.encode('utf-8')
    print("\nutf-8 bytes:", b2)
    s2 = b2.decode('utf-8')
    print("utf-8 text:", s2)