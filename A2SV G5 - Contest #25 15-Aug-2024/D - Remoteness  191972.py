# Problem: D - Remoteness  - https://codeforces.com/gym/535749/problem/D


import sys, threading
from collections import defaultdict, deque

def Int():return int(sys.stdin.readline().strip())
def arr():return list(map(int, sys.stdin.readline().strip().split()))
def String():return sys.stdin.readline().strip()

def main():
    size = Int()
    graph = defaultdict(list)

    for _ in range(size):
        u, v = arr()
        graph[u].append(v)
        graph[v].append(u)

    
    color = [0] * (size + 1)  
    parent = [-1] * (size + 1)
    path = [] 
    cycle_start = -1 
    cycle_end = -1  

    def dfs(node):
        nonlocal cycle_start, cycle_end
        color[node] = 1  
        path.append(node)  
        for neighbor in graph[node]:
            if color[neighbor] == 0:  
                parent[neighbor] = node
                if dfs(neighbor):
                    return True
            elif (
                neighbor != parent[node]
            ):  
                cycle_start = neighbor
                cycle_end = node
                return True
        path.pop()  
        color[node] = 2  
        return False

    cycle_found = False

    dfs(1)


    cycle = []
    cycle.append(cycle_start)
    x = cycle_end
    while x != cycle_start:
        cycle.append(x)
        x = parent[x]
    
   
    queue = [(i , 0) for i in cycle]
    answer = [0] * size
    queue = deque(queue)
    seen = set(cycle)
    while queue:
        node , val = queue.popleft()
        seen.add(node)
        for nbr in graph[node]:
            if nbr not in seen:
                answer[nbr-1] = val + 1
                queue.append((nbr , val+1))

    print(*answer)
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
