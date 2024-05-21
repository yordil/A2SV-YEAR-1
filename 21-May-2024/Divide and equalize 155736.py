# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import Counter
import sys


def Int():
    return int(sys.stdin.readline().strip())


def arr():
    return list(map(int, sys.stdin.readline().strip().split()))


def String():
    return sys.stdin.readline().strip()


r = lambda n: range(n)


def PrimeFactorization(n):
    res = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            res.append(d)
            n //= d
        d += 1
    if n > 1:
        res.append(n)
    return res


def solve():

    N = int(input())

    myarr = arr()
    if len(set(myarr)) == 1:return "YES"
    newarr = []

    lenn = set()
    for i in r(N):
        newarr.append(PrimeFactorization(myarr[i]))
        lenn.add(len(newarr[-1]))
    counter = Counter()
    for e in newarr:
        for i in r(len(e)):
            counter[e[i]] += 1
    for key , value in counter.items():
        if value % N != 0:
            return "NO"
    return "YES"

            
   
    

    pass


T = 1
T = int(input())

for _ in range(T):
    print(solve())
