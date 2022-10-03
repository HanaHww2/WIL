from itertools import accumulate
import sys

n, m = map(int, sys.stdin.readline().split(" "))  # 길이, 높이

ob = []
for i in range(n):
    ob.append(int(sys.stdin.readline().strip()))

###############################
# 전체 동굴의 그림을 그려서 접근하려고 했다.
# 당연?하게도 시간초과...
#
# h_space = [0] * m

# for i in range(n):  # 각 높이마다 바로 합산
#     if i % 2 == 0:  # 석순
#         for j in range(1, ob[i] + 1):
#             h_space[m - j] += 1
#     else:
#         for j in range(1, ob[i] + 1):
#             h_space[j - 1] += 1

# answer = n
# cnt = 0
# for i, a in enumerate(h_space):
#     if answer > a:
#         answer = a
#         cnt = 1
#     elif answer == a:
#         cnt += 1
# print(min(h_space), cnt)

# 높이 기준으로 접근
up = [0] * (m + 1)
down = [0] * (m + 1)

for i in range(n):
    if i % 2 == 0:  # 석순
        down[ob[i]] += 1
    else:
        up[ob[i]] += 1

# 역방향으로 누적합 수행
for j in range(m - 1, -1, -1):
    down[j] += down[j + 1]
    up[j] += up[j + 1]

answer = n
cnt = 0
for j in range(1, m + 1):
    temp = down[m - j + 1] + up[j]
    if answer > temp:
        answer = temp
        cnt = 1
    elif answer == temp:
        cnt += 1

print(answer, cnt)
