# Problem: D - Meron and Games - https://codeforces.com/gym/523525/problem/D

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from functools import cache


def solve():
    N = int(input())
    # S = input()

    # row, col = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    counter = Counter(arr)
    # print(counter)

    dp = [0] * (max(arr) + 2)
   

    dp[1] = 1 * counter[1]


    for i in range(2, max(arr) + 2):
        dp[i] = max(i * counter[i] + dp[i - 2], dp[i - 1])

    return dp[-1]

    visited = set()

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
# T = int(input())

for _ in range(T):
    print(solve())
