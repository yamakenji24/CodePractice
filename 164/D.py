import numpy as np
#S = list(input().strip())
#length = len(S)
#op = np.asarray(S)

def solution():
    S = input()
    N = len(S)
    num = [0] * 2019
    num[0] = 1
    c, ans, dgt = 0, 0, 1
    for i in reversed(range(N)):
        c = (c + int(S[i]) * dgt) % 2019
        print("c: ", c)
        dgt *= 10
        dgt %= 2019
        ans += num[c]
        num[c] += 1
        
    print(ans)
solution()

# 以下は遅すぎましたはい
def sample():
    x = -1
    count = 0
    for i in op:
        x += 1
        group = ""
        for j, name in enumerate(op, x):
            group += name
            if int(group) % 2019 == 0:
                count += 1
    print(count)

def checkValue():
    count = 0
    for i in range(length):
        group = ""
        for j in range(i, length):
            group += op[j]
            if int(group) % 2019 == 0:
                count += 1
    print(count)
