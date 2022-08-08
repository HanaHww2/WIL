class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 주어진 데이터를 정렬
        intervals.sort(key=lambda x: x[0])

        length = len(intervals)
        i = 0
        while i < len(intervals)-1:

            a = intervals[i]
            b = intervals[i+1]

            # 순회하며 값이 중첩되는지 확인
            if a[1] >= b[0]:
                temp = [a[0] if a[0] < b[0] else b[0],
                        a[1] if a[1] > b[1] else b[1]]
                # 중첩된다면, 데이터를 갱신
                intervals = intervals[:i] + [temp] + intervals[i+2:]

            # 중첩되는 것이 없다면 포인터 이동
            else:
                i += 1

        return intervals

    # 책 풀이 참고
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        for d in (sorted(intervals, key=lambda x: x[0])):

            # 이전에 삽입한 데이터 기준으로, 중첩이 있는지 확인
            if merged and d[0] <= merged[-1][1]:
                merged[-1][1] = max(d[1], merged[-1][1])
            # 중첩되는 것이 없다면, 반환할 리스트에 삽입
            else:
                merged += d,  # 콤마를 이용하면 서브리스트 형태로 입력

        return merged
