import os


def visit_dir(path):
    if not os.path.isdir(path):
        print("Errpr:", path, "is not a directory or doesn t exisit.")
    else:
        for l in os.listdir(path):
            sub_path = os.path.join(path, l)
            print(sub_path)
            if os.path.isdir(sub_path):
                visit_dir(sub_path)


def visit_dir2(path):
    if not os.path.isdir(path):
        print("Errpr:", path, "is not a directory or doesn t exisit.")
    else:
        # 使用walk方法
        list_dirs = os.walk(path)
        for root, dirs, files in list_dirs:
            for d in dirs:
                # 列出root下的所有目录
                print(os.path.join(root, d))
            for f in files:
                # 列出root下的所有文件
                print(os.path.join(root, f))


if __name__ == '__main__':
    path = input("input path: ")
    # visit_dir1(path)
    visit_dir2(path)
