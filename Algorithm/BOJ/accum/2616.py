from itertools import accumulate
import sys

n = int(sys.stdin.readline().strip())  # 길이
train_p = list(int(x) for x in sys.stdin.readline().split(" "))
m = int(sys.stdin.readline().strip())  # 최대 객차


acc_p = [0] + list(accumulate(train_p))  # 누적합
# last = m - 1

# 시간초과 날 거 같아... 그리디인가...>>>> dp 였다!!!
# def dfs(tot, last, i):
#     global answer

#     if i == 4:
#         answer = max(answer, tot)
#         return

#     for j in range(last, n - max_capacity * (3 - i)):
#         # 기관차가 끄는 승객 수
#         new_tot = tot + acc_p[j]
#         if j - max_capacity > -1:
#             new_tot -= acc_p[j - max_capacity]

#         dfs(new_tot, j + max_capacity, i + 1)


# answer = 0
# dfs(0, 0, 1)
# print(answer)
dp = [[0 for j in range(n + 1)] for i in range(3)]
for i in range(3):
    # j는 최소 m 부터 시작
    # 이전 기관차에서 최소로 사용할 객차 수 ~ 전체 - 이후 기관차에서 최소한 사용할 객차 수
    for j in range((i + 1) * m, n - m * (3 - i - 1) + 1):
        if i == 0:
            dp[i][j] = max(dp[i][j - 1], acc_p[j] - acc_p[j - m])
        else:
            # 현재 기관차에서 j-1까자의 최댓값
            # 이전 기관차에서 j-m까지 최댓값 + j-m+1부터 j까지의 객차를 태우는 경우
            dp[i][j] = max(dp[i][j - 1], (dp[i - 1][j - m] + acc_p[j] - acc_p[j - m]))

print(dp[-1][-1])
