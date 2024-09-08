# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from functools import cache
r = lambda n: range(n)

def solve():
    N = int(input())
    # S = input()

    # row, col = list(map(int, input().split()))

    arr  = list(map(int, input().split()))
    r = N -2
    flag = 1
    answer = 0
    zeroCount = 0
    n  = 0
    flag = False
    while n < N-1:
        if arr[n] !=0:
            flag = True
        answer +=1 if flag and arr[n]== 0 else arr[n]
        n+=1
    return answer
    # while r >= 0:
    #     if flag and arr[r]:
    #         answer += arr[r]
    #     elif arr[r] == 0:
    #         zeroCount +=1
    #         flag  = 0
    #     else:
    #         if zeroCount <= arr[r]:
    #             answer += 2 * (zeroCount)
    #             answer += arr[r] - zeroCount 
    #         else:
    #             answer += 2* arr[r]
    #         zeroCount = 0
    #         flag  = 1
    #     r-=1
    
    return answer

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())
