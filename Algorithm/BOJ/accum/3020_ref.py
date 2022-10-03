import sys

IN = sys.stdin.readline


def main():
    N, H = map(int, IN().split())
    arr = [0] * H
    for i in range(N):
        h = int(IN())
        if i % 2 == 0:
            arr[h] -= 1  # 석순이 존재하지 않는 공간에 -1
        else:
            arr[-h] += 1

    ret = [N // 2, 1]  # 석순이 존재하지 않는 공간엔 -1을 수행했으므로, N//2에서 시작
    cur = ret[0]
    for i in range(1, H):
        cur += arr[i]
        if cur < ret[0]:
            ret = [cur, 1]
        elif cur == ret[0]:
            ret[1] += 1
    print(*ret)


if __name__ == "__main__":
    main()
##################################
# 로직이 흥미로워서 타인의 풀이를 퍼왔다.
# https://www.acmicpc.net/source/43060869
