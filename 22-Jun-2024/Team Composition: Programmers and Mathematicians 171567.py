# Problem: Team Composition: Programmers and Mathematicians - https://codeforces.com/problemset/problem/1611/B

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from functools import cache
r = lambda n: range(n)

def solve():
    # N = int(input())
    # S = input()

    a, b = list(map(int, input().split()))
    maxx = (a + b) // 4

    if maxx > min(a, b):
        return min(a  , b )
    else:
        return maxx

    # arr  = list(map(int, input().split()))

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())
