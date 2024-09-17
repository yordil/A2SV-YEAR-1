# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    # N = int(input())
    # S = input()
    
    n, s = list(map(int, input().split()))
    ss = s
    maxx = -1
    minn = -1
    if s >  9* n:
        print(-1 , -1)
        return
    elif s == 0:
        print(-1  , -1) if n > 1 else print(0 , 0)
        return 
    else:
        ans = ""
        while ss:
            if ss > 9:
                ans+="9"
                ss-=9
            else:
                ans+= str(ss)
                ss -=ss

        if len(ans) < n:
            diff = n - len(ans)
            ans += "0" * diff
        maxx = int(ans)
       
    ans = [0] * n
    ans[0] = 1
    ss = s-1
    j  = n-1

    while j >= 0:
        if ss > 9:
            ans[j] += 9
            ss -=9
        else:
            ans[j] += ss
            ss -= ss
        j -= 1

    ans = [str(i) for i in ans]
    ans = "".join(ans)

    minn = int(ans)

    print(minn , maxx)


T = 1
# T = int(input())

for _ in range(T):
    solve()