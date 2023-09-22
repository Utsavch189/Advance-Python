"""
It's a optimized list for quicker append and pop operations from both sides of the container. It provides O(1) time for 
append and pop as compared to list with O(n) complexity.
"""

from collections import deque

queue=deque([1,2,3,5,4,9])

print(queue)

print("after appending 30 ")
queue.append(30) # append to end
print(queue)

print("after appending 55 ")
queue.appendleft(55) # append to start
print(queue)

print("after removing last elem ")
queue.pop()
print(queue)

print("after removing first elem ")
queue.popleft()
print(queue)