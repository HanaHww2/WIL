from collections import defaultdict


class Solution:
    # 딕셔너리를 사용한 풀이
    def isAnagram(self, s: str, t: str) -> bool:
        table = defaultdict(int)

        for w in s:
            table[w] += 1
        for w in t:
            table[w] -= 1
        for key in table:
            if table[key] != 0:
                return False

        return True

     # 정렬을 사용한 풀이
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
