# Problem: C - Permutation Sorting - https://codeforces.com/gym/538762/problem/C

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from functools import cache
import sys


def II():
    return int(sys.stdin.readline().strip())


def IL():
    return list(map(int, sys.stdin.readline().strip().split()))


def S():
    return sys.stdin.readline().strip()


r = lambda n: range(n)


def solve():
    N = int(input())
    # S = input()

    # row, col = list(map(int, input().split()))

    arr  = list(map(int, input().split()))

    sett = set()
    ans  = 0
    for a in arr:
        if a + 1 in sett:
            ans +=1
        sett.add(a)
    return ans 

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())
