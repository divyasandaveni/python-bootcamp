#from collections import deque
from collections import deque

numbers=[1,2,3,4]

numbers=deque(numbers)

numbers.pop()#if we do popleft the op;[2,3,4]
print(numbers)

