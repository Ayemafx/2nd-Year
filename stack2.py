import random
import time
from collections import deque


def queue_list(M, N):
    for i in range(M):
        queue = []
        # enqueue N random integers into the list
        for j in range(N):
            queue.append(random.randint(1, 100))
        # dequeue the elements from the list
        start_time = time.time()
        for j in range(N):
            queue.pop(0)
        end_time = time.time()
        print(f"List implementation: Dequeueing {N} elements took {end_time - start_time:.6f} seconds")


def queue_deque(M, N):
    for i in range(M):
        queue = deque()
        # enqueue N random integers into the deque
        for j in range(N):
            queue.append(random.randint(1, 100))
        # dequeue the elements from the deque
        start_time = time.time()
        for j in range(N):
            queue.popleft()
        end_time = time.time()
        print(f"Deque implementation: Dequeueing {N} elements took {end_time - start_time:.6f} seconds")


# example usage
M = 5
N = 1000
queue_list(M, N)
queue_deque(M, N)
