import time
K, S = map(int, input().split())

# 0 <= X, Y, Z <= K
# X + Y + Z = S を満たすX, Y, Zの値は何通りあるか

def triple():
    start = time.time()
    ans = 0
    for x in range(K+1):
        for y in range(K+1):
            for z in range(K+1):
                if x + y + z == S:
                    ans += 1
    elapsed_time = time.time() - start    
    return ans, elapsed_time

def double():
    ans = 0
    for x in range(K+1):
        for y in range(K+1):
            if 0 <= S - x - y <= K:
                ans += 1
    return ans

# よくわかりませんでした
def single():
    start = time.time()
    ans = 0
    for x in range(K+1):
        # 欲しい値から 今の値とmax範囲を引いたやつのmaxをとる(マイナスに行くのを防ぐ？)
        y_min = max(S - x - K, 0)
        y_max = min(S - x, K)
        ans += max(0, y_max - y_min + 1)
    elapsed_time = time.time() - start    
    return ans, elapsed_time

print(single())
print(triple())
