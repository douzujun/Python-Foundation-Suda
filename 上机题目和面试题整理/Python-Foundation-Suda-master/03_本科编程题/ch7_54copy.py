
import shutil

def copy_file(filename='ch7_54_copy.txt'):
    shutil.copyfile(filename, 'ch7_54_new.txt')

if __name__ == "__main__":
    copy_file()