def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    if len(arr) < 3:
        return "NO"
    else:
        for i in range(len(arr)):
            temp = int(arr[i])
            for j in range(i + 2, len(arr)):
                if arr[j] == temp:
                    return "YES"

        return "NO"


testcase = int(input())
for _ in range(testcase):
    print(solve())


# # improved solution O(N) - > both space and Time
# def solve():
#     N = int(input())
#     arr = list(map(int, input().split()))
#     if len(arr) < 3:
#         return "NO"
#     else:
#         mydict = {}
#         for i in range(len(arr)):
#             if arr[i] in mydict:
#                 if i - mydict[arr[i]] >= 2:
#                     return "YES"
#             else:
#                 mydict[arr[i]] = i

#         return "NO"


# testcase = int(input())
# for _ in range(testcase):
#     print(solve())
