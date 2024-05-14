# Problem: D - Medina & Merbebt - https://codeforces.com/gym/522079/problem/D

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
from functools import cache

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    q = int(input())

    arr = [0] * 32
    prefix = [arr] 

    for num in nums:
        arr = prefix[-1].copy()
        for i in range(32):
            if num & (1 << i) != 0:
                arr[i] += 1
        prefix.append(arr)

    def rr(l, r):
        ans = 0
        for i in range(32):
            bit_count = prefix[r][i] - prefix[l - 1][i] if l > 0 else prefix[r][i]
            if bit_count == (r - l + 1):
                ans |= 1 << i
        return ans

    def find(l, k):
        left = l
        right = n
        while left <= right:
            mid = (right + left) // 2
            if rr(l, mid) >= k:
                left = mid + 1
            else:
                right = mid - 1

        if right < l:
            return -1
        return right

    ans = []
    for _ in range(q):
        l, k = map(int, input().split())
        ans.append(find(l, k))
    return ans 


T = 1
T = int(input())

for _ in range(T):
    print(*solve())
