class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        answer = []
        heap = []  # 힙을 활용한 정렬

        for (x, y) in points:
            d_squared = x**2 + y**2
            heapq.heappush(heap, (d_squared, [x, y]))

        while k:
            answer.append(heapq.heappop(heap)[1])
            k -= 1

        return answer
