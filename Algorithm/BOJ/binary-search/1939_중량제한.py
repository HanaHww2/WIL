# 중량제한
# https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-1939%EB%B2%88-%EC%A4%91%EB%9F%89%EC%A0%9C%ED%95%9C-1-Python
# https://www.acmicpc.net/problem/1939
#
import sys, collections

input = sys.stdin.readline
n, m = map(int, input().split())  # 섬 갯수, 다리 갯수

graph = collections.defaultdict(list)
for _ in range(m):
    x, y, l = map(int, input().split())
    graph[x].append((y, l))
    graph[y].append((x, l))


def possible_bfs(mid):
    visited[start] = 1
    q = collections.deque()
    q.append(start)

    while q:
        now = q.popleft()
        if now == end:
            return True
        for nd, limit in graph[now]:
            if visited[nd] == 0 and mid <= limit:
                q.append(nd)
                visited[nd] = 1

    return False


start, end = map(int, input().split())
low, high = 1, 1000000000

while low <= high:
    visited = [0] * (n + 1)
    mid = (low + high) // 2
    if possible_bfs(mid):  # 목적지까지 도달이 가능하다면 low를 올림
        low = mid + 1
    else:  # 목적지까지 불가능하다면 high를 내림
        high = mid - 1

# 정답이 항상 존재하므로
print(high)


## TODO 다익스트라 풀이해보기