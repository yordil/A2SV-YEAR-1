from collections import deque
from collections import defaultdict
from collections import Counter
from math import ceil
 
 
def solve():
    N = int(input())
    arr  = list(map(int, input().split()))
    speed  = list(map(int, input().split()))
 
    long = 10e9 +1
    flag = 1 / 1000000
    
    start  = 0 
    end = ceil((max(arr) - min(arr) ) / 2)
    answer = end  + 1 
 
    while start + flag  <= end:
        
        midd = ( start + end) / 2
        minall = -10000000
        maxall = long
 
        for i in range(len(arr)):
            
            minncover = arr[i] - ( midd * speed[i] )
            maxxcover =  arr[i] +  (midd * speed[i] )
            
            minall = max(minall , minncover) 
            maxall = min(maxall , maxxcover)
 
        
        # print(minall , maxall)
    
        if minall >= maxall:
            start = midd + flag
            answer = min(answer , midd)
        else:
            end = midd - flag
        # print(midd)
        # print(midd)
    return end
 
 
        
        
 
 
    # pass
 
 
T = 1
# T = int(input())
 
for _ in range(T):
   print(solve())