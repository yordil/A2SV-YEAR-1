# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    # N = int(input())
    # S = input()

    n, m , k = list(map(int, input().split()))
    parent = {i: i for i in range(1 , n+1)}
    size = {i: 1 for i in range(1 , n+1)}
    def find(x):
        while x != parent[x]:
            x = parent[x]
            parent[x] = parent[parent[x]]

        return x
    def union(x , y):
        parx = find(x)
        pary = find(y)
        if parx != pary:
            if size[parx] > size[pary]:
                parent[pary] = parx
                size[parx] += size[pary]
            else:
                parent[parx] = pary
                size[pary] += size[parx]
    def isConnected(x , y):
        return find(x) == find(y)

   

    for i in range(m):
         a = list(map(int, input().split()))
    queue = []
    for i in range(k):
        ss = input().split()
        queue.append(ss)
    
    answer = deque()
    for word , fromm , to in queue[::-1]:
       if word == "cut":
           union(int(fromm) , int(to))
       else:
            if isConnected(int(fromm) , int(to)):
              answer.appendleft("YES")
            else:
              answer.appendleft("NO")
       
    for a in answer:
        print(a)

  

   


T = 1
# T = int(input())

for _ in range(T):
    solve()
