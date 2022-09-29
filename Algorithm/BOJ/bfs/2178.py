# https://www.acmicpc.net/submit/2178/49839740
# 미로 탐색

# 당연하게도 시간 초과를 먹었다.
# dfs 완탐인 듯...


import sys
import collections


def dfs(y, x, cnt, visited):
    global answer
    if not in_range(y, x) or arr[y][x] == 0 or (y, x) in visited:
        return
    if (y, x) == (n-1, m-1):
        # 목표 도달시 거리 갱신
        answer = min(answer, cnt)
        return

    # 동서남북 이동
    dfs(y+1, x, cnt+1, visited | {(y, x)})
    dfs(y, x+1, cnt+1, visited | {(y, x)})
    dfs(y-1, x, cnt+1, visited | {(y, x)})
    dfs(y, x-1, cnt+1, visited | {(y, x)})


#########################

n, m = 4, 6
arr = ['101111',
       '101010',
       '101011',
       '111011']

arr = [list(map(int, row)) for row in arr]
print(arr)

#########################

# n, m = map(int, sys.stdin.readline().split(' '))
# arr = []
# for i in range(n):
#     arr.append(list(int(x) for x in sys.stdin.readline().strip()))


def in_range(y, x):
    if -1 < y < len(arr) and -1 < x < len(arr[0]):
        return True
    return False


def bfs(y, x):
    global answer
    queue = collections.deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + rd[i], x + cd[i]

            if not in_range(ny, nx) or arr[ny][nx] == 0:
                continue

            if arr[ny][nx] == 1:
                queue.append((ny, nx))
                if arr[ny][nx] > 1 and arr[ny][nx] < arr[y][x] + 1:
                    continue
                arr[ny][nx] = arr[y][x] + 1


# bfs 는 멋있어!!
rd = [1, -1, 0, 0]
cd = [0, 0, 1, -1]

answer = 10e5
# dfs(0, 0, 1, set())
bfs(0, 0)
print(arr[n-1][m-1])
