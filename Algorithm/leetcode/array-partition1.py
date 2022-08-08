class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()  # 반환값이 없고, nums 위치에서 정렬
        count = 0
        for i in range(0, len(nums), 2):
            count += nums[i]
        return count

    # 코드 최적화
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
