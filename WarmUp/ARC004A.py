N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for u in S:
    for v in S:
        res = pow(pow(abs(u[0] - v[0]), 2) + pow(abs(u[1] - v[1]), 2), 1/2)
        ans = max(ans, res)
print(ans)
