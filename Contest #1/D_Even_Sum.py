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


# arrodd = []
# arreven = []
# for i in arr:
#     if i % 2:
#         arrodd.append(i)
#     else:
#         arreven.append(i)
# arrodd.sort()
# arreven.sort()
# total = sum(arrodd) + sum(arreven)
# print(total) if total % 2 == 0 else print(total - arrodd[0])

def myfunc():
    N = input()

    arr = N.split()

    for i in range(len(arr)-1):
        if arr[i] == "?":
            continue
        elif arr[i] ==arr[i+1]:
            return "NO";
    m = "m"
    y = "y"
    c = "c"
    



print(myfunc())


