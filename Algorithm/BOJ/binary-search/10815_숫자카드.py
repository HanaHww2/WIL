# 숫자 카드
# https://www.acmicpc.net/problem/10815
#
import sys

input = sys.stdin.readline
n = int(input())
arr = sorted(list(int(x) for x in input().split(" ")))
m = int(input())
m_arr = list(int(x) for x in input().split(" "))


def binary_search(left, right, target):

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            right = mid - 1
            continue
        if arr[mid] < target:
            left = mid + 1
            continue
        # if arr[mid] == target:
        return True

    return False


answer = [0] * m
for i, x in enumerate(m_arr):
    if binary_search(0, n - 1, x):
        answer[i] = 1

print(*answer)

# 이진탐색 문제라서 이진탐색으로 풀었을 뿐인데... 정렬 수행 등으로 2000ms 정도 나옴
# set()으로 바로 검색하는 코드는 300ms 대
# https://www.acmicpc.net/source/48572077
# def solution():
#     import sys

#     A, B = sys.stdin.read().split("\n")[1::2] # n, m 입력값은 건너뛰고 배열만 받음
#     A = set(A.split()) # set()
#     B = B.split()
#     print("".join("1 " if x in A else "0 " for x in B)) # 1차 순회로 해결

# solution()
