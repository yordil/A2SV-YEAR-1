# Problem: G - MEX Tree Labeling - https://codeforces.com/gym/544853/problem/E

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from functools import cache
r = lambda n: range(n)

def solve():


    n = int(input())
    v = defaultdict(list)
    ans = [-1] * 100005
    
   
    for i in range(1, n):
        a, b = map(int, input().split())
        v[a].append(i)
        v[b].append(i)
        ans[i] = -1


    mx = (0, 0)
    for i in range(1, n + 1):
        mx = max(mx, (len(v[i]), i))

    
    cur = 0
    for i in v[mx[1]]:
        ans[i] = cur
        cur += 1
    
    for i in range(1, n):
        if ans[i] == -1:
            ans[i] = cur
            cur += 1
        print(ans[i])

T = 1
# T = int(input())

for _ in range(T):
    (solve())
