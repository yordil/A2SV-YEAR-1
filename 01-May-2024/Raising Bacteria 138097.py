# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations

# arr = [pow(2 , i) for i in range(0 , 32)]
def solve():
    
    N = int(input())
    if N & N-1 == 0:
        return 1
    else:
        day  = 0
        while N:
            if N & 1:
                day +=1
            N = N>>1
        return day
    # S = input()


    # row, col = list(map(int, input().split()))

    # arr  = list(map(int, input().split()))

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
# T = int(input())

for _ in range(T):
    print(solve())
