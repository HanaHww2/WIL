# 친구 네트워크
# https://www.acmicpc.net/problem/4195
# 참고 풀이 https://assaeunji.github.io/python/2020-05-05-bj4195/
################################################################
# 352ms 로직은 위와 동일한데 위 코드는 8000ms가 소요(input() 메소드 차이 같다.)
################################################################
import sys, collections

input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] += number[root_y]


def check_input(m):

    for _ in range(m):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a, b)
        print(number[find(a)])


n = int(input())  # 전체 테케 수
answer = []
for _ in range(n):
    m = int(input())  # 친추 횟수
    parent = {}
    number = {}
    check_input(m)
