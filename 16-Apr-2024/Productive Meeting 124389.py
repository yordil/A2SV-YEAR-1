# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from heapq import heapify , heappop , heappush

def solve():
    N = int(input())
   

    arr  = list(map(int, input().split()))

    newarr = []
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        newarr.append([-arr[i], i+1])
    heapify(newarr)
    answer = []
    while len(newarr) > 1:
        first = heappop(newarr)
        second = heappop(newarr)
        answer.append([first[1] , second[1] ])
        
        if first[0] + 1 < 0:
            heappush(newarr , [first[0] +1 , first[1]])
          
        if second[0] + 1 < 0:
            heappush(newarr , [second[0] +1 , second[1]])\
        
      
          
    print(len(answer))
    for b , a in answer:
        print(a , b)




    pass


T = 1
T = int(input())

for _ in range(T):
    solve()
