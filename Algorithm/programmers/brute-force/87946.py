# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 피로도


def solution(k, dungeons):
    answer = -1

    # nonlocal 없이...
    # visited 배열 만들어서 해보기
    def dfs(cnt, curr, dungeons):
        nonlocal answer

        if cnt > answer:
            answer = cnt
        if not dungeons or answer >= cnt + len(dungeons):
            return

        for i, (n, u) in enumerate(dungeons):
            if n > curr:
                continue
            dfs(cnt + 1, curr - u, dungeons[:i] + dungeons[i + 1 :])

    dfs(0, k, dungeons)

    return answer
