import collections

N = int(input())
S = []
for _ in range(N):
    S.append(input())
c = collections.Counter(S)

print(len(c))
