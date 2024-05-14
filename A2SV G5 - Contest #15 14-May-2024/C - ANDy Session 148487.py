# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    # N = int(input())
    # S = input()

    n, k = list(map(int, input().split()))

    arr  = list(map(int, input().split()))
    ans = ["0"] * 31
    ones = []
    
    for i in range(31):
        count = 0
        for num in arr:
            if  num & 1<<i:
                count+=1
        ones.append(n-count)

    # print(ones)

    ones = ones[::-1]

    for i in range(31):
        if k >= ones[i]:
            ans[i] = "1"
            k -= ones[i]
        elif ones[i] == 0:
            ans[i] = "1"

    return int("".join(ans) , 2)




    # arr  = list(map(int, input().split()))

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())
