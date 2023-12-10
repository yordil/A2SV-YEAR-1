testcase = int(input())

for _ in range(testcase):
    ans = ""
    b = input()
    arr = list(b)
    if len(arr) < 3:
        print(b)
    else:
        i=0
        for i in range(0 ,len(arr) , 2):
            ans += b[i]
        print(ans + b[len(b)-1])
    

        




