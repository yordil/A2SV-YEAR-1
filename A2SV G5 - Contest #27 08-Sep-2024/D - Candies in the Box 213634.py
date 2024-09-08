# Problem: D - Candies in the Box - https://codeforces.com/gym/538762/problem/D

from collections import deque, defaultdict, Counter
from math import gcd, ceil, floor
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from functools import cache

r = lambda n: range(n)


def solve():
    N = int(input())
    # S = input()
    half = ceil(N / 2)
    if N < 10 :
        return 1

    def binarySearch(k):

        vas, pet = 0, 0
        copyn = N

        while copyn > 0:

            curr = min(k , copyn)
            copyn -= curr
            vas += curr

           
            copyn -= copyn//10

        return vas*2 >= N

    

    left, right = 1, N
    answer = N
    while left  <=  right:
        midd = (left + right) // 2
        
        if binarySearch(midd):
            answer = min(answer , midd)
            right = midd  -1       
        else:
            left = midd + 1

    return answer

    # row, col = list(map(int, input().split()))

    # arr  = list(map(int, input().split()))

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
# T = int(input())

for _ in range(T):
    print(solve())
