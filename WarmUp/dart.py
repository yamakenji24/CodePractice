from bisect import bisect_right
def main():
    N, M = map(int, input().split())
    P = [int(input()) for _ in range(N)]
    P.append(0)
    #Q = {1 for i in range(N+1) for j in range(i, N+1) if P[i] + P[j] <= M}
    Q = {P[i] + P[j] for i in range(N+1) for j in range(i, N+1) if P[i] + P[j] <= M}
    Q = sorted(Q)
    print(Q)
    ans = 0
    for q in Q:
        idx = bisect_right(Q, M-q) - 1
        res = q + Q[idx]
        ans = max(ans, res)
    print(ans)
main()
