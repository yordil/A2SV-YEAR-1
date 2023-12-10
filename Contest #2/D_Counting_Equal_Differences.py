testcase = int(input())

for _ in range(testcase):
    N = int(input())
    arr = list(map(int , input().split()))
    prefixmap = {}
    counter = 0
    
    for i in range(len(arr)):
        target = arr[i] - i
        if target in prefixmap:
            counter += prefixmap[target]
            prefixmap[target] +=1
        else:
            prefixmap[target] = 1
    print(counter)
