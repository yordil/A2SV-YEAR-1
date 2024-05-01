# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    # N = int(input())
    # S = input()

    n, m, k = list(map(int, input().split()))
    arr = []
    for i in range(m + 1):
        arr.append(int(input()))
    ans = 0
    fedor = arr[-1]
    for i in range(m):
        if bin((arr[i] ^ fedor)).count("1") <= k:
            ans+=1
    return ans

   
    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
# T = int(input())

for _ in range(T):
    print(solve())
