from collections import deque

K = int(input())

d = deque(range(1, 10))

def Lunlun():
    for i in range(K):
        x = d.popleft()
        r = x % 10
        
        if r != 0:
            d.append((10 * x) + (r - 1))
        d.append(10 * x + r)
        if r != 9:
            d.append((10 * x) +(r + 1))
    return x

        
print(Lunlun())
