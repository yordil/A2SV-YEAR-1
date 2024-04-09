# Problem: C - Casino - https://codeforces.com/gym/514644/problem/C

from collections import deque, defaultdict, Counter
from math import gcd, ceil , lcm
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations

power = [2**i for i in range(25)]
powerof3 = [3**i for i in range(22)]
powermul = [power[i]* 3 for i in range(20)]
powermul2 = [powerof3[i]* 2 for i in range(16)]
power = set(power)
powerof3 =set(powerof3)


def solve():
    N = int(input())
    # S = input()

    # row, col = list(map(int, input().split()))

    arr  = list(map(int, input().split()))
    primes = [2 , 3 , 7]
    lc = arr[0]

    lc = max(arr)
    # maxx = max(arr)
    for i in range(N):
            val =arr[i]
            j = 0
            while val > 1:
                if val % primes[0] == 0:
                    val //= primes[0]
                elif val % primes[1] == 0:
                    val //= primes[1]
                else:
                    break
            
            arr[i] = val

    return "Yes"   if len(set(arr)) == 1 else "No"

    # S = list(S)

    # matrix = [list(map(int, input().split())) for _ in range(row)]

    pass


T = 1
# T = int(input())

for _ in range(T):
    print(solve())