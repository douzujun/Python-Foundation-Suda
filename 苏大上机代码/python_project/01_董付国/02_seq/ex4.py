import random

l = [random.randint(0, 100) for i in range(20)]
print(l)
l2 = sorted(l[:10]) + sorted(l[10:], reverse=True)
print(l2
      )