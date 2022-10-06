# 욕심쟁이 판다
# https://www.acmicpc.net/problem/1937
# 4
# 14 9 12 10
# 1 11 5 4
# 7 15 2 13
# 6 3 16 8

import sys

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(list(int(x) for x in sys.stdin.readline().split(" ")))

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dist = [[0] * n for _ in range(n)]  # 거리를 표시하는 동시에 방문했음을 나타냄

# 나의 기존 코드
def dfs(y, x):
    result = 1
    for m in move:
        ny, nx = y + m[0], x + m[1]
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] > arr[y][x]:
            temp = dist[ny][nx]
            if temp == 0:
                temp = dfs(ny, nx)
            if temp + 1 > result:
                result = temp + 1

    dist[y][x] = result
    return result


# https://www.acmicpc.net/source/26134536 참고하여 개선
# 그런데 현재 내 코드는 pypy3으로는 메모리 초과가 계속 발생하며,
# python3으로 실행했을 때는 위 코드가 더 속도면에서 낫다.(아마 재귀 호출을 덜해서인듯?)
# def dfs(y, x):
#     if dist[y][x] != 0:
#         return dist[y][x]
#     else:
#         dist[y][x] = 1
#         for m in move:
#             ny, nx = y + m[0], x + m[1]
#             if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] > arr[y][x]:
#                 temp = dfs(ny, nx) + 1
#                 dist[y][x] = max(temp, dist[y][x])
#     return dist[y][x]

# 2.
# def dfs(y, x):
#     dist[y][x] = 1
#     for m in move:
#         ny, nx = y + m[0], x + m[1]
#         if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] > arr[y][x]:
#             temp = dist[ny][nx]
#             if temp == 0:
#                 temp = dfs(ny, nx)
#             dist[y][x] = max(dist[y][x], temp + 1)

#     return dist[y][x]


answer = 1

# dfs 가 필요한 것 같다!
for i in range(n):
    for j in range(n):
        if dist[i][j] == 0:
            dfs(i, j)

        if dist[i][j] > answer:
            answer = dist[i][j]

print(answer)
