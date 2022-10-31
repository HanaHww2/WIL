# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 전력망 둘로 나누기
#
import collections


def solution(n, wires):
    answer = 100
    # 유니온 파인드 방식으로도 풀어보기

    # 메모이제이션?
    # 각 노드의 최소 서브트리 크기를 저장해두어서
    # 최적화를 할 수 있을 거 같은데
    def count(parent):
        temp = 1
        for d in graph[parent]:
            if visited[d] == 1:
                continue
            visited[d] = 1
            temp += count(d)

        return temp

    # 그래프 생성
    graph = collections.defaultdict(set)
    for x, y in wires:
        graph[x].add(y)
        graph[y].add(x)

    # 루트 노드 지정해서 계산
    for (x, y) in wires:
        visited = [0] * (n + 1)
        visited[x] = visited[y] = 1
        temp = abs(count(x) - count(y))
        if answer > temp:
            answer = temp

    return answer


# 다른 사람 풀이
# def solution(n, wires):
#     ans = n
#     for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
#         s = set(sub[0])

#         # 교집합이 존재하지 확인하고
#         # 서브트리를 갱신하며 크기를 비교하는 방식
#         [s.update(v) for _ in sub for v in sub if set(v) & s]
#         ans = min(ans, abs(2 * len(s) - n))
#     return ans
