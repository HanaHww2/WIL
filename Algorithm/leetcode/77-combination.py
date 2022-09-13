import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(start, prev):
            if len(prev) == k:
                answer.append(prev[:])
                return

            for i in range(start, n+1):
                prev.append(i)
                dfs(i+1, prev)
                prev.pop()
        dfs(1, [])

        return answer

    # 반복문 최적화하여 개선
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(start, cnt, prev):
            if len(prev) == k:
                answer.append(prev[:])
                return

            # 만들어야 하는 조합의 길이를 고려하여 반복문 구현
            # 주어진 숫자 전체를 반복하지 않고, 앞으로 수행될 반복문을 고려
            # 예를 들어 [1, 2, 3, 4, 5] 에서 길이가 3인 조합을 생성하려고 하면,
            # 1~5까지 반복문을 도는 것이 아니라, 1~3까지, 2~4까지 3~5까지 순으로 반복문 작성하여 최적화
            # 남은 문자열의 길이(cnt-1) 고려
            for i in range(start, n+1-(cnt-1)):
                prev.append(i)
                dfs(i+1, cnt-1, prev)
                prev.pop()

        dfs(1, k, [])

        return answer

    # itertools 활용
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))
