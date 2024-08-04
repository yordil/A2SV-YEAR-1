# Problem: D - Energy Crisis - https://codeforces.com/gym/511242/problem/D

from collections import deque, defaultdict, Counter
from math import gcd, ceil
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations


n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def checker(mid):
    ca = 0
    hold = 0
    for i in range(len(arr)):
        if arr[i] < mid:
            diff = mid - arr[i]
            ca += (diff) * 100 / (100 - k)
        else:
            hold += arr[i] - mid

    if ca > hold:
        return False
    else:
        return True

left = arr[0]
right = arr[-1]

while abs(right - left) > 1e-9:
    mid = (left + right) / 2
    if checker(mid):
        left = mid
    else:
        right = mid

print('{:.9f}'.format(right))


# n, k = list(map(int, input().split()))

# arr  = list(map(int, input().split()))

# arr.sort()


# def checker(mid):
    
#     ca = 0
#     hold = 0
#     for i in range(len(arr)):
#         if arr[i] < mid:
#             diff = mid - arr[i]
#             ca += (diff)*100/(100-k)
#         else:
#             hold += arr[i] - mid

#     if ca > hold:
#         return False
#     else:
#         return True




# # N = int(input())
# # S = input()


# left  = arr[0]
# right = arr[-1]
# ans = float( "-inf")
# mid = 0
# while left <= right:
#     mid = (left +  right) / 2
    
#     flag = checker(mid)
#     if flag:
#         left = mid+ 0.0000001
#     else:
#         right - mid - 0.0000001


# print(left)

     
    

 