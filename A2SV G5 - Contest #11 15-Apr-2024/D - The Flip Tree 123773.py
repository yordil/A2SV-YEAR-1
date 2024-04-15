# Problem: D - The Flip Tree - https://codeforces.com/gym/515998/problem/D

from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for _ in range(n -1):
    v,u = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

arr1 =  list(map(int,input().split()))
arr2 =  list(map(int,input().split()))

stack = [(1,0,0,0)]
ans = []
visited = set()

while stack:
    node,level,even,odd = stack.pop()
    visited.add(node)

    if level == 0:#for father
        if even % 2 == 0:#if the g.fth is even no change needed
            if arr1[node -1] !=  arr2[node-1]:
                ans.append(node)
                even += 1
        else: 
            if 1 - arr1[node -1] !=  arr2[node-1]: #check is the changed value is equal to goal
                ans.append(node)
                even += 1
    else:#for child
        if odd % 2 == 0:
            if arr1[node -1] !=  arr2[node-1]:
                ans.append(node)
                odd += 1
        else:
            if 1 - arr1[node -1] !=  arr2[node-1]:
                ans.append(node)
                odd += 1
        
    for ni in graph[node]:
        if ni not in visited:
            stack.append((ni,1-level,even, odd))
    

print(len(ans))

for  i in range(len(ans) - 1,-1,-1):
    print(ans[i])
