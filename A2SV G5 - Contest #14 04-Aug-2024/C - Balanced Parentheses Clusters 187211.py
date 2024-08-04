# Problem: C - Balanced Parentheses Clusters - https://codeforces.com/gym/520688/problem/C

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    n = int(input())
    S = input()
    S = list(S)

    # row, col = list(map(int, input().split()))

    # arr  = list(map(int, input().split()))
    parent = {i: i for i in range(1, 2 * n + 1)}
    size = {i: 0 for i in range(1, 2 * n + 1)}

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

    def isConnected(x, y):
        return find(x) == find(y)

    stack = []
    counter = 0
    union(1, 2 * n)
    for i in range(2 * n):
        if S[i] == "(":
            stack.append(i + 1)
            counter += 1
        else:
            prev = stack.pop()
            union(prev, i + 1)
            if i < 2*n -1 and S[i+1]  == "(":
                union(i+1 , i+2)

    answer = 0

    for i in range(2 * n):

        if find(i + 1) == i + 1:
            answer += 1
    return answer
    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())