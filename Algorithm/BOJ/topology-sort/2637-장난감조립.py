# 장난감 조립
# https://www.acmicpc.net/problem/2637

import heapq
import sys, collections

input = sys.stdin.readline

n, m = [int(input()) for _ in range(2)]


graph = collections.defaultdict(list)
pre_table = collections.defaultdict(list)
indegree = [0] * (n + 1)

for i in range(m):
    x, y, k = map(int, input().split())
    graph[x].append((y, k))
    indegree[y] += 1


def topology_sort():
    answer = []
    result = [0] * (n + 1)  # 알고리즘 수행 결과를 담을 리스트
    q = collections.deque()  # 큐 기능을 위한 deque 라이브러리 사용

    # 완제품이 진입노드
    q.append(n)
    result[n] = 1

    while q:
        # 큐에서 원소 꺼내기
        s = q.popleft()

        if not graph[s]:
            heapq.heappush(answer, (s, result[s]))
            continue
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i, c in graph[s]:
            indegree[i] -= 1
            result[i] += c * result[s]

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    return answer


# answer = sorted(topology_sort(), key=lambda x: x[0])
# print(answer)
answer = topology_sort()
while answer:
    print(*heapq.heappop(answer))
