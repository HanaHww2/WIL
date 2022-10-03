# 11660 구간합 구하기5
# https://www.acmicpc.net/problem/11660
###############
from itertools import accumulate
import sys


def in_range(y, x):
    if -1 < y < n and -1 < x < n:
        return True
    return False


# n, m = map(int, sys.stdin.readline().split(" "))
# arr = []
# coordinate = []
# for i in range(n):
#     arr.append(list(int(x) for x in sys.stdin.readline().split(" ")))
# for i in range(m):
#     coordinate.append(list(int(x) for x in sys.stdin.readline().split(" ")))

# for i in range(len(arr)):
#     arr[i] = accumulate(arr[i])

# temp = []
# for j, a in enumerate(zip(*arr)):
#     temp.append(accumulate(a))
# arr = list(zip(*temp))

# result = []
# for c in coordinate:  # 인덱싱 실수를 주의하자!
#     temp_t = arr[c[2] - 1][c[3] - 1]

#     if in_range(c[0] - 2, c[3] - 1):  # 시작 행 위
#         temp_t -= arr[c[0] - 2][c[3] - 1]

#     if in_range(c[2] - 1, c[1] - 2):  # 시작 열 전
#         temp_t -= arr[c[2] - 1][c[1] - 2]

#     if in_range(c[0] - 2, c[1] - 2):  # 2번 제거된 교집합
#         temp_t += arr[c[0] - 2][c[1] - 2]

#     result.append(temp_t)
#     print(temp_t)

##################################################
# 참고 https://pacific-ocean.tistory.com/459
# 처음부터 배열 크기를 +1 로 구성하면, 더 깔끔하게 풀이를 작성할 수 있다!
# 더하여 accumulate를 두 번 수행하는 과정에서
# 행렬의 전치까지 수행하게 되므로,
# 직접 이중 포문을 작성하는 편이 더 효율적인 것 같다.
n, m = map(int, sys.stdin.readline().split(" "))
arr = [[0] * (n + 1)]
coordinate = []
for i in range(n):
    arr.append([0] + list(int(x) for x in sys.stdin.readline().split(" ")))

for i in range(m):
    coordinate.append(list(int(x) for x in sys.stdin.readline().split(" ")))

for i in range(len(arr)):
    arr[i] = accumulate(arr[i])

temp = []
for j, a in enumerate(zip(*arr)):
    temp.append(accumulate(a))
arr = list(zip(*temp))

# 행렬의 누적합을 동시에 시행하므로 중복으로 더해지는 arr[i][j] 값을 차감해준다.
# for i in range(n):
#     for j in range(n):
#         arr[i + 1][j + 1] = (arr[i][j + 1] + arr[i + 1][j] - arr[i][j])

# 혹은 아래와 같이 행, 열의 누적합 각각 시행
# https://www.acmicpc.net/source/36698930
# for i in range(1, n+1):
#     for j in range(2, n+1):
#         arr[i][j] += arr[i][j-1]
# for i in range(2, n+1):
#     for j in range(1, n+1):
#         arr[i][j] += arr[i-1][j]
# 백준 코드에 이외에도 다양한 방식의 누적합 계산 코드가 존재!
# https://www.acmicpc.net/problem/status/11660/1003/1

result = []
for c in coordinate:  # 인덱싱 실수를 주의하자!
    temp_t = (
        arr[c[2]][c[3]]
        - arr[c[0] - 1][c[3]]
        - arr[c[2]][c[1] - 1]
        + arr[c[0] - 1][c[1] - 1]
    )
    result.append(temp_t)
    print(temp_t)
