class Solution:

    # 브루트 포스 풀이
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        set1 = set(nums1)
        set2 = set(nums2)

        for n in set1:
            if n in set2:
                result.append(n)
        return result

    # 이진 탐색을 활용한 풀이, O(nlogn)
    # nums2를 정렬하고, nums1은 set() 으로 변경
    # nums1의 요소를 nums2가 갖고 있는지 이진 검색을 통해서 확인
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        set1 = set(nums1)
        nums2.sort()  # 정렬

        for n in set1:
            i = bisect.bisect_left(nums2, n)

            if i < len(nums2) and n == nums2[i]:
                result.append(n)

        return result

    # 투 포인터 활용, O(nlogn)
    # 두 리스트 모두 정렬하고, 각각의 리스트에 포인터를 두고 순회
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()

        # 리스트 모두 정렬
        nums1.sort()
        nums2.sort()

        i = j = 0

        # 투포인터를 각각 이동하며, 일치하는 수를 찾는다.
        # 투 포인터로 조회하는데 O(2n) 소요
        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                result.add(nums2[j])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result
