import sys, collections

input = sys.stdin.readline

n, m = [int(input()) for _ in range(2)]
dist = [[float("inf")] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    s, d, w = map(int, input().split())
    if dist[s][d] > w:
        dist[s][d] = w


for k in range(1, n + 1):  # 거치는 점
    for i in range(1, n + 1):  # 시작점
        for j in range(1, n + 1):  # 끝점

            if dist[j][j] != 0:
                dist[j][j] = 0
            # k를 거쳤을 때의 경로가 더 적은 경로
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# python3 인터프리터에서는 위가 약소하게 더 빠르다. 별 차이 x
# pypy3은 확실히 빠르나, 메모리를 많이 먹는다. 위 아래 둘 다 속도 메모리 비슷함
# for i in range(1, n + 1):
#     print(*map(lambda x: 0 if x == float("inf") else x, dist[i][1:]))
for d in dist[1:]:
    for c in d[1:]:
        if c == float("inf"):
            sys.stdout.write("0 ")
        else:
            sys.stdout.write(str(c) + " ")
    sys.stdout.write("\n")
