# https://www.acmicpc.net/problem/1753
# 최단경로

import sys, collections, heapq

input = sys.stdin.readline
v, e = map(int, input().split())
s = int(input())
table = collections.defaultdict(list)
for _ in range(e):
    f, t, w = map(int, input().split())
    table[f].append((w, t))
    # table[t].append((w, f))


def dijkstra(src):
    dist = [float("inf")] * (v + 1)
    dist[src] = 0
    queue = [(0, src)]

    while queue:
        w, f = heapq.heappop(queue)

        if w > dist[f]:
            continue
        # dist[f] = w

        for des in table[f]:
            nw, nd = des
            if dist[nd] > w + nw:
                dist[nd] = w + nw
                heapq.heappush(queue, (w + des[0], des[1]))
    return dist


dist = dijkstra(s)
for i in range(1, v + 1):
    print("INF" if dist[i] == float("inf") else dist[i])
