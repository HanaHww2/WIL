# 분할 정복 Divide And Conquer

다중 분기 재귀를 기반으로 하는 알고리즘 디자인 패러다임을 말한다. 즉 재귀를 활용하는 대표적인 알고리즘 중 하나이다.

분할 정복은 직접 해결할 수 있을 정도로 간단한 문제가 될 때까지 문제를 재귀적으로 쪼개나간 다음, 그 **하위 문제의 결과들을 조합하여 원래 문제의 결과**로 만들어 낸다.

대표적인 분할 정복 알고리즘으로 병합 정렬을 들 수 있다.

- 1945년 폰 노이만이 병합 정렬을 통해서 분할 정복 개념을 제안했다.

참고) 그보다 훨씬 이른 고대 그리스의 수학자 유클리드가 정리한 문제를 분할해 풀이하는 방식의 최대 공약수 알고리즘이 인류 최초의 알고리즘이다.

- 유클리드 알고리즘이라고도 한다.
- 문제를 축소해서 정복한다는 개념을 적용한 알고리즘이다.

### 분할 정복 단계

- 분할 : 문제를 동일한 유형의 여러 하위 문제로 나눈다.
- 정복 : 가장 작은 단위의 하위 문제를 해결하여 정복한다.
- 조합 : 하위 문제에 대한  결과를 원래 문제에 대한 결과로 조합한다.

# 리트코드

83) 과반수 엘리먼트
- 정렬하여 가운데 지정하는 방식으로도 풀 수 있다. (항상 답이 있다는 전제가 필요하다)
- [Majority Element - LeetCode](https://leetcode.com/problems/majority-element/solution/)

```python
// 내 풀이
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        n = len(nums)
        
        while nums:
            tmp = nums.pop()
            counts[tmp] += 1
            
            if counts[tmp] > n//2:
                return tmp
```

```python
// 책 풀이 - count() 활용, 메모제이션을 이용한 다이나믹 프로그래밍
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        n = len(nums)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
                
            if counts[num] > len(nums) //2:
                return num
```

84) 괄호를 삽입하는 여러가지 방법
- [Different Ways to Add Parentheses - LeetCode](https://leetcode.com/problems/different-ways-to-add-parentheses/)

#### 출처
- 파이썬 알고리즘 인터뷰