# 2468 안전 영역
# https://www.acmicpc.net/problem/2468
#############################
# 7
# 9 9 9 9 9 9 9
# 9 2 1 2 1 2 9
# 9 1 8 7 8 1 9
# 9 2 7 9 7 2 9
# 9 1 8 7 8 1 9
# 9 2 1 2 1 2 9
# 9 9 9 9 9 9 9
#
# 70퍼에서 틀려서 찾아본 추가 테케
# 최소 안전영역은 0이 아니라 1이 되어야 한다.
# 5
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
#
# 2 <= n <=100
# 1 <= 높이 <= 100
#############################
### 70 퍼센트에서 틀려버림..
import sys, copy

sys.setrecursionlimit(int(10e6))
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split(" "))))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def in_range(y, x):
    if -1 < y < n and -1 < x < n:
        return True
    return False


def get_min_max():

    a = min(list(map(min, arr)))
    b = max(list(map(max, arr)))
    return a, b


def dfs(y, x):

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if in_range(ny, nx) and copied[ny][nx] > h:
            copied[ny][nx] = h  # 방문지 표시
            dfs(ny, nx)


# 비 높이 최소 0 이라는 말은 없었잖아 ㅡ,ㅡ  최소가 항상 1이다.
answer = 1
a, b = get_min_max()
# 높이 "이하"로 물에 잠긴다. 최대값 b이면 전체 잠기는 상태
for h in range(a, b):
    # arr 에서 물에 잠기는 땅 조작하기

    # 조작 방식...고민
    # map()으로 감싸면서 새로운 배열 생성
    # 매번 전체를 탐색하고 새 배열을 만들어서 낭비 같음;
    # copied = list(list(map(lambda x: 0 if x <= h else x, r)) for r in arr)
    # 선탐색할 필요없음, 높이 기준으로 dfs 수행
    copied = copy.deepcopy(arr)
    cnt = 0
    # 안전지대 탐색
    for i in range(n):
        for j in range(n):
            if copied[i][j] > h:
                cnt += 1
                dfs(i, j)

    answer = max(answer, cnt)

print(answer)
