# Problem: B - Optimal Point - https://codeforces.com/gym/535749/problem/B

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from functools import cache
r = lambda n: range(n)

def solve():
    # N = int(input())
    # S = input()

    n, k = list(map(int, input().split()))

    matrix = [list(map(int, input().split())) for _ in range(n)]


    array = [0] * 51

    for a , b in matrix:
        for i in range(a , b+1):
            array[i] += 1
    
    optimal = array[k]

    if optimal == 0:
        return "NO"

    equals = []

    for i in range(len(array)):
        if array[i] >= optimal and i != k:
            equals.append(i)
    
    for a , b in matrix:
        aa = set(range(a , b+1))
        for i in range(a , b+1):
            if i in equals and k not in  aa:
                array[i] -= 1


        # if (a in equals or b in equals) :
        #     if k not in range(a , b+1):
        #         for i in range(a , b+1):
        #             array[i] -=1
    
    if array.count(array[k]) > 1:
        return "NO"
    return "YES"

    # print(optimal)



    # arr  = list(map(int, input().split()))

    # S = list(S)


    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())
