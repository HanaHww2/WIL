# https://www.acmicpc.net/problem/1976
# 여행가자
# 76ms
import sys

input = sys.stdin.readline


def set_parent(x):
    if x not in parent:
        parent[x] = x


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):  # 유니온에서 불필요한 로직이 있는 것 같은데...다시 살펴보기
    _x = find(x)
    _y = find(y)

    if _x > _y:
        parent[_x] = _y
    elif _x < _y:
        parent[_y] = _x


n, m = [int(input()) for _ in range(2)]
graph = [[0] * (n + 1)]
parent = dict()

for i in range(1, n + 1):
    # graph.append( [0] + list(map(int, input().split())) )
    temp = [0] + list(map(int, input().split()))
    set_parent(i)

    for j in range(i + 1, n + 1):
        if temp[j] == 1:  # 길이 연결되어 있으면,
            set_parent(j)
            union(j, i)


# 방문할 도시
visiting = list(map(int, input().split()))
temp = find(visiting[0])
for v in visiting[1:]:
    if temp != find(v):
        print("NO")
        break
else:
    print("YES")

# 참고해보기 https://www.acmicpc.net/source/18199880 64ms
