# 구간 나누기
# https://www.acmicpc.net/problem/2228
# 어렵다...
# 재귀로 푸는 풀이도 있던데 확인할 것
#################

# https://velog.io/@asdsa2134/%EB%B0%B1%EC%A4%80-2228-%EA%B5%AC%EA%B0%84-%EB%82%98%EB%88%84%EA%B8%B0
import sys

input = sys.stdin.readline


n, m = map(int, input().split(" "))

arr = [0]
for i in range(1, n + 1):
    arr.append(int(input().strip()) + arr[-1])  # 누적합

dp = [[0] + [float("-inf")] * m] + list([0] * (m + 1) for _ in range(n))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j]

        # i 인덱스까지 j 개의 구간을 선택하는 경우의 수
        # i번째를 포함하지 않으면서 j개의 구간을 선택했을 때
        # i번째를 포함하며, j-1번째 구간은 k-2를 넘지 않는 경우
        for k in range(1, i + 1):
            if k >= 2:
                dp[i][j] = max(dp[i][j], arr[i] - arr[k - 1] + dp[k - 2][j - 1])
            elif k == 1 and j == 1:
                dp[i][j] = max(dp[i][j], arr[i])


print(dp[n][m])
