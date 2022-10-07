# https://www.acmicpc.net/problem/2169
# 로봇 조종하기
#
#
import sys, collections

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(y, x, prev, visited):
    global answer
    if y == n - 1 and x == m - 1:
        answer = max(answer, prev)
        return

    for d in move:
        ny, nx = y + d[0], x + d[1]

        if not (-1 < ny < n and -1 < nx < m) or (ny, nx) in visited:
            continue

        dfs(ny, nx, prev + arr[ny][nx], visited | {(ny, nx)})


if __name__ == "__main__":

    move = [(1, 0), (0, 1), (0, -1)]  # dy, dx

    n, m = map(int, input().split(" "))
    arr = []
    for i in range(n):
        arr.append(list(int(x) for x in input().split(" ")))

    # 100 * 1000 * 1000
    dp = [[float("inf")] * (m + 1) for _ in range(n + 1)]
    answer = float("-inf")
    dfs(0, 0, arr[0][0], {(0, 0)})
    print(answer)
