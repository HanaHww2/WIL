# 단지번호 붙이기
# https://www.acmicpc.net/problem/2667
# 조건, 반환할 결과 등 문제를 잘 읽자!!!!!
######################
import sys

n = 7
arr = [
    "0110100",
    "0110101",
    "1110101",
    "0000111",
    "0100000",
    "0111110",
    "0111000",
]

arr = [list(map(int, row)) for row in arr]


# n = int(sys.stdin.readline())
# arr = []
# for i in range(n):
#     arr.append(list(int(x) for x in sys.stdin.readline().strip()))

# print(arr)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def in_range(y, x):
    if -1 < y < n and -1 < x < n:
        return True
    return False


###############################
# 정렬 빼먹음 ㅠㅠㅠㅠㅠㅠ
# 문제 잘 읽고 풀자...시간낭비;
def dfs(y, x):
    cnt = 0
    # 동서남북 이동
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if in_range(ny, nx) and arr[ny][nx] == 1:
            arr[ny][nx] = 0
            cnt += 1
            cnt += dfs(ny, nx)

    return cnt


answer = 0
cnt_l = []
# 1 찾기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            answer += 1
            arr[i][j] = 0
            cnt_l.append(dfs(i, j) + 1)

print(answer)
for a in sorted(cnt_l):
    print(a)
##########################
# 틀린 로직 2. 글로벌 사용
# def dfs(y, x):
#     global cnt
#     # cnt = 0
#     # 동서남북 이동
#     for d in range(4):
#         ny = y + dy[d]
#         nx = x + dx[d]
#         if in_range(ny, nx) and arr[ny][nx] == 1:
#             arr[ny][nx] = 0
#             cnt += 1
#             dfs(ny, nx)


# answer = 0
# cnt_l = []
# cnt = 0
# # 1 찾기
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 1:
#             answer += 1
#             arr[i][j] = 0
#             cnt = 1
#             dfs(i, j) # 수정하다가 함수 실행 빼먹음...
#             cnt_l.append(cnt)

# print(answer)
# for a in sorted(cnt_l): # 정렬 빼먹음
#     print(a)
############################################
# 정답 로직
# 다른 사람 풀이를 참고해서 수정한 건데
# 사실 조건 로직을 언제 타느냐의 차이 뿐이었다.
# 순간 뇌정지 와서 한참 고민했다...
#
# 결과적으로는 그냥 정렬 수행을 안해서 그랬던 것...
# 중간에 로직 비교할 때 반복적으로 실패가 떴는데 계속 백준 사이트에 코드 수정했다가
# ide에 수정했다가 하면서 뭔가를 자꾸 하나씩 빠뜨린 게 패착이었다. (<- 즉, 거의 뇌정지 상태)
#
# def dfs(y, x):
#     global cnt
#     # cnt = 0
#     if not in_range(y, x):
#         return

#     if arr[y][x] == 1:
#         arr[y][x] = 0
#         cnt += 1
#         # 동서남북 이동
#         for d in range(4):
#             ny = y + dy[d]
#             nx = x + dx[d]
#             dfs(ny, nx)

#     # return cnt


# answer = 0
# cnt = 0
# cnt_l = []
# # 1 찾기
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 1:
#             answer += 1
#             dfs(i, j)
#             cnt_l.append(cnt)
#             cnt = 0
# print(answer)
# for a in sorted(cnt_l):
#     print(a)
