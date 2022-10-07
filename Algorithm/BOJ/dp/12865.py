# 평범한 배낭
# https://www.acmicpc.net/problem/12865
#
import sys

n, k = map(int, sys.stdin.readline().split(" "))

arr = []
for i in range(n):
    arr.append(tuple(int(x) for x in sys.stdin.readline().split(" ")))

dp = [[0] * (k + 1) for _ in range(n + 1)]

# 정렬 없어도 됨.
arr.sort(key=lambda x: x[0])

# 으아악 짐은 한 개만 존재한다!
def packing():
    for i, b in enumerate(arr):
        w, v = b

        if w > k:  # 정렬 수행한 경우
            return print(dp[i][-1])

        # 테이블을 다 채워야 한다! w 부터 시작해서 틀림 x
        for j in range(1, k + 1):
            if j < w:
                dp[i + 1][j] = dp[i][j]
                continue

            dp[i + 1][j] = max(
                dp[i][j], v + dp[i][j - w]
            )  ### 짐은 한번만 담을 수 있다; ㅠ dp[i + 1][j - w]는 불가능

    return print(dp[-1][-1])

packing()
