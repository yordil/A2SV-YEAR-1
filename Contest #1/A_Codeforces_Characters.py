s = "codeforces"

t = int(input())

for _ in range(t):
    x = input()
    if len(x) > 10:
        a = x[0]
        a+=len(x) - 2
        a += x[len(x) - 1]
        print(a)
    else:
        print(x)