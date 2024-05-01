# Problem: C. Restructuring Company - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    # N = int(input())
    # S = input()

    n, q = list(map(int, input().split()))
    parent = {i: i for i in range(1, n + 1)}
    size = {i: 1 for i in range(1, n + 1)}

    def find(x):
        while x != parent[x]:
            x = parent[x]
            parent[x] = parent[parent[x]]
        return x

    def union(x, y):
        parx = find(x)
        pary = find(y)
        if parx != pary:
            if size[parx] > size[pary]:
                parent[pary] = parx
                size[parx] += size[pary]
            else:
                parent[parx] = pary
                size[pary] += size[parx]


    
    parentnew = {i : i+ 1 for i in range(1 , n+1)}

    for i in range(q):
        a, b, c = list(map(int, input().split()))

        if a == 3:
            if find(b) == find(c):
                print("YES")
            else:
                print("NO")
        elif a == 1:
            union(b, c)
        else:
            lastparent = parentnew[b]

            while lastparent <= c:
                union(b , lastparent)
                lastpos = parentnew[lastparent]
                parentnew[lastparent] = parentnew[c]
                lastparent = lastpos



T = 1
# T = int(input())

for _ in range(T):
    solve()

