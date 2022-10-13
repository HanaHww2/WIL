# https://www.acmicpc.net/problem/2169
# 로봇 조종하기
#
# 단순 재귀 dfs 구현시 시간초과
import sys, collections

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dp 배열을 어떻게 만들어줘야할지 모르겠어서 그냥 dfs로 풀었었다.
# 3차원 배열 dfs 이용한다!
# https://peisea0830.tistory.com/m/107


def dfs(y, x, moved):

    if y == n - 1 and x == m - 1:
        return arr[y][x]

    for d in range(3):
        # 이전 방향과 반대인 경우, 재방문 방지
        if (moved == 2 and d == 1) or (moved == 1 and d == 2):
            continue

        ny, nx = y + move[d][0], x + move[d][1]

        if not (-1 < ny < n and -1 < nx < m):
            continue

        if dp[ny][nx][d] == float("-inf"):
            dp[y][x][moved] = max(dp[y][x][moved], dfs(ny, nx, d) + arr[y][x])
        else:
            dp[y][x][moved] = max(dp[y][x][moved], dp[ny][nx][d] + arr[y][x])

    return dp[y][x][moved]


if __name__ == "__main__":

    move = [(1, 0), (0, 1), (0, -1)]  # dy, dx 0, 1, 2 방향 존재

    n, m = map(int, input().split(" "))
    arr = []
    for i in range(n):
        arr.append(list(int(x) for x in input().split(" ")))

    # 100 * 1000 * 1000
    dp = [[[float("-inf")] * 3 for _ in range(m)] for _ in range(n)]

    print(dfs(0, 0, 0))
