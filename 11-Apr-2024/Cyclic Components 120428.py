# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
 
    n, m = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(m):
        u, v = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)

    stack = []
    visited = set()
    cycle = 0

    def dfs(node):
        stack.append(node)
        temp  = []
        temp.append(node)
        while temp:
            node = temp.pop()
            stack.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    temp.append(neighbor)
                    visited.add(neighbor)
        for vertex in stack:
            if len(graph[vertex]) != 2:
                stack.clear()
                return False

        stack.clear()
        return True


    for vertex in graph:
        if vertex in visited:
            continue
        if dfs(vertex):
            cycle += 1
         

    return cycle

    

    

    pass


T = 1
# T = int(input())

for _ in range(T):
    print(solve())



