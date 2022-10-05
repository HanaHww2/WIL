# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
# 참고 https://pacific-ocean.tistory.com/153
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))

dp = [0] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
