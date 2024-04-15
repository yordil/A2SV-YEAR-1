# Problem: B - Path Finder - https://codeforces.com/gym/517685/problem/B

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    N = int(input())
   
    graph = defaultdict(list)
    for i in range(N-1):
        a , b , c = list(map(int, input().split()))
        graph[a].append((b , c))
        graph[b].append((a , c))
    # finding the longest distance using bfs

    def dfs(node , parent):
        maxx = 0
        for child , cost in graph[node]:
            if child != parent:
                maxx = max(maxx , dfs(child , node) + cost)
            
        
        return maxx
    
    return dfs(0 , -1)
  


T = 1


for _ in range(T):
    print(solve())
