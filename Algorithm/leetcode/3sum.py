class Solution:

    def getTwoEl(self, nums, target):
        res = []
        left, right = 0, len(nums)-1

        while left < right:
            temp_sum = nums[left] + nums[right]

            if temp_sum > target:
                right -= 1
            elif temp_sum < target:
                left += 1
            else:
                # 이하 로직 개선 필요
                right -= 1
                left += 1
                if left-1 != 0 and nums[left-1] == nums[left-2]:
                    continue
                res.append([-target, nums[left-1], nums[right+1]])
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()  # 반환값이 인덱스 순서와 무관하므로

        for i, n in enumerate(nums[:-2]):
            if i != 0 and n == nums[i-1]:
                continue  # 중복방지
            target = -n
            result = self.getTwoEl(nums[i+1:], target)
            if result:
                answer += result

        return answer
