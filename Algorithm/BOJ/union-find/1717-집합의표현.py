# https://www.acmicpc.net/problem/1717
# 집합의 표현
# 464ms
import sys, collections

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
table = dict()


def set_parent(x):
    if x not in table:
        table[x] = x


def find(x):
    if table[x] == x:
        return x
    table[x] = find(table[x])  # 부모의 부모가 존재하는 경우
    return table[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        table[root_x] = root_y  # 이 부분에서 한 방향으로 병합되도록 개선하면 좋을 듯


for _ in range(m):
    op, x, y = map(int, input().split())
    set_parent(x)
    set_parent(y)
    if op == 0:
        union(x, y)
    else:
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")

# 나중에 확인해볼 풀이 https://www.acmicpc.net/source/42009511 232ms
