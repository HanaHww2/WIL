from functools import cmp_to_key


class Solution:

    def comperator(self, x, y):
        return int(x + y) - int(y + x)

    def largestNumber(self, nums: List[int]) -> str:

        # str_nums = [str(n) for n in nums]
        str_nums = list(map(str, nums))
        str_nums.sort(reverse=True, key=cmp_to_key(self.comperator))

        # result = ''.join(str_nums)
        # if result == '0'*len(result): return '0'
        # return result
        # 아래와 같이 코드 간결화
        return str(int(''.join(str_nums)))

    ###################
    # 삽입정렬로 구현하기
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        result = []

        for n in str_nums:
            if not result or self.compare(result[-1], n) >= 0:
                result.append(n)
                continue

            idx = -1
            length = len(result)

            # result를 뒤에서부터 순회하면서 삽입할 위치 확인
            while -length <= idx and self.compare(result[idx], n) < 0:
                idx -= 1
            result = result[:idx+1] + [n] + result[idx+1:]

        return str(int(''.join(result)))

    ###########
    # 책에서 제공하는 삽입정렬 구현 풀이
        # 비교 함수
    @staticmethod
    def to_swap(x: str, y: str) -> bool:
        return int(x + y) < int(y + x)

    # 삽입정렬(제자리 정렬)로 구현하기
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))

        i = 1
        while i < len(nums):
            j = i

            # 기준 노드를 그 앞에 위치하는 요소들과
            # 더 이상 스왑하지 않아도 될 때까지 하나씩 비교하며 정렬
            while j > 0 and self.to_swap(str_nums[j-1], str_nums[j]):
                str_nums[j], str_nums[j-1] = str_nums[j-1], str_nums[j]
                j -= 1

            i += 1  # 기준 노드의 인덱스

        return str(int(''.join(str_nums)))

    ###########
    # 프로그래머스 풀이 참고
    # https://school.programmers.co.kr/learn/courses/30/lessons/42746

    def largestNumber(self, nums: List[int]) -> str:
        numbers = list(map(str, nums))
        # 크기 제한 <= 10^9 이므로 9자리수 차이를 고려
        numbers.sort(key=lambda x: x*9, reverse=True)
        return str(int(''.join(numbers)))
