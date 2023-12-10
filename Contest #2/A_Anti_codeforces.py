testcase = int(input())
c = "codeforces"
for _ in range(testcase):
    s = input()
    counter = 0
    for i in range(len(s)):
        if s[i] != c[i]:
            counter +=1
    print(counter)
