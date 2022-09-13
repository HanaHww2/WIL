class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        def dfs(nums, arr):
            if not nums:
                return
            for i, n in enumerate(nums):
                arr.append(n)
                answer.append(arr[:])
                dfs(nums[i+1:], arr)
                arr.pop()

        dfs(nums, [])

        return answer

    # 책 풀이
    # 인덱스를 활용, 깔끔한 풀이
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(index, path):

            answer.append(path)

            # 종료 조건이 없어도 index가 len(nums)와 같은 크기가 되면, 자동 종료된다.
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        dfs(0, [])

        return answer
