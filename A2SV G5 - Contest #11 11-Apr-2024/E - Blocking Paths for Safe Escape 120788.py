# Problem: E - Blocking Paths for Safe Escape - https://codeforces.com/gym/515998/problem/E

import sys


def mapIn(dataType=int):
    return map(dataType, sys.stdin.readline().strip().split())


def lstIn(dataType=int, itType=list):
    return itType(map(dataType, sys.stdin.readline().strip().split()))


def mtrxIn(row, col, dataType=int, itType=list):
    mat = []
    for _ in range(row):
        colo = lstIn(dataType, itType)
        mat.append(colo)
    return mat


def split(arr, dtaType, itType=list):
    temp = str(arr)
    res = [dtaType(i) for i in temp]
    return itType(res)


def solve():
    x, y = mapIn()
    # if x == y == 1:
    grid = []

    for _ in range(x):
        grid.append(split(input(), str))
    dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def inbound(row, col):
        return (0 <= row < x) and (0 <= col < y)

    the_gs = 0

    for i in range(x):
        for j in range(y):
            if grid[i][j] == "G":
                the_gs += 1
            if grid[i][j] == "B":
                for dir in dirc:
                    ci = i + dir[0]
                    cj = j + dir[1]

                    if inbound(ci, cj):
                        if grid[ci][cj] == "G":
                            print("No")
                            return
                        if grid[ci][cj] == "B":
                            continue

                        grid[ci][cj] = "#"
    
    if grid[x - 1][y - 1] == "#" and the_gs > 0:
        print("No")
        return
    elif grid[x - 1][y - 1] == "#" and the_gs == 0:
        print("Yes")
        return

    def dfs():
        stk = [(x - 1, y - 1)]
        visited = set()
        count = 0

        while stk:
            i, j = stk.pop()

            if grid[i][j] == "G":
                count += 1
            elif grid[i][j] == "B":
                return 5000000

            for dir in dirc:
                pi = i + dir[0]
                pj = j + dir[1]

                if inbound(pi, pj) and grid[pi][pj] != "#" and (pi, pj) not in visited:
                    stk.append((pi, pj))
                    visited.add((pi, pj))

        return count

    if the_gs == dfs():
        print("Yes")
    else:
        print("No")


testcase = 1
T = int(input()) if testcase else 1
for _ in range(T):
    solve()
