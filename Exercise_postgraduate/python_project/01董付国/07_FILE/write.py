import random



def main():
    f = open('integers.txt','w')
    for count in range(500):
        number = random.randint(1,500)
        f.write(str(number) + "\n")
    f.close()

def readfile():
    f = open('integers.txt','r')
    sum = 0
    for line in f:
        line = line.strip()
        number = int(line)
        sum += number
    print("The sum is %d" % (sum))
    f.close()



if __name__ == "__main__":
    main()
    readfile()