class Solution:

    PHONE_STR = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    arr = []

    def dfs(self, digits, prefix):

        if not digits:
            self.arr.append(prefix)
            return

        for a in self.PHONE_STR[digits[0]]:
            self.dfs(digits[1:], prefix + a)

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.arr = []
        self.dfs(digits, '')

        return self.arr

    # 책에서 제공하는 풀이
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(index, path):
            print(path, index)
            if len(path) == len(digits):
                result.append(path)
                return

            # 여기서 첫번째 반복문이 수행되는 이유가 없는 것 같다.
            # 주어진 digit에 해당하는 문자를 모두 만들어야 하는데
            # 해당 반복문을 돈다면, 불필요하게 하나의 디짓을 건너뛴 조합을 생성해버린다.
            # 결국 길이 조건에 만족하지 않아 결과 집합에 포함되지 않을 문자열을 생성하는 셈이다.
            for i in range(index, len(digits)):
                for j in self.PHONE_STR[digits[i]]:
                    print(path + j)
                    dfs(i+1, path + j)

        if not digits:
            return []

        result = []
        dfs(0, '')

        return result
