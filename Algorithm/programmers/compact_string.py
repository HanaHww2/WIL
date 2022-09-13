# https://programmers.co.kr/learn/courses/30/lessons/60057
# 예전 풀이
def solution(s):
    answer = 0
    results = []
    for i in range(len(s)):
        cnt = 1
        words = [s[j:j+i+1] for j in range(0, len(s), i+1)]
        for k in range(len(words)):
            if k == len(words)-1:
                if cnt != 1:
                    words[k] = str(cnt)+words[k]
            else:
                if words[k] == words[k+1]:
                    cnt += 1
                    words[k] = ''
                elif cnt != 1:  # words[k] != words[k+1]
                    words[k] = str(cnt)+words[k]
                    cnt = 1
        results.append(len(''.join(words)))

        answer = min(results)
    return answer

# 수정할 부분 ->
# 최초 반복을 전체 문자열 길이의 절반으로
# words 리스트를 만들지 않고 문자열 슬라이싱을 반복해보기
# 문자열 길이도 그 때 그 때 count해서 메모리 아껴보기
