import sys


class Solution:
    def manhattanDistance(self, a, b):
        return sum([abs(z1 - z2) for z1, z2 in zip(a, b)])

    # 조건을 잘 읽자!
    # 이미 한 번 계산한 거리는 두 번 계산하지 않도록 기록을 한다.
    # 거리 테이블 생성 (대칭 행렬), 상향식, 타뷸레이션

    # 가중치가 있는 무방향 싸이클이 없는 그래프(트리)
    # 최소 신장 트리 문제, 프림 알고리즘
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) < 2:
            return 0
        summation = 0
        length = len(points)
        #weight = collections.defaultdict(lambda: sys.maxsize)
        heap = []

        #weight_dict = collections.defauldict([0]*length)

        connected = [0]
        while len(connected) < length:

            # 직전 연결된 정점 순회
            i = connected[-1]
            j = -1
            while j < length-1:
                j += 1
                if j in connected:
                    continue
                temp_d = self.manhattanDistance(points[i], points[j])
                # if temp_d < weight[j]:
                #weight[j] = temp_d
                #heapq.heappush(heap, [weight[j], j])
                heapq.heappush(heap, [temp_d, j])

            temp = heapq.heappop(heap)
            while temp[1] in connected:
                temp = heapq.heappop(heap)
            idx = temp[1]
            #weight[idx] = sys.maxsize
            summation += temp[0]
            connected.append(idx)
        return summation


class Solution:

    def manhattanDistance(self, a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) < 2:
            return 0

        length = len(points)
        weight = collections.defaultdict(lambda: sys.maxsize)
        heap = []
        connected = {0}
        summation = 0
        i = 0

        while len(connected) < length:

            j = -1
            while j < length-1:
                j += 1
                if j in connected:
                    continue
                temp_d = self.manhattanDistance(points[i], points[j])
                if temp_d < weight[j]:
                    weight[j] = temp_d
                    heapq.heappush(heap, [temp_d, j])

            temp = heapq.heappop(heap)
            while temp[1] in connected:
                temp = heapq.heappop(heap)

            i = temp[1]
            weight[i] = sys.maxsize
            connected.add(i)

            summation += temp[0]

        return summation
