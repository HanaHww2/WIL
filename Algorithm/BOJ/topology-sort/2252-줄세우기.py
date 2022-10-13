# 줄세우기
# https://www.acmicpc.net/problem/2252

import sys, collections

input = sys.stdin.readline
n, m = map(int, input().split())

graph = collections.defaultdict(list)
indegree = [0] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())  # x < y
    graph[x].append(y)
    indegree[y] += 1


def topology_sort():
    result = []  # 결과를 담을 리스트
    q = collections.deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 큐에서 원소 꺼내기
        s = q.popleft()
        result.append(s)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[s]:
            indegree[i] -= 1

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    return result


result = topology_sort()
print(*result)
