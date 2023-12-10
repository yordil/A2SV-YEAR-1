s = "codeforces"

# t = int(input())

# for _ in range(t):
#     x = input()
#     if len(x) > 10:
#         a = x[0]
#         a += str(len(x) - 2)
#         a += x[len(x) - 1]
#         print(a)
#     else:
#         print(x)

N  = int(input())

arr = list(map(int , input().split()))

arrodd = []
arreven = []
for i in arr:
    if i %  2 :
        arrodd.append(i)
    else:
        arreven.append(i)
arrodd.sort()
arreven.sort()
total = sum(arrodd) + sum(arreven)
print(total) if total % 2 == 0 else print(total - arrodd[0])



