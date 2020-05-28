import heapq
import random

data = list(range(10))
random.shuffle(data)

# 建堆
heap = []  # 使用heapq包对列表进行操作
for n in data:
    heapq.heappush(heap, n)  # 数据入堆

# 弹出堆的最小元素(堆会自动重建)
heapq.heappop(heap)

# 列表转换为堆
myheap = [i for i in range(10)]
heapq.heapify(myheap)

# heapreplace(heap, item) -> value. Pop and return the current smallest value, and add the new item.
heapq.heapreplace(myheap, 6)

heapq.nlargest(3, myheap)   # 返回前3个最大的元素
heapq.nsmallest(3, myheap)  # 返回前3个最小的元素
