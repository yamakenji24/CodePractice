import math
Bill, Total = map(int, input().split())

# 10000円札, 5000円札, 1000円札の３種類

#普通に解くと
def otoshidama():
    for i in range(Bill + 1):
        for j in range(Bill + 1 - i):
            k = Bill - i - j
            if(10000*i + 5000*j + 1000*k == Total):
                return i, j, k
    return -1, -1, -1

# 数学的に
def ByMathmatic():
    # i + j + k = Bill
    # (10000 * i) + (5000 * j) + (1000 * k) = Total 
    # 変数 k を消去して
    # 9000i + 4000j = Total - 1000Bill
    t = (Total - 1000 * Bill) / 1000
    # と置くことで、 9i + 4j = t とおける
    # 不定方程式で、gcd(9, 4) = 1 より整数解は存在する
    i = t % 4
    j = (t - 9 * (t % 4)) / 4
    # i = 4m + a
    # j = -9m + b と置けるようになる
    # i, jは0以上なので、 0 <= 4m+a, 0<=-9m + b
    # i + j <= Bill なので、 4m+a + -9m+b <= Bill
    minK = max(math.ceil(-1 * i / 4), math.ceil((i + j - Bill) / 5))
    maxK = math.floor(j / 9)
    if (minK <= maxK):
        k = minK
        x = 4 * k + i
        y = -9 * k + j
        z = Bill - x - y
        return x, y, z
    else:
        return -1, -1, -1
        
print(ByMathmatic())
