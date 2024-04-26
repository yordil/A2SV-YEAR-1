# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations

val = 3 * (pow(10, 5))


def solve():
    # N = int(input())
    # S = input()
    n, m = list(map(int, input().split()))
    parent = {i: i for i in range( n + 1)}
    minpar = {i: i for i in range( n + 1)}
    maxpar = {i: i for i in range(n + 1)}
    size = {i: 1 for i in range( n + 1)}

    def find(x):
        while x != parent[x]:
            x = parent[parent[x]]
        return x

    def union(x, y):
        parx = find(x)
        pary = find(y)

        if parx != pary:
            if size[parx] > size[pary]:
                parent[pary] = parx
                size[parx] += size[pary]
                minpar[parx] = min(minpar[pary], minpar[parx])
                maxpar[parx] = max(maxpar[pary], maxpar[parx])
            else:
                parent[parx] = pary
                size[pary] += size[parx]
                minpar[pary] = min(minpar[parx], minpar[pary])
                maxpar[pary] = max(maxpar[parx], maxpar[pary])

    def isConnected(x, y):
        return find(x) == find(y)

    answer = []
    query = []
    for i in range(m):
        strr = input()
        query = strr.split()
        if len(query) == 3:
            union(int(query[1]), int(query[2]))
        else:
            pare = find(int(query[1]))
            answer.append([minpar[pare], maxpar[pare], size[pare]])
    for a, b, c in answer:
        print(a, b, c)


T = 1
# T = int(input())

for _ in range(T):
    solve()
