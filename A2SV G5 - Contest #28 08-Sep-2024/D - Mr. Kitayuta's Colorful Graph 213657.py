# Problem: D - Mr. Kitayuta's Colorful Graph - https://codeforces.com/gym/540354/problem/D

from collections import defaultdict
import sys


# Input helpers
def II():
    return int(sys.stdin.readline().strip())


def IL():
    return list(map(int, sys.stdin.readline().strip().split()))


def S():
    return sys.stdin.readline().strip()


# Range shortcut
r = lambda n: range(n)

def solve():
    
    n, m = IL()  
    graph = defaultdict(list)

    
    for _ in range(m):
        f, t, c = IL()
        graph[f].append((t, c))
        graph[t].append((f, c))

    queries = []
    for _ in range(II()):
        a, b = IL()
        queries.append((a, b))

    answers = []
    def dfs(a, b, color, graph):
        
        stack = [a]
        vis = set()
        vis.add(a)

        while stack:
            node = stack.pop()
            if node == b:
                return True
            for nbr, col in graph[node]:
                if col == color and nbr not in vis:
                    vis.add(nbr)
                    stack.append(nbr)
        return False

    for a, b in queries:
        res = 0
        for color in range(1, 101):   
            if dfs(a, b, color, graph):
                res += 1
        print(res)

    return 



T = 1
# T = int(input())

for _ in range(T):
    solve()
