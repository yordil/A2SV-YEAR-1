# Problem: Odd Sum - https://codeforces.com/problemset/problem/797/B

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

    arr.sort()
    odd = 0
    index = bisect_left(arr, 0)
    # if even like 100 
    summ = sum(arr[index:])
    tempsum = 0
    if summ % 2:
        return summ
    else:
       tempsum = summ
       for i in range(index-1 , -1 , -1):
           if arr[i] % 2:
               tempsum += arr[i]
               break
       for a in range(index, N):
           if arr[a] % 2:
               summ -= arr[a]
               break
    if tempsum % 2 and summ % 2:
        return max(tempsum, summ)
    elif tempsum % 2:
        return tempsum
    else:
        return summ


    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
# T = int(input())

for _ in range(T):
    print(solve())
