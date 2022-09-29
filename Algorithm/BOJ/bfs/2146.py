# 다리 만들기
# https://www.acmicpc.net/problem/2146

n = 10
arr = [
    "1 1 1 0 0 0 0 1 1 1",
    "1 1 1 1 0 0 0 0 1 1",
    "1 0 1 1 0 0 0 0 1 1",
    "0 0 1 1 1 0 0 0 0 1",
    "0 0 0 1 0 0 0 0 0 1",
    "0 0 0 0 0 0 0 0 0 1",
    "0 0 0 0 0 0 0 0 0 0",
    "0 0 0 0 1 1 0 0 0 0",
    "0 0 0 0 1 1 1 0 0 0",
    "0 0 0 0 0 0 0 0 0 0",
]
arr = [list(map(int, x.split(" "))) for x in arr]
###################################################################

import collections
import sys

# n = int(sys.stdin.readline())
# arr = []

# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split(' '))))


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def in_range(y, x):
    if -1 < y < len(arr) and -1 < x < len(arr[0]):
        return True
    return False


# 주변에 하나라도 바다가 있다면,
def near_sea(y, x):
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if in_range(ny, nx) and is_sea(ny, nx):
            return True
    return False


# bfs 로직!
# 처음엔 플래그를 두고 바다를 건넌 건지 확인해보려 했으나 실패
# 다른 사람들의 풀이를 확인 -> 섬들을 먼저 숫자 등으로 구분 짓고, 바다를 건너는 거리를 계산하는 로직으로 구현
def search(y, x):
    # print(y, x, cnt)
    global answer

    queue.append((y, x, False))
    while queue:
        y, x, f = queue.popleft()

        if arr[y][x] > answer:
            continue

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if not in_range(ny, nx) or arr[ny][nx] == -1:
                continue

            new_f = f
            # 바다이고, 섬에서 출발한 경우, 거리 계산
            if is_sea(ny, nx) and f:
                temp = 2
                if arr[y][x] != -1:
                    temp = arr[y][x] + 1
                if arr[ny][nx] == 0 or arr[ny][nx] > temp:

                    arr[ny][nx] = temp

            # 대륙이고,
            if arr[ny][nx] == 1:
                if f and arr[y][x] > 1:  # 바다를 건너 온 경우
                    # 거리 최솟값 확인
                    answer = min(answer, arr[y][x])
                    print(answer)
                    new_f = not f
                else:
                    # 바다를 인접한 경우
                    if near_sea(y, x):
                        new_f = True
                arr[ny][nx] = -1  # 방문했음 표시

            queue.append((ny, nx, new_f))


queue = collections.deque()
answer = 200
search(0, 0)
print(answer)
