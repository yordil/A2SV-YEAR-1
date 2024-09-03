# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

from collections import deque, defaultdict, Counter
from math import gcd, ceil , sqrt
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from functools import cache

r = lambda n: range(n)


def solve():
    N = int(input())
    # S = input()

    bit = bin(N)[2:]

    fliped = ""
  
    for i in bit:
        fliped += str(int(i) ^ 1)

    i = 0
    while i < len(fliped):
        if i != "0":
            break
        i+=1
    nn = len(fliped)
    fliped = fliped[i:]

    b = int(fliped , 2)
    
    if b == 0:
        root = int(sqrt(N)) + 1
        ans  = 0
        i = 2
        while i <= root:
            if N % i == 0:

                ans = max(i ,  N// i , ans)
            i+=1
        
        return ans if ans else 1
    
    # print(N , b  ,  N ^ b   , N & b)
    return gcd(N ^ b, N & b)

    
    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())
