import os

class CodeCounter:
    def __init__(self, targetdir='', ext='py'):
        self.targetdir = targetdir
        self.ext = ext
        print('now working at ' + self.targetdir)
    
    def chdir(self, newdir=''):
        self.targetdir = newdir
        print('now working at ' + self.targetdir)

    def list_ext(self):
        return os.walk(self.targetdir)

    def count_files(self):
        total = 0
        for root, _, files in self.list_ext():
            for name in files:
                if os.path.splitext(name)[1] == '.py':
                    length = self.count_line(os.path.join(root, name))
                    total += length
                    print(name,': ', length)
        return total

    def count_line(self, file_path):
        f = open(file_path, 'r', encoding='utf-8')
        try:
            lines = f.readlines()
        except UnicodeDecodeError as e:
            print(e,'when reading ', file_path)
            f.close()
            return 0
        f.close()
        mode, length = 1, 0
        for line in lines:
            if r'"""' in line:
                mode = -mode
            if mode == 1:
                if line != '\n':
                    # print(line, end='')
                    length += 1
        return length

if __name__ == "__main__":
    # dirname = "D:\\CODE\\PythonFoundation\\"
    dirname = input(r"请输入文件夹地址例如D:\\CODE\\PythonFoundation\\:")
    py = CodeCounter(dirname)
    
    # py.list_ext()
    # print(py.count_line(r'D:\CODE\PythonFoundation\07_FILE\demo1.py'))
    print(py.count_files())