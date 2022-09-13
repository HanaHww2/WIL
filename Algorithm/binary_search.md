# Binary Search 이진 검색

- 이진 검색은 **정렬된 배열에서 타겟을 찾는 검색 알고리즘**을 말한다. 
- **값을 찾아내는 시간 복잡도가 O(log n)** 이라는 점에서 대표적인 로그 시간 알고리즘이다.

### Binary Search Tree & Binary Search
- **이진 탐색 트리 BST**와 유사한 점이 많다. 
  - 그러나 이진 탐색 트리가 정렬된 구조를 저장하고 탐색하는 **자료구조**라면, 이진 검색은 정렬된 배열에서 값을 찾아내는 **알고리즘** 자체를 말한다.

### 파이썬 모듈
- 파이썬의 bisect 모듈이 이진 검색 알고리즘을 지원한다. (여러가지 예외 처리가 포함되어 있다.)
  - 원래는 리스트의 삽입 지점을 찾는 모듈이지만, 이진 검색으로 위치를 찾는 데에도 매우 유용하게 활용된다.
> 참고.  
> 파이썬의 index() 메소드는 앞에서부터 차례대로 주어진 값의 인덱스를 찾는 함수로, 탐색에 활용이 가능하다. 그러나 최악의 경우 시간 복잡도가 **O(n)** 이므로 사용에 주의가 필요하다.

### 이진 검색 알고리즘 버그

이진 검색에서 중앙의 인덱스 값을 계산할 때, 왼쪽 끝 인덱스 값과 오른쪽 끝 인덱스 값을 더하고 그 결과를 반으로 나누는 식으로 구현한다. 그러나 이 경우, 컴퓨터 과학에서는 오류가 발생할 소지가 있다.

즉, 두 수를 더하면, 항상 각각의 수보다 큰 수가 되고, 자료형의 최댓값을 초과할 가능성이 발생한다.
만약 int 형을 이용하는 경우, 이를 허용하는 최댓값을 초과하면 오버플로(Overflow)가 발생한다. 

- 그렇기에 중앙값을 구할 때, 두 수의 합을 반으로 나누기 보다는 두 수의 차를 반으로 나누고 낮은 수에 더하여 구한다.

```python
mid = left + (right - left)//2
```

- 다만, 파이썬은 임의 정밀도 정수형을 지원하기 때문에 이 문제에 해당 사항이 없다.
    - 임의 정밀도 정수형이란 무제한 자릿수를 제공하는 정수열을 말한다. 
    - 정수를 배열과 같이 다루며, 2^30 진법으로 만들게 된다. 다만, 임의 정밀도로 숫자를 처리하게 되면 계산 속도가 저하된다. 
    - 파이썬 3부터는 일반 정수형이 사라지고, 임의 정밀도 정수형(bigInt)만 지원된다고 한다. (정수형 통합)
    - ([https://velog.io/@lhr_06/임의정밀도와-자료형-객체](https://velog.io/@lhr_06/%EC%9E%84%EC%9D%98%EC%A0%95%EB%B0%80%EB%8F%84%EC%99%80-%EC%9E%90%EB%A3%8C%ED%98%95-%EA%B0%9D%EC%B2%B4))

# 리트코드

- 65) 이진 검색

[Binary Search - LeetCode](https://leetcode.com/problems/binary-search/)

```python
# 재귀
class Solution:
    def search(self, nums: List[int], target: int) -> int:
				def bin_search(left, right, target):
            if left > right:
                return -1
            
            mid = left + (right - left)//2
            if nums[mid] == target: 
                return mid
            elif nums[mid] > target:
                return bin_search(left, mid-1, target)
            else: 
                return bin_search(mid+1, right, target)

        return bin_search(0, len(nums)-1, target)
```

```python
# 반복
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
```

- 67) 두 배열의 교집합

[Intersection of Two Arrays - LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)

```python
# Built-in 기능
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set2 & set1)
```