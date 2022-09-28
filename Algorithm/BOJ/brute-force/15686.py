# 치킨 배달 - https://www.acmicpc.net/source/49790025
# n, m = 5, 3
# arr = [[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [
#     0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]]
# 32468KB 288ms
# 100ms 대의 코드가 많이 있다.

import sys
import itertools
import collections

n, m = map(int, sys.stdin.readline().split(' '))
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split(' '))))

house = []
chick = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chick.append((i, j))


def check_dist(chi, dist):
    for i, h in enumerate(house):
        temp = abs(chi[0]-h[0]) + abs(chi[1]-h[1])
        if dist[i] > temp:
            dist[i] = temp  # 더 작은 결과라면 갱신
    return dist

# m 이하의 모든 조합을 고려


def dfs(dist, opened, not_visited):
    global answer
    if opened > m:
        return
    answer = min(answer, sum(dist))
    for i, chi in enumerate(not_visited):
        dfs(check_dist(chi, dist[:]), opened + 1,
            not_visited[i+1:])


answer = 50 * 101
dist = [101]*len(house)
dfs(dist, 0, chick)

print(answer)
