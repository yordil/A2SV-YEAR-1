from math import ceil
def solve():
    N = int(input())
    arr =  list(map(int , input().split()))
    x = 0
    for i in range(len(arr) -1):
        if arr[i] > arr[i+1]:
            temp = ceil((arr[i] + arr[i+1]) / 2)
            x = max(x , temp )
    for i in range(len(arr)):
        arr[i] = abs(x-arr[i])
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return -1
           
    
    return x
       
testcase = int(input())
for _ in range(testcase):
    print(solve())
