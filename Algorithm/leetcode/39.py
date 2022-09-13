class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(temp, path, candidates):
            if temp > target:
                return
            if temp == target:
                answer.append(path)
                return

            for i, c in enumerate(candidates):
                dfs(temp + c, path + [c], candidates[i:])

        dfs(0, [], candidates)

        return answer

    # 책 풀이
    # 인덱스를 활용한 풀이로 공간복잡도가 낮으며, 간단하고 깔끔
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                answer.append(path)
                return

            # 인덱스를 이용한 순회 및 재귀호출
            for i in range(index, len(candidates)):

                # 만약 0 의 값이 주어지는 입력에 존재한다면 무한 루프에 빠질 수 있으므로, 예외 처리, 해당 문제에서는 존재하지 않으므로 생략가능
                # if candidates[i] == 0: continue
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])

        return answer
