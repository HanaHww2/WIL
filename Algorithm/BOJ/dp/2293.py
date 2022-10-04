import sys

n, k = map(int, sys.stdin.readline().split(" "))

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

# 참고 https://mong9data.tistory.com/68
# 첨 접근할 때 2차원으로 테이블을 만들려고 했었는데 너무 복잡하게 생각한 것 같다!
memo = [0] * (k + 1)
memo[0] = 1  # 동전 1개를 썼을 때 나오는 값

for coin in arr:
    for target in range(coin, k + 1):
        memo[target] += memo[target - coin]  # 누적합

print(memo[k])
