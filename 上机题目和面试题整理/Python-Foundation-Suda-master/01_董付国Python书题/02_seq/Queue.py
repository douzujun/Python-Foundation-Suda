import queue

# FIFO
q = queue.Queue()
q.put(0)
q.put(1)
print(q.queue)
print(q.get())  # 出队

# LIFO
LIFOQueue = queue.LifoQueue(3)  # 可以选择设置队列大小

# 优先级队列PriorityQueue
# Variant of Queue that retrieves open entries in priority order (lowest first).
# Entries are typically tuples of the form:  (priority number, data).