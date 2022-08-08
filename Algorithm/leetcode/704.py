class Solution:
    # 재귀 풀이
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

           half = len(nums)//2

            if nums[half] == target:
                return half
            elif nums[half] > target: return self.search(nums[:half], target)
            else:
                temp = self.search(nums[half+1:], target)
                return half + 1 + temp if temp != -1 else -1

    # 포인터와 재귀를 이용한 이진 검색 풀이
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] < target:
                return binary_search(mid+1, right)
            elif nums[mid] > target: return binary_search(left, mid-1)
            else:
                return mid

        return binary_search(0, len(nums)-1)

    # 포인터와 반복을 활용한 풀이
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target: left = mid + 1
            elif nums[mid] > target: right = mid -1
            else: return mid
        
        return -1

    # 이진 검색 bisect 모듈을 활용한 풀이, 안정적인 O(logn)
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    # index() 메소드 활용, 최악의 경우 O(n)
    def search(self, nums: List[int], target: int) -> int:
        try: 
            return nums.index(target)
        except ValueError:
            return -1