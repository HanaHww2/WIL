# 트리와 쿼리
# https://www.acmicpc.net/problem/15681
import sys, collections
sys.setrecursionlimit(10**6)
n, r, q = map(int, sys.stdin.readline().split(" "))

table = collections.defaultdict(list)
query = []

for _ in range(n - 1):
    p, c = list(map(int, sys.stdin.readline().split(" ")))
    table[p].append(c)
    table[c].append(p)

query = [int(sys.stdin.readline()) for _ in range(q)]

dp = [0] * (n + 1)

# 트리 탐색
def dfs(node, prev):
    if not table[node]:
        dp[node] = 1
        return 1

    cnt = 1
    for child in table[node]:
        if child == prev:
            continue
        if dp[child] == 0:
            cnt += dfs(child, node)
        else:
            cnt += dp[child]

    dp[node] = cnt
    return cnt


dfs(r, 0)
for i in query:
    print(dp[i])
