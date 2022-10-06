# 이동하기
# https://www.acmicpc.net/problem/11048
#
import sys, collections, heapq

n, m = map(int, sys.stdin.readline().split(" "))

arr = []
for i in range(n):
    arr.append(list(int(x) for x in sys.stdin.readline().split(" ")))

move = [(1, 0), (0, 1), (1, 1)]
dp = [[0] * (m + 1) for _ in range(n + 1)]

# 참고 https://resilient-923.tistory.com/293
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + arr[i - 1][j - 1]
print(dp[n][m])

# 역시 bfs로는 96퍼에서 틀렸는데 뭘까 ㅡ,ㅡ 대각방향 이동 탓인가??..
# 다익스트라는 그리디 속성도 가지고 있으므로 가능한...
# 이문제도 그리다 속성을 가졌다면 최대 힙으로 구현 가능할까?
# 안되는 거 같음. 대각방향이...문제인가...ㅠ
# def bfs(y, x):

#     queue = collections.deque()
#     queue.append((y, x))
#     # queue = [(-arr[y][x], y, x)]
#     dp[y][x] = arr[y][x]

#     while queue:
#         y, x = queue.popleft()
#         # pre, y, x = heapq.heappop(queue)
#         # pre *= -1
#         pre = dp[y][x]
#         # if y == n - 1 and x == m - 1:
#         #     break
#         for d in move:
#             ny, nx = y + d[0], x + d[1]
#             if not (-1 < ny < n and -1 < nx < m):
#                 continue
#             if arr[ny][nx] + pre > dp[ny][nx]:
#                 dp[ny][nx] = arr[ny][nx] + pre
#                 queue.append((ny, nx))
#                 # heapq.heappush(queue, (-dp[ny][nx], ny, nx))

#     return dp[n - 1][m - 1]

# print(bfs(0, 0))
