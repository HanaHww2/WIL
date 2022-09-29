# 2638 치즈
# https://www.acmicpc.net/problem/2638
# 32540KB, 140ms
n, m = 8, 9
arr = [
    "0 0 0 0 0 0 0 0 0",
    "0 0 0 1 1 0 0 0 0",
    "0 0 0 1 1 0 1 1 0",
    "0 0 1 1 1 1 1 1 0",
    "0 0 1 1 1 1 1 0 0",
    "0 0 1 1 0 1 1 0 0",
    "0 0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0 0",
]

###################################
import sys
import collections


arr = [list(map(int, x.split(" "))) for x in arr]

# n, m = map(int, sys.stdin.readline().split(' '))
# arr = []
# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split(' '))))


def in_range(y, x):
    if (-1 < y < n) and (-1 < x < m):
        return True
    return False


def is_melting(ny, nx):
    cnt = 0
    for d in range(4):
        nny = ny + dy[d]
        nnx = nx + dx[d]
        if in_range(nny, nnx) and arr[nny][nnx] == 2:
            cnt += 1
        if cnt > 1:
            return True
    return False


# 아래 작성 로직은 다른 사람 풀이를 참고하여 조금 변형했다.
# 1. 모서리이면서, 1이 아닌 경우 외부 공기 2라고 설정한다.
# 2. 이 외부 공기와 닿은 공간은 모두 외부 공기로 갱신한다.
# 3. 치즈를 순회하면서 외부 공기와 2개 이상 닿아 있으면
# 4. 이를 삭제한다. time +1
def set_env(y, x, visited):
    queue.append((y, x))
    melted = set()

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if not in_range(ny, nx):
                continue

            # 외부 공기와 2면 이상 맞닿은 치즈 발견
            if arr[ny][nx] == 1 and is_melting(ny, nx):
                melted.add((ny, nx))
                continue

            # 외부 공기라면
            if arr[ny][nx] == 0:
                arr[ny][nx] = 2
                queue.append((ny, nx))  # 외부 공기만 큐에 담아준다.

            # queue.append((ny, nx))  # 처음에는 여기서 좌표를 큐에 담았는데 무한 루프를 돌게 된다.
            # 방문지로 마킹하지 않기 때문에
            # ~와는 별개로 큐에 담아서 추가 탐색을 할 이유가 없다.

    return melted  # 외부 공기와 닿은 치즈 반환


def search(r, c):
    cnt = -1
    visited = [[0] * m for _ in range(n)]
    # visited = set()
    melted = {(r, c)}

    # 4번 로직 수행
    while melted:

        cnt += 1
        # 멜티드 치즈를 담는 그릇을 셋으로 변경해서 중복으로
        # 큐에 담기는 것을 방지한다.
        # 이 변경을 하고나서 제출 중반부에서 시간초과난 것을 해결했다.
        for (y, x) in melted:
            arr[y][x] = 2  # 공기로 변경
            queue.append((y, x))
        r, c = melted.pop()  # 녹은 치즈 위치에서 다시 시작
        # 2 부터 다시 반복
        melted = set_env(r, c, visited)

    return cnt


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
queue = collections.deque()
answer = search(0, 0)
print(answer)
