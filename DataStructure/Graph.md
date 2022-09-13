# Graph 그래프

- 20세기에 출현한 위상수학에서 다루는 이론 중 하나
- 그래프 이론에서 그래프란, 객체의 일부 쌍들이 "연관"되어 있는 객체 집합 구조를 말한다.
- `쾨니히스베르크의 다리 문제` 를 연구하며 레온하르트 오일러가 발표한 논문이 그래프 이론의 시초라고 한다.
  - 다리 문제에서 강으로 구분된 땅을 정점(Vertex)으로, 각 땅을 연결하는 다리를 간선(Edge)으로 간주하여, 다리 문제를 도식화한 것이 그래프 구조의 원형이라 할 수 있다.
---
### 오일러의 정리(Euler's Theorem)
- 오일러는 **모든 정점이 짝수 개의 차수를 갖는다면, 모든 다리를 한 번씩 건너서 도달하는 것이 성립한다**고 말했다. 이를 오일러의 정리라고 부른다. (증명은 발표 100년 뒤에 완성)
- 다리 문제에서는 모든 정점이 짝수개의 차수를 갖지 않으므로, 모든 다리를 한 번씩 거쳐갈 수 없다.

### 오일러 경로(Eulerian Trail/Path)
- **모든 간선을 한 번씩** 방문하는 유한 그래프Finite Graph를 일컫는다. 
- 한 붓 그리기를 예로 들 수 있다.

### 해밀턴 경로
- **각 정점을 한 번씩** 방문하는 무향 또는 유향 그래프 경로를 말한다.
- 최적 알고리즘이 없는 대표적인 NP-완전Complete 문제다.
- 결정 문제(Decision Problem)로 다항 시간에 정답을 검증할 수 있다.
- 즉, NP 문제이면서 NP-난해 문제다.

### 해밀턴 순환(Hamiltonian Cycle)
- 해밀턴 경로 중에서도 원래의 출발점으로 돌아오는 경로를 말한다.

### 외판원 문제(Travelling Salesman Problem, TSP)
- ⭐이론 컴퓨터 과학 분야의 매우 중요한 문제 중 하나!
- 외판원 문제는 각 도시를 방문하고 돌아오는 가장 짧은 경로를 찾는 문제이다.
- 이 문제는 **최단 거리인 해밀턴 순환을 찾는 문제**이며, NP-난해Hard 문제에 속한다.
  - 결정 문제가 아니므로, NP 문제가 아닐 수 있다.
  - 즉, 증명할 수 있는 NP-난해 문제이지만, NP 문제가 아닐 수 있으므로 NP-완전 문제가 아니다.

- 외판원 문제의 **브루트 포스 솔루션의 시간 복잡도는 O(n!)** 이다.

- **다이나믹 프로그래밍** 기법을 활용해 보다 최적화를 꾀할 수 있다. → **시간 복잡도 O(n^2 x 2^n)** 로 최적화

---
## 그래프의 요소
- Vertex 정점 
- Edge 간선
   
## 그래프의 표현
### Adjacency Matrix 인접 행렬

### Adjacency List 인접 리스트
- 출발 노드를 키로 도착 노드를 값으로 표현할 수 있다.
- 도착 노드는 여러 개가 될 수 있으므로 리스트 형태가 된다.

---
# Graph Traversals 그래프 순회/탐색

그래프를 탐색하며, 각 정점을 방문하는 과정을 말한다.

## DFS (Depth-First Search) 깊이 우선 탐색
- 스택 혹은 재귀로 구현한다. 
  - 재귀로 구현시 코드가 더 간단하다는 장점이 있다.
- BFS 에 비해 더 널리 쓰인다.
- 특히, 백트래킹과 함께 사용하면 뛰어난 효용을 보인다.

### 재귀를 이용한 구현
- 정점 v의 모든 인접 (유향) 간선들을 확인해 다음 정점을 방문한다.
```python
class Traversal():
    graph = {}

    def __init__(self, graph={}):
        self.graph = graph

    def recursive_dfs(self, v, discovered=[]):
        discovered.append(v)
        # 정점 v 의 모든 인접 정점을 하나씩 접근
        for w in self.graph[v]:
            # 인접 정점이 이미 지나온 정점이 아니면
            if w not in discovered:
                # 해당 정점부터 재귀적으로 깊이 탐색
                discovered = self.recursive_dfs(w, discovered)
        # 방문했던 정점을 누적하기 위해서 리턴한다.
        return discovered   

```
### 스택을 이용한 구현
- 하나의 정점에서 인접간선들을 모두 거쳐 도착하는 정점을 다시 스택에 담는 형식으로 순회를 반복한다.
- 직관적이라 이해가 더 쉽다.
- 속도 또한 더 빠르다.
  
```python
def iterative_dfs(self, v):
    stack = [v]
    discovered = []

    while stack:
        v = stack.pop()
        # 정점 v를 방문 리스트에 추가
        # if v not in discovered:
        discovered.append(v)
        # 정점 v의 모든 인접 정점을 다시 스택에 쌓는다.
        for w in self.graph[v]:
            if w not in discovered:
                stack.append(w)
    return discovered
```
## BFS (Breadth-First Search) 너비 우선 탐색
- 큐를 이용해 구현한다.
- 재귀로는 구현되지 않는다.
- DFS 보다 쓰임새는 적지만, **그래프의 최단 경로**를 구하는 다익스트라 알고리즘 문제 등에 활용된다.

### 큐를 이용한 구현
- 모든 인접 간섭을 추출하고 도착점인 정점을 큐에 삽입하는 방식으로 구현한다.
- 지금은 리스트의 pop(0) 연산으로 큐의 연산을 구현했지만, 데크 자료형을 이용하여 최적화할 수 있다.
  
```python
def iterative_bfs(self, v):
    discovered = [v]
    queue = [v]

    while queue:
        v = queue.pop(0)
        # 정점 v의 인접 정점 순회
        for w in self.graph[v]:
            if w not in discovered:
                queue.append(w)
                discovered.append(w)
    return discovered
```
### 결과비교
```python
def main():
    graph = {
        1: [2, 3, 4],
        2: [5],
        3: [5],
        4: [],
        5: [6, 7],
        6: [],
        7: [3],
    }
    discovered_recur = recursive_dfs(1, graph)
    discovered_iter = iterative_dfs(1, graph)
    discovered_bfs = iterative_bfs(1, graph)
    print(f"결과 : {discovered_recur}, {discovered_iter}, {discovered_bfs}")

if __name__ == "__main__":
    main()

# 결과 : [1, 2, 5, 6, 7, 3, 4], [1, 4, 3, 5, 7, 6, 2], [1, 2, 3, 4, 5, 6, 7]
```
- 재귀로 구현한 DFS는 사전식 순서(Lexicographical Order)로 방문한다.
- 한편, 스택으로 구현한 경우에는 스택의 특징으로 인해서, 주어진 간접 정점 리스트의 역순으로 그래프의 정점(노드)들을 방문한다.

---
## Backtracking 백트래킹
- 해결 방안 후보를 탐색해 나가다가 가능성이 없다고 판단되는 즉시, 후보를 포기(backtrack 백트랙)하고, 다른 정답 후보를 찾아가는 범용적인 알고리즘을 말한다.
- 제약 충족 문제에 특히 유용하다.

백트래킹은 DFS와 같은 방식으로 탐색하는 모든 방법을 뜻하며, DFS는 백트래킹의 골격을 이루는 알고리즘이다.

주로 재귀로 구현되며, 알고리즘마다 조금씩 변형이 있지만 모두 DFS의 범주에 속한다.

최악의 경우, 모든 경우를 다 거치게 되므로, 브루트 포스와 유사한 점이 있다. 하지만, 한 번 방문 후 가능성이 없는 경우에는 바로 후보를 포기한다는 점에서 매번 같은 경로를 방문하는 브루트 포스보다는 발전된 방식이다.

## 트리의 가지치기(Pruning)
- 트리 탐색의 최적화 문제와 관련이 깊다.
- 트리 탐색 시, 가능성이 없는 후보를 즉시 포기하고 백트랙킹 해, 트리의 불필요한 부분을 버리는 것을 일컫는다.

## Constraint Satisfaction Problems(CSP) 제약 충족 문제
- 수많은 제약 조건을 충족하는 상태를 찾아내는 수학 문제를 일컫는다.
    -예를 들면, 스도쿠Sudoku와 같이 1에서 9까지 숫자를 한 번만 넣는(제약 조건) 정답(충족 상태)을 찾아내는 유형의 문제를 말한다.
- 합리적 시간 내에 문제를 풀기 위해 휴리스틱과 조합 탐색 같은 개념을 함께 결합해 문제를 풀이한다.
- 가지치기를 통해 제약 충족 문제를 최적화하므로, CPS 문제를 해결하기 위해 백트랙킹은 필수적인 알고리즘이다.

---
참고자료)
1. 파이썬 알고리즘 인터뷰, 박상길 저