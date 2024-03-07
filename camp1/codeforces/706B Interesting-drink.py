from bisect import bisect_left
from collections import deque
from collections import defaultdict
from collections import Counter



def solve():
    # matrix = [list(map(int, input().split())) for _ in range(row)]
    # row, col = list(map(int, input().split()))
    # S = input()
    N = int(input())
    arr  = list(map(int, input().split()))
    q  = int(input())
    days = []
    for i in range(q):
        x = int(input())
        days.append(x)
    
    arr.sort()
    # days.sort()
    ans = []
    sett = Counter(arr)


    for i in range(q):
        temp = bisect_left(arr, days[i])
        if days[i] in sett:
            ans.append(temp+ sett[days[i]])
        else:
            ans.append(temp)

    for an in ans:
        print(an) 

    pass


T = 1
# T = int(input())

for _ in range(T):
    solve()
