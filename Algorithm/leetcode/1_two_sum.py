# 1. Two Sum
class Solution:
    # 유튜브에서 최적화 전략엔 일단 해시테이블이라는 말을 본 기억이 있다.
    # There's saying that the base optimizaion strategy is almost from HashTable
    # so I'm using it, but with just list(index coulb be key)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_nums = []
        for i, n in enumerate(nums):
            need_num = target-n
            # index() 메소드를 사용할 때, list에 값이 존재하지 않으면 ValueError가 발생한다.
            # 오류를 try except로 제어했는데, 오류 말고 다른 반환값을 주는 메소드가 있다면 그것으로 변경하는 게 좋을지도.
            try:
                x = need_nums.index(n)
                return [x, i]
            except ValueError:
                pass
            need_nums.append(need_num)

        return []

    # 딕셔너리의 키 값으로 조회하는 방식
    # 파이썬의 리스트 또한 일종의 해시 구조인 것으로 알고 있지만 값으로 탐색했었다,
    # 아래의 경우에는 키 값으로 조회하므로 속도가 훨씬 개선된다. 공간복잡도는 리스트 풀이가 낫긴 하지만 느린 편이다.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_nums = {}
        for i, n in enumerate(nums):
            need_num = target-n
            # key에 값이 존재하는지 in 연산으로 탐색하고, 또 값을 찾아가는 방식보단
            # KeyError 오류를 try except로 제어해보았다
            try:
                x = need_nums[n]
                return [x, i]
            except KeyError:
                pass
            need_nums[need_num] = i

        return []

    # 에러를 제어하는 것보다 in 연산 탐색이 더 빠르다.
    # 에러의 발생과 제어에서도 연산 로직이 추가되기 때문인 듯 하다.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need_nums = {}
        for i, n in enumerate(nums):
            if n in need_nums:
                return [need_nums[n], i]
            need_nums[target-n] = i

        return []

    # 인풋을 정렬(O(nlogn))하고, 투 포인터를 활용해본다.
    # 찾아낸 값을 인덱스로 다시 조회해야 한다.
    # 생각만큼 느리진 않다? 모든 테케 인풋이 이미 정렬이 되어있는 걸까
     def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums)-1
        while not left == right:
            temp_sum = sorted_nums[left] + sorted_nums[right]
            if temp_sum < target:    
                left += 1
            elif temp_sum > target:
                right -= 1
            else:
                first = nums.index(sorted_nums[left])
                second = nums.index(sorted_nums[right])
                if first == second:
                    second = nums[first+1:].index(sorted_nums[left]) + first + 1
                return first, second 
        return []