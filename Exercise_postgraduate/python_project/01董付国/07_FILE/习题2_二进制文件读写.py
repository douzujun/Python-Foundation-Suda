"""
将学生成绩字典保存为二进制文件，然后读取内容并显示。
"""
import pickle

filename = ".\习题2_成绩字典.bin"

def read_dict():
    f = open(filename, 'rb')
    score_dict = pickle.load(f)
    return score_dict

def write_dict(score_dict):
    f = open(filename, 'wb')
    pickle.dump(score_dict, f)
    print('已写入', filename)
    f.close()

if __name__ == "__main__":
    mode = input('输入模式 r or w:')
    if mode == 'w':
        score_dict = {'小明':99,'小红':100}
        write_dict(score_dict)
    else:
        print(read_dict())