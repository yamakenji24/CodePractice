from sys import stdin
import collections

def main():
    readline = stdin.readline
    N = int(input())
    A = list(map(int, readline().split()))
    listN = list(range(1, N+1))    
    c = collections.Counter(A)
    
    for i in listN:
        print(c[i])
main()
