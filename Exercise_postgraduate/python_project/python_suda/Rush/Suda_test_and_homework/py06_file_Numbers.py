#-*- coding: utf-8 -*-

def readNumbers(url):
    with open(url, 'r', encoding='utf8') as f:
        nums = f.readlines()
        return list( map(lambda x: float(x.strip()), nums) )    
    
def SortByNums(url, nums):
    with open(url, 'w', encoding='utf8') as f:
        nums.sort()
        for e in nums:
            f.write(str(e) + '\n')

def Avg_and_Var(url, nums):
    with open(url, 'a', encoding='utf8') as f:
        ave = sum(nums) / len(nums)
        var = sum([(num - ave)**2 for num in nums]) / len(nums)
        f.write('avg: ' + str(ave) + '\n' + 'var: ' + str(var) + '\n')

def main():
    numbers = readNumbers('./Suda_test_and_homework/File/numbers.txt')
    print(numbers)
    SortByNums('./Suda_test_and_homework/File/Sort.txt', numbers)

    Avg_and_Var('./Suda_test_and_homework/File/Sort.txt', numbers)

if __name__ == "__main__":
    main()