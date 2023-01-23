# 트리Tree

![image](https://user-images.githubusercontent.com/62924471/214093785-4f80db2a-6431-4d39-b56a-197335d3dbea.png)

가계도처럼 **노드를 나무 형태로 연결한 구조**를 **트리**라고 부른다. 

트리에 있는 각각의 요소는 노드Node라고 불리며, 노드는 **부모, 자식** 형태로 이어진다.

### 용어

- **뿌리 (root)**
    - 트리의 시작 부분으로, 항상 루트를 시작점으로 두고 트리를 탐색하게 된다.
- **잎 (leaf)**
    - 자식이 딸려 있지 않은 노드를 말한다.
- **간선 (edge)**
    - 두 노드를 연결하는 선을 말한다.
- **레벨 (levels)**
    - 뿌리로부터의 간선의 수에 따라 **level** 을 갖는다.
- **높이 (height)**
    - 루트에서부터 가장 먼 잎까지 가는데 거치게 되는 간선의 개수를 높이로 한다.

### 사용 예

탐색을 목적으로 하는 경우 데이터를 트리 형태로 저장할 수 있다. 디렉터리 구조, 검색 엔진, DBMS, 라우터 알고리즘 등을 예로 들 수 있다.

---
## 완전 트리 Complete Tree
![image](https://user-images.githubusercontent.com/62924471/214093877-ddb9fb78-e4e7-43dc-8716-cb32116dae43.png)

모**든 잎이 아닌 노드가 2개의 자식 노드**를 가지고 있고 **마지막 줄은 왼쪽에서 오른쪽 순서**로 채워져 있는 트리를 말한다.

- **Every non leaf has two children except for the last row**
- **the last row is filled left to right**


### 완전 이진 트리의 특성

완전 이진 트리의 노드에 레벨 순서에 따라 번호를 부여하면, 노드의 위치는 아래와 같다. (루트에는 0을 부여한 경우)

- 자식children : **2 * parent + 1** 또는 **2 * parent + 2**
- 부모parent : **floor((child - 1) / 2)**

## 정 트리 Full Tree
![image](https://user-images.githubusercontent.com/62924471/214093926-42001909-4c10-499d-831f-637ecdb508ba.png)

**모든 잎이 아닌 노드가 2개의 자식 노드**를 가지고 있고 **모든 잎이 같은 레벨**에 있는 트리를 말한다.

- **Every non leaf has two children**
- **All the leaves are on the same level**

## 트리 순회 **Trees Traversal**

트리의 노드에 숫자를 매기는 방식을 말한다.

### 전위 순회 Pre order traversal

- visit root node → visit left child → visit right child
- **루트** 노드에서 시작하여 **왼쪽 자식** 노드에 갔다가 **오른쪽 자식** 노드로 가는 순회 방법입니다. 다른 모든 노드를 지나기 전에 루트 노드를 방문하기 때문에 이름에 전(Pre)이 들어갑니다.

### 중위 순회 In order traversal

- visit left child → visit root → visit right child
- **왼쪽 자식** 노드에서 시작하여 **루트** 노드에 갔다가 **오른쪽 자식** 노드로 가는 순회 방법을 말한다.

### 후위 순회 Post order traversal

- visit left child → visit right child → visit root
- **왼쪽 자식** 노드에서 시작하여 **오른쪽 자식** 노드에 갔다가 **루트** 노드로 가는 순회 방법을 말한다.

### 너비 우선/레벨 순서 순회 Breadth first /level order traversal

**가장 위에 있는 노드에서 시작**하여 **왼쪽에서 오른쪽**으로 가는 순회 방법을 말한다.

---

## 트리 표현

표현식 트리를 활용하여 굉장히 복잡한 식도 트리 형식으로 표현할 수 있다.

- 예 1)
    
    ![image](https://user-images.githubusercontent.com/62924471/214094461-bfbdd736-d616-4d87-8a8c-7c9e0d6ab83b.png)

    - ~~전위(Pre order) 표기식 : * 2 3~~
    - 중위(In order) 표기식 : 2 * 3
    - 후위(Post order) 표기식 : 2 3 *
- 예 2)
    
    ![image](https://user-images.githubusercontent.com/62924471/214094500-20aa914f-480a-49ef-aae0-91215bb1679e.png)
    - 중위(Infix) 표기식: (((22 / 11) + 3) * (6 + 5)) - 50
    - 후위(Postfix) 표기식: 22 11 / 3 + 6 5 + * 50 -
