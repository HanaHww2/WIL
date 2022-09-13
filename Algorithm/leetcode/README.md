# Graph 

- 섬의 갯수
    - 입력 값이 반드시 그래프 형이 아니더라도 그래프로 변환해서 풀 수 있다.

[Number of Islands - LeetCode](https://leetcode.com/problems/number-of-islands/)

- 전화번호 문자 조합

[Letter Combinations of a Phone Number - LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

- 순열
    - ❗파이썬에서 객체 참조 주의
    - 실무에서는 잘 정립된 라이브러리인 itertools를 사용한다.

[Permutations - LeetCode](https://leetcode.com/problems/permutations/)

```python
class Solution:
    def permute(self, nums):
        result = []
        tmp_result = []

        def dfs(elements):
            if len(elements) == 0:
								# 객체 참조가 아니라 복사 이용
                result.append(tmp_result[:])

            for e in elements:
								# 객체 참조가 아니라 복사 이용
                tmp_elements = elements[:]
                tmp_elements.remove(e)

                tmp_result.append(e)
								# dfs 재귀 호출
                dfs(tmp_elements)
								# 재귀에서 리턴(백트랙킹)된 이후, 반복 시행 전 리스트 비우기
                tmp_result.pop() 

        dfs(nums)
        return result
```

- 조합
    
    [](https://leetcode.com/problems/combinations/)
    

```python
class Solution:
		def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(tmp_result, start: int, k: int):
            if k == 0:
                result.append(tmp_result[:])
                return
						# 반복횟수 최적화, 조합 결과 크기(k)에 제한이 있는만큼 불필요한 전체 반복은 없게 한다.
            for i in range(start, n+1-(k-1)):
                tmp_result.append(i)
                dfs(tmp_result, i+1, k-1)
                tmp_result.pop()

        dfs([], 1, k)
        return result
```

아래와 같이 작성할 수도 있다.

```python
class Solution:
    def combine(self, num_list, num):
        answer = []
        if num > len(num_list):
            return answer
        # Base Case
        if num == 1:
            for i in num_list:
                answer.append([i])
        # General Case
        elif num > 1:
            for i in range(len(num_list) - num + 1):
                for temp in self.combine(self, num_list[i+1:], num-1):
                    answer.append([num_list[i]] + temp)

        return answer
```

- 참고)
    - [https://medium.com/@dltkddud4403/python-순열-조합-구현-5e496e74621c](https://medium.com/@dltkddud4403/python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%EA%B5%AC%ED%98%84-5e496e74621c)
    - [https://learnandearn.tistory.com/21](https://learnandearn.tistory.com/21)
- 조합의 합
- 부분 집합

[Subsets - LeetCode](https://leetcode.com/problems/subsets/)

- 일정 재구성
    - 문제가 명확하지 않은 것 같다.
    - 사전 순서가 우선이 되는 거 아닌가? 순회가 필수적인 건가?
    - [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] 의 test 케이스의 경우 답은 ["JFK","NRT","JFK","KUL"] 이 요구된다. 아무리 생각해도 답이 오류인 것 같다. 토론에서 찾아보면 해당 테스트 케이스에 대해 논의한 글들이 존재한다. ← K가 N보다 사전적으로 우선한다.
    - 상길북에서 위와 같은 케이스 때문인지 해당 문제를 while로 접근해서 해결한다. 그러나 내 생각엔 일단 문제가 좀 애매하다. if로 조건을 주는 게 맞는 것 같다.
        - while문을 이용하면, 백트랙킹을 하면서 다시 남은 경로를 방문하게 되는 경우가 발생한다. (만약 ["JFK", "ANY"] 와 같은 구간이 추가되는 경우)

[Reconstruct Itinerary - LeetCode](https://leetcode.com/problems/reconstruct-itinerary/)

- 코스 스케쥴
    - defaultdictionary 를 순회할 때 오류가 발생한다. 순회가 필요할 경우, list() 함수를 이용해 새로운 key 값 리스트를 생성해 활용할 수 있다. (python 3.9.6 에서는 오류가 없었다.)
    - 이미 방문한 노드는 다시 재방문 하지 않는 방식으로 가지치기를 진행하면 최적화가 가능하다.
    - [Course Schedule - LeetCode](https://leetcode.com/problems/course-schedule/)