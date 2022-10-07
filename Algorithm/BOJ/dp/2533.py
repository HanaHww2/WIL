# 사회망 서비스(SNS)
# https://www.acmicpc.net/problem/2533
# 수정전 4756ms 수정후 4268ms
###
# 참고
# https://www.acmicpc.net/source/48967210 dfs 3424ms python3
# https://www.acmicpc.net/source/45478151 bfs 큐로 풀이 2056ms pypy3
#######################################################
import sys, collections

sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
table = collections.defaultdict(list)

for _ in range(n - 1):
    p, c = map(int, sys.stdin.readline().split(" "))
    table[p].append(c)
    table[c].append(p)

dp = [0] * (n + 1)
visited = [0] * (n + 1)
# early = [0] * (n + 1)

# 자신이 얼리어답터가 아닌데, 얼리어답터가 아닌 자식 노드가 존재한다면 +1
# 리프노드부터 체크해야 하므로 dfs
def check_fr(node):
    global answer

    visited[node] = 1
    if not table[node]:
        return True  # 더 이상 탐색할 노드 없는 리프노드.

    temp = 0
    for child in table[node]:  # 트리 탐색

        if visited[child]:
            continue

        # 얼리어답터 유무는 어떻게 체크하나 배열 혹은 리턴 True
        if check_fr(child) and dp[node] == 0:
            temp = 1
            # dp[node] = 1
    answer += temp
    return False if temp == 1 else True


answer = 0
check_fr(1)
print(answer)
# print(sum(dp)) sum에서 시간 소요되는 거 같아 수정
