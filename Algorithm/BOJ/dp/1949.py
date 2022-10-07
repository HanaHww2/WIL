# 우수마을
# https://www.acmicpc.net/problem/1949

import sys, collections

n = int(sys.stdin.readline())

arr = [0] + list(map(int, sys.stdin.readline().split(" ")))

table = collections.defaultdict(list)
for _ in range(n - 1):
    p, c = list(map(int, sys.stdin.readline().split(" ")))
    table[p].append(c)
    table[c].append(p)

dp = [[-1] * (n + 1) for _ in range(2)]

# 이전에 우수 마을이었으면 우수마을이 될 수 없음
# 인접한 마을과 자기 자신 중 적어도 하나가 우수마을이어야 함.
def dfs(node, prev, selected):

    if dp[selected][node] != -1:
        return dp[selected][node]

    temp = 0

    for child in table[node]:
        if prev == child:
            continue

        if dp[not selected][child] == -1:
            dp[not selected][child] = dfs(child, node, not selected)

            # 직전 노드가 선택되었으므로,
            # 현재 노드는 선택 불가
            # 더하여 다음 노드까지 선택되지 않아도 된다.
            if not selected:
                dp[not selected][child] = max(
                    dp[not selected][child], dfs(child, node, selected)
                )

        temp += dp[not selected][child]

    # 자기 자신을 선택
    if selected:
        temp += arr[node]
    dp[selected][node] = temp
    return dp[selected][node]


print(max(dfs(1, 0, 1), dfs(1, 0, 0)))
