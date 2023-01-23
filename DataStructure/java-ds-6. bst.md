# 이진 검색 트리(Binary Search Tree, BST)

![image](https://user-images.githubusercontent.com/62924471/214094955-b39ad7bd-82e0-4ada-9a1b-bb14f4a4d22f.png)

- 이진 탐색 트리에서는 부모 노드보다 작은 데이터가 왼쪽 자식 노드에 오고, 부모 노드보다 큰 데이터가 오른쪽 자식 노드에 온다.
- 이진 탐색트리에서 탐색을 하는 경우, 부모 노드보다 작으면 왼쪽, 크면 오른쪽으로 이동하게 되어서 결국 log n의 복잡도를 갖는다.

## 노드 클래스

```java
// 트리 클래스의 inner 클래스
class Node<E> {
	E data;
	Node <E> left, right; // 노드의 포인터, 더하여 parent 포인터를 추가할 수 있다.

	public Node(E obj) {
		this.data = obj;
		left=right=null;
	}
}
```

## add() 메소드

트리에 새로운 요소를 추가하는 add 함수를 재귀 함수로 구현한다.

- 트리에 새로운 데이터를 추가하는 과정
    1. 루트에서부터 시작한다.
    2. **트리의 규칙**에 따라 아래로 내려가며 탐색한다.
    3. **null인 부분**을 만나면, 그 곳에 새로운 노드를 추가한다.

```java
Node<E> root;
int currentSize;

/*
* 외부에 공개하는 add 메소드, 오버로딩 방식
* 직접적으로 트리 노드에 접근하여 수정하는 메소드는 내부에 감춰둔다.
* */
public void add(E obj){

    if (root == null) { // 트리가 비어있을 경우
        root = new Node<E>(obj);
    } else {
        add(obj, root);
    }
    currentSize++;
}

/*
* 트리에 요소를 추가하는 add 메소드
* 트리 내부를 탐색하며 삽입할 위치를 찾아야 하므로, 재귀함수로 구현한다.
* 더하여, 트리 내부를 탐색하는 로직은 트리 클래스 내 모든 메소드들에서 동일하게 만든다. (일관성 유지)
* */
private void add (E obj, Node<E> node) {
    if (((Comparable<E>) obj).compareTo(node.data) > 0) {
        // if obj > node.data, go to the right
        if (node.right == null) {
            node.right = new Node<E>(obj);
            return;
        }
        add(obj, node.right); 
    }
    // if obj <= node.data, go to the left
    if(node.left == null) { 
        node.left = new Node<E>(obj);
        return;
    }
    add(obj, node.left);
}
```

## contains() 메소드

트리에 특정 요소가 포함되어 있는지 확인하는 contains 함수를 재귀 함수로 구현한다.

- 특정 요소가 트리에 포함되어있는지 확인하는 과정
    1. 루트에서부터 시작한다.
    2. **트리의 규칙**에 따라 내려간다.
    3. **요소를 찾으면 True**를 반환하고 **null인 노드**에 다다르면 **False**를 반환한다.

```java
/*
* 사용자들이 접근할 수 있도록 오버로딩한 public method
* */
public boolean contains (E obj){
    return contains(obj, root);
}

/*
* 외부에서 실제 로직과 노드에 접근하지 못하도록 은닉된 private method
* */
private boolean contains (E obj, Node<E> node){
    // 트리의 끝에 도달한 경우
    if (node==null) return false;
    // node의 data가 찾는 값과 일치하는 경우
    if (((Comparable<E>) obj).compareTo(node.data) == 0) return true;
    
    // node의 data가 찾는 값보다 작은 경우, go to the right
    if (((Comparable<E>) obj).compareTo(node.data) > 0) return contains(obj, node.right);
    // else, go to the left
    return contains(obj, node.left);
}
```

## 제거

자식 노드의 개수에 따라 트리의 특정 요소를 제거하는 방법이 달라지며, 각각은 아래와 같다.

1. 잎 노드를 제거할 경우
    - 제거할 노드의 **부모 노드의 포인터를 null**로 설정한다.
2. 자식 노드가 1개인 노드를 제거할 경우
    - 제거할 노드의 **부모 노드의 포인터를 자식 노드**로 향하게 한다.
3. 자식 노드가 2개인 노드를 제거할 경우
    - 중위 후속자와 중위 선임자 중 하나와 자리를 바꾼 후, 자리를 바꾼 노드를 제거한다.

### 중위 후속자(in-order successor)

- 중위 순회 방식으로 노드를 탐색할 때 가장 마지막에 혹은 루트 노드를 방문하기 직전에 만나게 되는 노드이다. 또는 (하위 sub) 트리를 중위 탐색할 때, 가장 마지막에 탐색하게 되는 노드를 말한다.
- 루트 혹은 기준 노드보다 작은 노드들 중에서 가장 큰 노드를 가리킨다.
- 루트 혹은 기준 노드에서 시작하여 왼쪽으로 한 번 내려갔다가 계속 오른쪽으로 내려간 곳의 잎 노드를 말한다.

### 중위 선임자(in-order predessor)

- 중위 후속자와 달리 중위 순회시, 가장 먼저 루트 혹은 기준 노드를 방문한 이후 만나게 되는 노드이다.  또는 (하위 sub) 트리를 중위 탐색할 때, 가장 처음에 탐색하게 되는 노드를 말한다.
- 루트 혹은 기준 노드보다 큰 노드들 중에서 가장 작은 노드를 가리킨다.
- 루트 혹은 기준 노드에서 시작하여 오른쪽으로 한 번 내려갔다가 계속 왼쪽으로 내려간 곳의 잎 노드를 말한다.

## 회전

**균형 잡힌 트리 Balanced Tree**를 만들기 위해 트리의 노드 위치를 바꾸는 과정을 **회전**이라고 한다.

> 연결 리스트처럼 한 방향으로 나열된 트리는 균형 잡혀 있지 않다고 표현한다. 
균형 잡힌 트리에서는 특정 요소를 탐색하는 시간 복잡도가 **O(logn)**이지만, 균형 잡히지 않은 트리에서는 연결 리스트와 같은 **O(n)**이 된다. 
따라서, 이상적으로 트리 구조를 활용하기 위해서 트리를 균형 있게 만들 필요가 있다.
> 

이진 탐색 트리 구조의 간결함과 균형만 맞다면, 검색, 삽입, 삭제 모두 O(logN)의 성능을 보이는 장점이 있기 때문에 지속적으로 개선시키기 위한 노력이 이루어져왔다.

균형 트리에는 AVL Tree, 2-3(-4) Tree, Red-Black Tree, B-Tree 등이 존재한다.

### 균형

회전과 같이 트리를 조작하는 방법 외에도 데이터를 다양한 방식으로 조작하여 트리의 균형을 도모할 수 있다. 예를 들어, 데이터가 정렬된 경우에는 편향 트리가 되므로, 데이터를 적절히 잘 섞어 랜덤성을 유지할 수 있다. 그리고 트리를 생성할 때, 루트 노드로 둘 데이터를 선택하는 다양한 방법 또한 존재한다.

### 우측 회전, 좌측 회전

- 조부모 노드, 부모 노드, 자식 노드의 크기 관계에 따라 **우측 회전**, 혹은 **좌측 회전**을 하게 된다.
- 트리를 재정렬하면 항상 중간 크기의 요소가 가장 위에 있는 루트가 된다.
1. 불균형이 **왼쪽 자식**의 **왼쪽 서브 트리**에서 나타날 경우 ➡ **우측 회전**

    <img width=400 src='https://user-images.githubusercontent.com/62924471/214095518-2c0604e3-eedd-4dd0-a242-f3557798456f.png'>
    
- 크기 관계는 (조부모 노드) > (부모 노드) > (자식 노드)
- **우측 회전**을 하여 조부모 노드를 부모 노드의 **오른쪽 자식 노드 위치로** 옮긴다.

2. 불균형이 **오른쪽 자식**의 **오른쪽 서브트리**에서 나타날 경우 ➡ **좌측 회전**

  ![image](https://user-images.githubusercontent.com/62924471/214095575-d7b8f01f-4d18-462a-8a70-750f1d90dd17.png)
  
- 크기 관계는 (조부모 노드) < (부모 노드) < (자식 노드) 이다.
- **좌측 회전**을 하여 조부모 노드를 부모 노드의 **왼쪽 자식 노드 위치로** 옮긴다.

### 또 다른 경우

우측 회전과 좌측 회전을 모두 사용하여 불균형을 해소한다.

1. 우측-좌측 회전
- 불균형이 **오른쪽 자식**의 **왼쪽 서브 트리**에서 나타날 경우, 부모 노드를 **우측 회전**시킨 다음, 조부모 노드를 **좌측 회전**시킨다.
  <img width=400 src='https://user-images.githubusercontent.com/62924471/214095848-63e5cbf2-dff9-4bc2-bcf1-902a899ec032.png'>
  
2. 좌측-우측 회전
- 불균형이 **왼쪽 자식**의 **오른쪽 서브 트리**에서 나타날 경우, 부모 노드를 **좌측 회전**시킨 다음, 조부모 노드를 **우측 회전**시킨다.
  <img width=400 src='https://user-images.githubusercontent.com/62924471/214095906-aa735851-bfe3-49fa-9cf8-9173e446ef39.png'>
  
즉, **불균형을 야기한 노드의 위치에 따라** 그러한 불균형을 해소할 회전 방식이 정해진다.

## 회전(코드 구현)

```java

```
