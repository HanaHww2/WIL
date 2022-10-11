# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로
# 다익스트라
# 너무 꼬아서 생각함;

import sys, collections, heapq

input = sys.stdin.readline

v, e = map(int, input().split())

table = collections.defaultdict(list)
for _ in range(e):
    f, t, w = map(int, input().split())
    table[f].append((w, t))
    table[t].append((w, f))

v1, v2 = map(int, input().split())


def search(start, end):
    dist = [float("inf")] * (v + 1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        w, f = heapq.heappop(q)

        if f == end:
            break

        for des in table[f]:
            nw, nd = des
            if nw + w < dist[nd]:
                dist[nd] = nw + w
                heapq.heappush(q, (nw + w, nd))

    return dist[end]


d1 = search(1, v1) + search(v1, v2) + search(v2, v)
d2 = search(1, v2) + search(v2, v1) + search(v1, v)
mini = min(d1, d2)

print(-1 if mini >= float("inf") else mini)
