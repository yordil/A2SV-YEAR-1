# Problem: E - XOR Fan - https://codeforces.com/gym/522079/problem/E

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


def solve():
    N = int(input())

    # row, col = list(map(int, input().split()))

    arr  = list(map(int, input().split()))
    S = input()
    onesxor  = 0
    prefix = [0] * (N+1)
    prefix[1] = arr[0]
    S = list(S)
    flag = False
    for i in range(len(S)):
        if S[i] == "1":
            if flag:
                onesxor ^= arr[i]
            else:
                onesxor = arr[i]
                flag = True
        prefix[i+1] = prefix[i] ^ arr[i]

    q = int(input())
    tot = prefix[-1]
    ans = []
    for i in range(q):
        aa = list(map(int, input().split()))

        if len(aa) == 2:
            if aa[1]  == 0:
                ans.append(tot^onesxor)
            elif aa[1] == 1:
                ans.append(onesxor)

        elif len(aa) == 3:
            onesxor ^=( prefix[(aa[2])] ^ prefix[(aa[1])-1])
    print(*ans)
    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass    


T = 1
T = int(input())

for _ in range(T):
    solve()
