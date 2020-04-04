X, Y, Z = map(int, input().split())

def swap(left, right):
    tmp = left
    left = right
    right = tmp

    return left, right

X, Y = swap(X, Y)
X, Z = swap(X, Z)

print(X, Y, Z)
