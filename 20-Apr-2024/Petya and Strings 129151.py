# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    # N = int(input())
    a = input()
    b = input()

    if a.lower() == b.lower():
        return 0
    elif a.lower() < b.lower():
        return -1
    else:
        return 1

    # row, col = list(map(int, input().split()))

    # arr  = list(map(int, input().split()))

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
# T = int(input())

for _ in range(T):
    print(solve())
