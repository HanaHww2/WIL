# 피자 굽기
# https://www.acmicpc.net/problem/1756
#
import sys, heapq

input = sys.stdin.readline

d, n = map(int, input().split())
minimum = 10**9
oven = [minimum]


for x in map(int, input().split()):
    if minimum > x:
        minimum = x
    oven.append(minimum)


def search(top, bottom, dough_len):

    while top <= bottom:
        mid = (top + bottom) // 2

        if oven[mid] < dough_len:
            bottom = mid - 1
        else:
            top = mid + 1
    return bottom


# 오븐 깊이 기준으로 이진 탐색

top, bottom = 1, d

for x in map(int, input().split()):

    bottom = search(top, bottom, x) - 1
    if bottom < 0:
        print(0)
        break
else:
    print(bottom + 1)

# 아래는 처음 작성했던 완탐 코드?
# 시간초과
# import sys


# input = sys.stdin.readline
# d, n = map(int, input().split())
# oven = list(int(x) for x in input().split())
# dough = list(int(x) for x in input().split())


# def search(left, right):

#     for dough_len in dough:
#         while oven[left] >= dough_len and left < right:
#             left += 1

#         right = left - 1
#         if right < 1:
#             return 0
#         left = 0
#     return right + 1


# print(search(0, d))
