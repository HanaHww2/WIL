class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        sub_string = ''
        max_cnt = 0
        temp_cnt = 0

        # 2개의 포인터 활용
        start = temp = 0

        while temp < len(s):
            w = s[temp]

            if w in sub_string:
                max_cnt = max(max_cnt, temp-start)
                idx = sub_string.index(w)+1
                start += idx
                sub_string = sub_string[idx:]+w

            else:
                sub_string += w
            temp += 1

            if temp == len(s):
                max_cnt = max(max_cnt, temp-start)

        return max_cnt if max_cnt != 0 else len(s)
