# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from heapq import heappush, heappop, heapify


def solve():
    N = int(input())

    # S = input()

    # row, col = list(map(int, input().split()))
    arr = []
    heap = []
    insert = "insert"
    getMin = "getMin"
    answer = []
    for i in range(N):
        a= list(map(str, input().split()))
        if a[0] == "insert":
            heappush(heap , int(a[1]))
            answer.append(a)
        elif a[0] == "removeMin":
            if heap:
                heappop(heap)
                answer.append(a)
            else:
                answer.append(["insert 0"])
                answer.append(a)
        elif a[0] == "getMin":
            while heap and heap[0] < int(a[1]):
                heappop(heap)
                answer.append(["removeMin"])
            if heap and heap[0] == int(a[1]):
                answer.append(a)
            else:
                mystr = "insert " + str(a[1])
                heappush(heap , int(a[1]))
                answer.append([mystr])
                answer.append(a)

    print(len(answer))
    for a in answer:
        if len(a) == 1:
            print(*a)
        else:
            print(a[0] , a[1])

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
# T = int(input())

for _ in range(T):
    solve()
