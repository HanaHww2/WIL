# 게임개발
# https://www.acmicpc.net/problem/1516

import sys, collections

input = sys.stdin.readline

n = int(input())

graph = collections.defaultdict(list)
pre_table = collections.defaultdict(list)
indegree = [0] * (n + 1)
time = [0] * (n + 1)

for idx in range(1, n + 1):
    temp = list(map(int, input().split()))
    time[idx] = temp[0]

    i = 1
    while temp[i] != -1:
        graph[temp[i]].append(idx)
        pre_table[idx].append(temp[i])
        indegree[idx] += 1
        i += 1


def topology_sort():
    result = [0] * (n + 1)  # 알고리즘 수행 결과를 담을 리스트
    q = collections.deque()  # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append((i, time[i]))

    while q:
        # 큐에서 원소 꺼내기
        s, w = q.popleft()

        result[s] = w

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[s]:
            indegree[i] -= 1

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                # 앞서 걸린 시간 중 최댓값을 가져온다...
                temp = 0
                for p in pre_table[i]:
                    temp = max(temp, result[p])

                q.append((i, temp + time[i]))
    return result[1:]


result = topology_sort()
for x in result:
    print(x)
