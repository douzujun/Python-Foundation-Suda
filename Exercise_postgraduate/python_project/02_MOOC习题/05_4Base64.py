
"""
• 本质上是3字节转4字节
• 3*8=4*6
• 将3字节中数据每次取6 位
• 用6位得到的数值 (0-63)作为索引去查编码表
• 得到编码字符
"""
import string 
import base64

def base64Encode(en_string):
    oldBin = ''
    tempStr = []
    result = ''
    base64_list = string.ascii_uppercase +string.ascii_lowercase \
        + string.digits + '+/'
    
    # 得到2进制字符串流  ord:返回字符的unicode编码(为了能编码汉字)
    for ch in en_string:
        temp = int(bin(ord(ch)).replace('0b', ''))
        oldBin += '{:08}'.format(temp)  # 把数字补到8位
    print(oldBin)

    # 切片 使得每6位合并得到字符串
    for i in range(0, len(oldBin), 6):
        tempStr.append('{:<06}'.format(oldBin[i:i+6]))  # 左对齐长6 (补0)
    print(tempStr)

    # 字符串装数字后查表，得到编码结果字符串
    for item in tempStr:
        result += base64_list[int(item, 2)]
    print(result)


    # 补等号
    if len(result) % 4 == 2:
        result += '=='
    elif len(result) % 4 ==3:
        result += '='

    return result

def testb64module():
    res = base64.b64encode("苏州大学".encode('utf-8'))
    print(str(res, 'utf-8'))        # res是bytes结构
    orgin = base64.b64decode(res)
    print(str(orgin, 'utf-8'))

    res = base64.b64encode("苏州大学".encode('gbk'))
    print(str(res, 'utf-8'))
    orgin = base64.b64decode(res)
    print(str(orgin, 'gbk'))

if __name__ == "__main__":
    print(base64Encode(input("请输入要编码的字符串：")))
    testb64module()
