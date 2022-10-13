# https://www.acmicpc.net/problem/3665
# 최종 순위
import sys, collections

input = sys.stdin.readline

n = int(input())  # 전체 테케 수


def organize_input():

    t = int(input())

    last = [0] * (t + 1)
    for i, x in enumerate(map(int, input().split())):

        last[x] = i + 1

    indegree = [0] * (t + 1)

    change = collections.defaultdict(list)
    change_cnt = int(input())

    for _ in range(change_cnt):
        x, y = map(int, input().split())

        # 현 순위 기준으로 테이블 입력
        # 무조건 작은 값(순위가 높은 값)이 키가 되도록 설정한다.
        if last[x] > last[y]:
            change[y].append(x)
            indegree[x] += 1
        else:
            change[x].append(y)
            indegree[y] += 1

    def topology_sort():
        q = collections.deque()

        # 변화가 있는 값 중
        for i in change.keys():
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()

            # 순위가 내려가는(+커지는) 경우 검증
            for x in change[node]:
                last[node] += 1
                last[x] -= 1
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
        return last

    return topology_sort()


answer = []
for _ in range(n):
    answer.append(organize_input())

for a in answer:
    t = len(a)
    result = [0] * t
    for i, order in enumerate(a[1:], start=1):
        # 순위가 겹치는, 꼬이는 경우가 발생 -> 임파서블
        if result[order] != 0 or order > t - 1 or order < 1:
            print("IMPOSSIBLE")
            break
        result[order] = i

    else:
        print(*result[1:])

# 풀긴 풀었는데...^,^ 문제 케이스에 대한 이해는 아직...좀 덜 되고 있다.
# 애초에 ? 는 답으로 나올 수 없다.
# (그래프를 어떻게 그리느냐에 따라) IMPOSSIBLE이 발생하는 경우는 그래프 내 싸이클이 있는 경우로 볼 수 있다고 한다.
# https://my-coding-notes.tistory.com/307?category=976963
