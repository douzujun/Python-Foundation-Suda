import re

# pattern1 = '(.)\\1+'
pattern1 = r'(.)\1+'

r1 = re.compile(pattern1)


while True:
    try:
        st = input("input a string ")
        if r1.match(st):
            print("r1 match")
        else:
            print("r1 dismatch")

    except:
        break