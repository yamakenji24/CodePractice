N, K = map(int, input().split())

def substract(min):
    if N % K == 0:
        return 0
    tmp = N % K
    if abs(tmp - K) < tmp:
        return abs(tmp-K)
    return tmp
    
if abs(N-K) < N or abs(N-K) < K:
    print(substract(abs(N-K)))
elif N < K:
    print(N)
else:
    print(K)
