# 다이나믹 프로그래밍

- 문제를 각각의 작은 문제로 나누어 해결한 결과를 저장해뒀다가 나중에 큰 문제의 결과와 합하여 풀이하는 알고리즘이다.
- 문제의 최적 해결 방법이 **부분 문제에 대한 최적 해결 방법으로 구성**되는 경우, 즉 **최적 부분 구조Optimal Substructure**를 갖고 있는 문제를 풀이할 수 있다.

## 재귀 알고리즘 분류

대부분의 재귀 알고리즘은 **최적 부분 구조** 문제를 풀 수 있다.

- 최적 부분 구조를 푸는 또 다른 알고리즘으로는 그리디 알고리즘과 분할 정복 알고리즘이 있다.

### 그리디 알고리즘

항상 그 순간에 최적이라고 생각되는 것을 선택하면서 풀이한다.

- 다익스트라 알고리즘
- 분할 가능 배낭 문제는 '**탐욕 선택 속성**'이 있기 때문에 그리디 알고리즘을 활용한다.

### 다이나믹 프로그래밍

**중복된 하위 문제Overlapping Subproblem**들의 결과를 저장해뒀다가 풀이해 나간다.

- 0-1 배낭 문제, 피보나치 수열, 다익스트라 알고리즘

### 분할 정복 알고리즘

- **병합 정렬, 퀵 정렬**은 '중복된 하위 문제들'을 푸는 것이 아니기 때문에 다이나믹 알고리즘이 아닌 분할 정복 알고리즘으로 분류된다.

# Leet Code
- 85) 피보나치 수
- [Fibonacci Number - LeetCode](https://leetcode.com/problems/fibonacci-number/)

#### 출처
- 파이썬 알고리즘 인터뷰