# Array Partition1

class Solution:

    # 정렬하여 인접 요소 페어를 생성하고, 작은 값으로 합을 구한다.
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()  # 반환값이 없고, nums 위치에서 정렬
        count = 0

        for i in range(0, len(nums), 2):
            count += nums[i]
        return count

    # 코드 최적화
    def arrayPairSum2(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
