# 자바로 구현하고 배우는 자료구조
- 참고 강의 링크 : [자바로 구현하고 배우는 자료구조](https://www.boostcourse.org/cs204)
- 부스트코스에서 제공하는 강의를 통해 학습하고 정리한 내용을 기록합니다.

0. [자바 자료구조 기본](java-ds-0.%20introduce.md)
1. [자료 구조 경계 조건](java-ds-1.%20boundary-conditions.md)
2. [Arrays 배열](java-ds-2.%20arrays.md)
3. [Linked List 연결리스트](java-ds-3.%20linked-list.md)
4. [Hash 해쉬](java-ds-4.%20hash.md)
5. [Tree 트리](java-ds-5.%20tree.md)
6. [BST 이진 탐색 트리](java-ds-6.%20bst.md) - 이하 구현 코드 보충 예정
7. [AVL Tree 자기균형 트리](java-ds-7.%20avl-tree.md)
8. [RB Tree 적흑 트리](java-ds-8.%20red-black-tree.md)

---
# ADT(Abstract Data Type, 추상 자료형) 구현 방식
- 자료구조는 크게 **메모리 공간 기반의 연속Contiguous 방식**과 **포인터 기반의 연결Link 방식**으로 나뉜다.
- 흔히 말하는 배열은 정적인 크기로 연속된 메모리 공간을 할당받는 연속 방식에 속한다.
- 연결 방식의 기본은 연결 리스트다.
- 추상 자료형의 실제 구현은 대부분 배열 또는 연결 리스트를 기반으로 한다.

---
## Linear Data Structure 선형 자료 구조
- 데이터 요소가 순차적으로 배열되는 자료구조
- 단일 레벨로 구성
- 한 번에 탐색이 가능
- 배열, 스택, 큐, 연결 리스트 등

### Contents
- [배열](./array.md)
- [연결 리스트](./linked-list.md)
- [해시 테이블](./hash-table.md)
---
## Non-Linear Data Structure 비선형 자료 구조
- 데이터 요소가 순차적 혹은 선형으로 배열되지 않는 자료구조를 비선형 자료구조라고 한다.
- 선형과 달리 멀티 레벨로 구성된다.
- 탐색이 복잡하고 선형에 비해 구현하기도 다소 복잡할 수 있으나, 메모리를 더 효율적으로 활용할 수 있다는 장점이 있다.
- 대표적으로 그래프가 존재하며, 트리는 그래프의 범주에 포함된다.

### Contents
- [그래프](./Graph.md)
- [힙](./heap.md)
- [B+Tree](./B%2BTree.md)

#### 트리
#### 힙 Heap
- 트리 기반 자료구조의 특수한 한 형태로, 정렬 알고리즘을 위한 자료구조이다.
#### 트라이 Trie
- 자연어 처리 분야에서 문자열 탐색을 위해 널리 쓰이는 자료구조이다.

