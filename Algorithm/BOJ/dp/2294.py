# https://www.acmicpc.net/problem/2294
# 동전2
#
import sys

n, k = map(int, sys.stdin.readline().split(" "))

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

# 불가능한 경우에는 -1을 출력한다.
# 위의 경우를 처음에 고려하지 못했다.
# 최소 동전 크기가 1이고, 10000원이 최대 금액이므로
# 10001로 값을 정한다.
memo = [10001] * (k + 1)
memo[0] = 0

for coin in arr:
    if coin > k:
        continue
        # break # 정렬 안됐다구...ㅠ
    memo[coin] = 1
    for target in range(coin, k + 1):
        if memo[target - coin] + 1 < memo[target]:
            memo[target] = memo[target - coin] + 1
print(memo[k] if memo[k] != 10001 else -1)
