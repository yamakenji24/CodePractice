N = int(input())
count = 0

for k in range(2, N+1):
    tmpN = N
    while(tmpN >= k):
        if tmpN % k == 0:
            tmpN = tmpN / k
        else:
            tmpN = tmpN - k
    if tmpN == 1:
        count += 1

print(count)
