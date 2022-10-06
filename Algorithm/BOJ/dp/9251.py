import sys

arr = []
for i in range(2):
    arr.append(sys.stdin.readline().rstrip())

n, m = len(arr[0]), len(arr[1])
dp = [0] * n

for i in range(m):
    cnt = 0
    for j in range(n):
        if cnt < dp[j]:
            cnt = dp[j]
        elif arr[1][i] == arr[0][j]:
            dp[j] = cnt + 1
print(max(dp))
