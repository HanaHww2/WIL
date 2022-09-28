# 30840KB 6120ms
# 최적화가 시급하다. 100ms
# 이터툴즈를 막 쓴 거 같다.
# 그리고 로직 자체가 최적화 없는 정직한 브루트 포스다.
import itertools
import sys
# n = 8
# arr = ['0 5 4 5 4 5 4 5',
#        '4 0 5 1 2 3 4 5',
#        '9 8 0 1 2 3 1 2',
#        '9 9 9 0 9 9 9 9',
#        '1 1 1 1 0 1 1 1',
#        '8 7 6 5 4 0 3 2',
#        '9 1 9 1 9 1 0 9',
#        '6 5 4 3 2 1 9 0']
# arr = [list(map(int, x.split(' '))) for x in arr]

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split(' '))))

# n명을 2그룹으로 나누는 방법, 조합
# n명 중에 n/2를 선택, 순서 무관, 조합
g1 = itertools.combinations(range(n), int(n/2))
answer = 10e4

# 생성한 조합 기준....
# 회원 2인 조합을 구한다. 혹은 반복문 수행
for g in g1:
    cnt = 0
    another = set(range(n)) - set(g)
    p1 = itertools.combinations(g, 2)
    p2 = itertools.combinations(another, 2)

    for x, y in zip(p1, p2):
        cnt += arr[x[0]][x[1]] + arr[x[1]][x[0]]
        cnt -= arr[y[0]][y[1]] + arr[y[1]][y[0]]
    answer = min(answer, abs(cnt))

print(answer)
