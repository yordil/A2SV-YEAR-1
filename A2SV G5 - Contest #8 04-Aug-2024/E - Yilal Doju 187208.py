# Problem: E - Yilal Doju - https://codeforces.com/gym/511242/problem/E

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    N = int(input())
    # S = input()
    # row, col = list(map(int, input().split()))
    arr  = list(map(int, input().split()))
    answer = float("inf")

    minn = min(arr)
    minn = arr.index(minn)
    arr[minn] +=100000000
    min2 = min(arr)
    min2 = arr.index(min2)
    arr[minn] -=100000000

    answer = ceil(arr[minn] / 2) + ceil(arr[min2] / 2)

    for i in range(len(arr) -1):
        minn = min(arr[i], arr[i+1])
        maxx = max(arr[i], arr[i+1])

        if maxx / 2 < minn:
            answer = min(answer, ceil((arr[i] + arr[i+1])/3))
        else:
            answer = min(answer, ceil(maxx/2))

    for i in range(1 , len(arr)-1):
        answer = min(answer, ceil((arr[i-1] + arr[i+1])/2))

    return answer


    

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
# T = int(input())

for _ in range(T):
    print(solve())