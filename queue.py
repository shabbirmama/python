from collections import deque

queue = deque(['Tom', 'Jerry', 'Hill'])
queue.append('Graham')
print(queue)
queue.append(23)
print(queue)
queue.popleft()
print(queue)

print(queue.sorted())

