from os import path

def read_files(Folder='ch7_Folder'):
    total_content = []
    for i in range(1,5):
        p = path.join(Folder, 'file{}.txt'.format(i))
        f = open(p,'r')
        content = f.readlines()
        total_content.extend(content)
        f.close()
    return total_content

def write_merge(content, Folder='ch7_Folder'):
    p = path.join(Folder, 'merge.txt')
    f = open(p, 'w')
    f.writelines(content)
    f.close()

if __name__ == "__main__":
    content = read_files()
    write_merge(content)