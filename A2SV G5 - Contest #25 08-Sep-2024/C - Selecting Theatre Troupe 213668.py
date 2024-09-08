# Problem: C - Selecting Theatre Troupe - https://codeforces.com/gym/535749/problem/C

from collections import deque, defaultdict, Counter
from math import gcd, ceil , comb
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


def combination(n, k):
    if k > n or k < 0:
        return 0
    return comb(n, k)

def solve():
    
    n, m, t = map(int, input().split())

    tot = 0
    
    # Iterate over the number of boys to be selected
    for by in range(4, min(n, t) + 1):
        gl = t - by
        
        if gl >= 1 and gl <= m:
            tot += combination(n, by) * combination(m, gl)
    
    return tot

   


    pass


T = 1
# T = int(input())

for _ in range(T):
    print(solve())
