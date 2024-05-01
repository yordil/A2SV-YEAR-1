# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    N = int(input())
    # S = input()
    if N == 1:
        return 3
    elif N &(N-1) == 0:
        return N+1
    binaryn = bin(N)
    answer = ""
    for i in range(len(binaryn)-1 , -1 , -1):
        if binaryn[i] == "1":
            answer += binaryn[i]
            break
        answer +=binaryn[i]
    return int(answer[::-1] , 2)

    


    # row, col = list(map(int, input().split()))

    # arr  = list(map(int, input().split()))

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())
