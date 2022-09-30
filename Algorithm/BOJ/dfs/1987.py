# https://www.acmicpc.net/problem/1987
# 알파벳
# 계속 시간 초과로 실패했는데 로직의 문제라기 보단 파이썬의 최적화 문제..
# 대부분 bfs로 해결했다.
# + ord()로 문자 비교 대신 숫자 비교를 활용 (아스키 코드)
#########################

# r, c = 2, 4
# arr = ["101111", "101010", "101011", "111011"]

# arr = [list(map(int, row)) for row in arr]
# 
# 3 6
# HFDFFB
# AJHGDH
# DGAGEH
# 
#########################

import sys

n, m = map(int, sys.stdin.readline().split(" "))
arr = []
for i in range(n):
    arr.append(list(x for x in sys.stdin.readline().strip()))  # 문자열 조작하지 않음
print(arr)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def in_range(y, x):
    if -1 < y < n and -1 < x < m:
        return True
    return False


# 집합을 전달하는 게 아니라 카운팅을 전달하는 식으로 개선
def dfs(y, x, cnt):
    global answer

    # if not in_range(y, x) or visited[y][x] == 1:
    #     return
    # visited[y][x] = 1
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if in_range(ny, nx):
            if arr[ny][nx] in checked:
                answer = max(answer, cnt)
                continue
            else:
                checked.add(arr[ny][nx])
                dfs(ny, nx, cnt + 1)
                checked.remove(arr[ny][nx])
    # visited[y][x] = 0


# visited = [[0] * m for _ in range(n)]
answer = 0
checked = {arr[0][0]}
dfs(0, 0, 1)  # , visited)
print(answer)
