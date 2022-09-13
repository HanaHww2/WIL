class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        answer = 0
        r_len = len(grid)
        l_len = len(grid[0])

        def dfs(n, m):

            if n >= r_len or n < 0 or m >= l_len or m < 0:
                return
            if grid[n][m] == '0':
                return

            if grid[n][m] == '1':
                grid[n][m] = '0'

                dfs(n+1, m)
                dfs(n-1, m)
                dfs(n, m+1)
                dfs(n, m-1)

        n = m = 0
        while True:
            # 전체 순회 완료
            if n == r_len:
                break

            if grid[n][m] == '0':
                m = (m + 1) % l_len
                if m == 0:
                    n += 1
            else:
                dfs(n, m)
                answer += 1

        return answer

    # 중첩함수 사용하지 않은 경우
    # 책에서 제공하는 풀이
    def dfs(self, grid: List[List[str]], n, m):
        r_len = len(grid)
        l_len = len(grid[0])

        # 조건 분기 개선
        if n >= r_len or n < 0 or m >= l_len or m < 0 or grid[n][m] == '0':
            return

        grid[n][m] = '0'

        self.dfs(grid, n+1, m)
        self.dfs(grid, n-1, m)
        self.dfs(grid, n, m+1)
        self.dfs(grid, n, m-1)

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0  # 예외 처리

        answer = 0
        r_len = len(grid)
        l_len = len(grid[0])

        # 포문 사용으로 반복을 명확하게 n*m 으로 수행하도록 개선
        for n in range(r_len):
            for m in range(l_len):
                if grid[n][m] == '1':
                    self.dfs(grid, n, m)
                    answer += 1

        return answer
