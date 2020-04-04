N, M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)

def checkPopular():
    count = 0
    for i in range(N):
        if (A[i] / total)  >= (1 / (4*M)):
            count += 1
    return count

if checkPopular() < M:
    print('No')
else:
    print('Yes')

    
