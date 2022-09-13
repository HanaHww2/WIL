import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        answer = []

        def dfs(arr, prev):
            # 리프 노드일 때 결과 추가
            if not arr:
                answer.append(prev[:])
                return

            for i, n in enumerate(arr):
                prev.append(n)
                dfs(arr[:i]+arr[i+1:], prev)
                prev.pop()

        dfs(nums, [])
        return answer

    # 책에서 제공된 풀이
    def permute(self, nums: List[int]) -> List[List[int]]:

        answer = []
        prev = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                answer.append(prev[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)  # 사용한 요소 제외한 나머지 요소들

                prev.append(e)
                dfs(next_elements)
                prev.pop()

        dfs(nums)
        return answer

    # itertools 모듈 활용
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
        # permutaions 메소드가 결과로 튜플의 리스트를 반환하므로, 이를 리스트의 리스트로 변환
        # 그러나 튜플의 리스트 형태도 릿코드에서 정답으로 패스된다.
        # return list(map(list, itertools.permutations(nums)))
