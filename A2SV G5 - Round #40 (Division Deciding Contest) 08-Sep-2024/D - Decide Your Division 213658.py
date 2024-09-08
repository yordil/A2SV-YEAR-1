# Problem: D - Decide Your Division - https://codeforces.com/gym/543431/problem/D

from collections import deque, defaultdict, Counter
from math import gcd, ceil, sqrt
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from functools import cache

r = lambda n: range(n)


def solve():
    N = int(input())
    answer = 0

    # init = 1

    # while init < N:

    #     if (2*init) < N:
    #         init *=2
    #     elif (3*init) % 2 == 0 and (3*init) / 2 < N:
    #         init *= 2
    #         init /=3
    #     elif (4*init) % 5 == 0 and (4*init) / 5 < N:
    #         init *= 4
    #         init /=5
    #     answer +=1
    # return answer
        

    while N != 1:
        if N % 2 == 0:
            N //= 2
            answer += 1
        elif N % 3 == 0:
                N //= 3
                # N*=2
                answer +=2
        elif N % 5 == 0:
            N //= 5
            # N*=4
            answer += 3

        else:
            break

    return answer if N == 1 else -1

    # S = input()

    # row, col = list(map(int, input().split()))

    # arr  = list(map(int, input().split()))

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())
