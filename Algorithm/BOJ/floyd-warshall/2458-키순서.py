# 키 순서
# https://www.acmicpc.net/problem/2458
#
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[float("inf")] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())  # x < y
    graph[x][y] = 1
    graph[y][x] = -1

for k in range(1, n + 1):  # 거치는 점
    for i in range(1, n + 1):  # 시작점
        for j in range(1, n + 1):  # 끝점

            if graph[j][j] != 0:
                graph[j][j] = 0
            # k를 거쳤을 때의 경로가 더 적은 경로
            if (
                graph[i][k] * graph[k][j] > 0
                and graph[i][j] > graph[i][k] + graph[k][j]
            ):
                graph[i][j] = graph[i][k] + graph[k][j]


def check():
    cnt = 0
    for g in graph[1:]:
        #    all(list(map(lambda x: True if x != float('inft') else False, g[1:])))
        if not g[1:].count(float("inf")):
            cnt += 1
    return cnt


print(check())

# python3 통과 풀이
# https://www.acmicpc.net/source/49859847
# https://www.acmicpc.net/source/19273716
# https://www.acmicpc.net/source/48386399
