# 차이를 최대로
# https://www.acmicpc.net/problem/10819
#
# 메모리 30840 KB 140 ms
# 60 ms 대로 푸는 케이스가 많이 있는데 로직이 아직 이해가 안된다.
#
# 리스트를 나열할 수 있는 모든 경우의 수(순열, 순서, 크기 고정)를 찾아서,
# 반복문을 돌며 거리를 계산합니다.
#
# 순열 생성 -> 모든 경우의 수 체크, 최댓값 반환
##############################################
import sys
import itertools

# 첨 코딩 배울 때 백준 잠깐 써보고
# 오랜만에 사용해서 입력값 받는 게 어색하고 아직 어렵다...
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


def count_diff(el):
    cnt = 0
    for i, _ in enumerate(el[1:]):
        cnt += abs(el[i] - el[i-1])
    return cnt


# 첨에 순열 생성할 때, 순열의 크기 지정을 하지 않아서
# 시간초과 오류가 났던 것 같다!
# dfs 구현 연습을 핑계?로 이터툴즈를 외면해왔기에 아직 익숙하지 않다.
possible = itertools.permutations(arr, n)
answer = 0
for el in possible:
    answer = max(answer, count_diff(el))

print(answer)
