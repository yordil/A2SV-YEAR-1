# Problem: D - The Kittens Test - https://codeforces.com/gym/520688/problem/D

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    n = int(input())
    query = []

    parent = {i : i for i in range(1 , n+1)}
    size = {i: i for i in range(1 , n+1)}
    answer = [ [i] for i in range(1 , n+1)]
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
                answer[parx-1].extend(answer[pary-1])
            else:
                parent[parx] = pary
                size[pary] += size[parx]
                answer[pary-1].extend(answer[parx-1])
    def isConnected(x , y):
        return find(x) == find(y)
    
    for i in range(n-1):
        a , b = list(map(int, input().split()))
        union(a , b)
    index = find(n)
    

    print(*answer[index-1])

        




T = 1
# T = int(input())

for _ in range(T):
    solve()