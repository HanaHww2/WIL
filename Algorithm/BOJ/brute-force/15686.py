# 치킨 배달 - https://www.acmicpc.net/source/49790025
# 1. 1부터 운영될 수 있는 치킨집의 수의 크기 m까지 모든 조합을 고려했습니다.
#     1. 이 때문에 이터툴즈가 아닌 dfs로 문제를 풀었습니다.
#     2. 그런데 사실 m으로 고정된 크기의 조합으로 문제를 풀었어도 답을 구하는데는 별 지장이 없는 것 같습니다.
# 2. ~~현재 풀이에서 재귀에서 최솟값과의 크기 비교를 통한 탈출 조건을 추가해 줄 수 있을 것 같습니다. (곧 해보겠습니다.)~~
#   ❌ 탐색을 통해서 현재 최솟값이 더 작은 값으로 갱신될 수 있으므로 탈출 조건을 이렇게 작성해서는 안됨

##############################################
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
        # 처음에 이 부분에서 not_visited[:i] + not_visited[i+1:] 와 같이
        # 마지막 매개변수를 전달하는 실수를 했다. (이 실수가 한 두번째가 아니다)
        # 고정된 크기의 조합, 순열을 구하는 로직과 이런 전체 조합, 순열을 구하는 로직을 한 번 정리해도 좋을 것 같다.
        dfs(check_dist(chi, dist[:]), opened + 1, not_visited[i+1:])

answer = 50 * 101
dist = [101]*len(house)
dfs(dist, 0, chick)

print(answer)
