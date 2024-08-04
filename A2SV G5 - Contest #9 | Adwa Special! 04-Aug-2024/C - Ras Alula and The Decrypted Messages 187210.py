# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/513152/problem/C

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    # N = int(input())

    n, m = list(map(int, input().split()))
    S = input()
    w = input()

    s = list(S)
    w = list(w)
    summ = 0
    for w in w :
        summ += ord(w)

    prefix  = [0] * (n+1)

    for i in range(n):
        prefix[i+1] = prefix[i] + ord(s[i])

    for i in range(n-m+1):
        if prefix[i+m] - prefix[i] == summ:
            return "YES"
    
    return "NO"
    # i = m 
    # flag = False
    # i = 0
    # for i in range(n-m + 1):
    #     incr = 0
    #     decr = 0
    #     ptr = 0
    #     for j in range(i , i+m):
    #         if w[ptr] > s[j]:
    #             incr += abs(ord(w[ptr]) - ord(s[j]))
    #         else:
    #             decr += abs(ord(w[ptr]) - ord(s[j]))
    #         ptr +=1
    
    #     if decr and decr == incr:
    #         return "YES"
        # print(decr , incr)
    
    
    return "NO"



    # while i <= n:
    
    #     incr , decr = 0 , 0
    #     for ii in range(m):
    #         if w[ii] > d[ii]:
    #             incr += ord(w[ii]) - ord(d[ii])
    #         else:
    #             decr += ord(d[ii]) - ord(w[ii])
    #     # print(incr , decr)
    #     if incr == decr and decr:
    #         flag = True

    #     d.popleft()
    #     if i < len(s):
    #         d.append(s[i])
    #     i+=1
        

    return "YES" if flag else "NO"

            

    

    # arr  = list(map(int, input().split()))

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())