# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

count = 0
def mergeSort(arr, left, right):
    if left == right:
        return [arr[left]]

    midd = (left + right) // 2
    leftPart = mergeSort(arr, left, midd)
    rightPart = mergeSort(arr, midd + 1, right)

    return merge(leftPart, rightPart)


def merge(lefthalf, righthalf):
    global count

    if righthalf[0] < lefthalf[0]:
        righthalf.extend(lefthalf)
        count += 1
        return righthalf
    else:
        lefthalf.extend(righthalf)
        return lefthalf


def solve():
    global count
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        val = mergeSort(nums, 0, n - 1)
        nums.sort()
        if val == nums:
            print(count)
        else:
            print(-1)
        count = 0
        


solve()
