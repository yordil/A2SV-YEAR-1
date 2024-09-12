# Problem: E - Machine Testing - https://codeforces.com/gym/513152/problem/E

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    N = int(input())
    health = list(map(int, input().split()))
    power = list(map(int, input().split()))
    if N == 1:
        return 0

    stack = [ [float("inf") , power[0]]]

    totalseconds =   0 

    for i in range(1, N):   
        temp = 0    
        temptime  = 0
        while  stack and health[i] > (stack[-1][0] - temptime) * stack[-1][1] or temptime >= stack[-1][0]:
            if temptime < stack[-1][0]:
                health[i] -= (stack[-1][0] - temptime) * stack[-1][1]
                temp += (stack[-1][0] - temptime)
            
            stack.pop()
            temptime = temp
            
        temptime += ceil(health[i]/stack[-1][1])
        temp += ceil(health [i]/stack[-1][1])  
        totalseconds = max(totalseconds , temp)
        stack.append([temp  , power[i]])

    return totalseconds
        

    # row, col = list(map(int, input().split()))

    # arr  = list(map(int, input().split()))

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())
