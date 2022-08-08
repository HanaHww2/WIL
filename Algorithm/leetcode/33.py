class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 조건에 따른 이진 검색
        # 조건 분기에서 막혀서, 다른 사람의 풀이를 참고했다.ㅠ
        def binary_search(left, right):

            if left > right:
                return -1

            mid = (left + right)//2

            # 미드값이 타겟인 경우
            if nums[mid] == target:
                return mid

            # left에서 mid까지 순차적인 경우, 피봇이 포함되지 않은 경우
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return binary_search(left, mid-1)
                else:
                    return binary_search(mid+1, right)
            # left에서 mid 사이에 피봇이 포함된 경우
            else:
                # mid 부터 right 까지 순차적이며, target이 포함된 경우
                if nums[mid] < target <= nums[right]:
                    return binary_search(mid+1, right)
                else:
                    return binary_search(left, mid-1)

        left, right = 0, len(nums)-1

        return binary_search(left, right)

    # 첵에서 제공하는 풀이
    # 피벗을 먼저 찾는다.
    def search(self, nums: List[int], target: int) -> int:
        # 예외처리
        if not nums:
            return -1

        # 최솟값을 찾아 피벗 설정
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # mid + 1 과 right 사이에 피벗된 지점이 존재
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 피벗 기준 이진 검색
        left, right = 0, len(nums) - 1

        while left <= right:
            # 이진검색의 자료형 초과 버그를 방지하는 mid 계산
            mid = left + (right-left)//2
            # 피봇을 고려한 mid 인덱스
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return - 1
