# 최대 서브 어레이 문제 유형과 유사한 구조
# 카데인 알고리즘
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_p = 10000  # 제약조건

        # 가격 탐색
        # 최솟값과 최댓값을 계속 갱신
        for i in range(len(prices)-1):
            min_p = min(min_p, prices[i])
            profit = max(profit, prices[i+1] - min_p)

        return profit
