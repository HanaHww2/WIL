class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 제자리 정렬, 삽입 정렬
        for i in range(1, len(nums)):
            j = i-1
            while j > -1:
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    # self.swap(i, j)
                    i = j
                j -= 1

    # 다익스트라가 제안한 네덜란드 국기 문제와 동일 (매우 유명)
    # 쿽 정렬의 개선 아이디어와 연관
    # 빨(0), 흰(1), 파(2)와 같이 세 부분으로 분할해, 기존 퀵 정렬의 두 부분 분할을 개선하는 방안 제시
    # 중앙값(1)을 기준으로 한다.
    def sortColors(self, nums: List[int]) -> None:
        # i, k 가 양 끝단 포인터
        # 비교가 완료되면 i는 붉은 색( 1보다 작은 수)의 다음 인덱스를 가리키게 되고,
        # k는 푸른색(1보다 큰 수)의 첫 인덱스가 된다.
        i = j = 0
        k = len(nums)

        while j < k:
            # 중앙값(1) 기준으로 스왑 수행
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif nums[j] > 1:
                k -= 1
                nums[k], nums[j] = nums[j], nums[k]
            else:
                j += 1
