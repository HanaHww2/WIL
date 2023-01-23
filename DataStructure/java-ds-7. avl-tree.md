AVL 트리는 스스로 균형을 잡는 이진 트리 자료 구조를 말한다.

AVL 트리에서는 **왼쪽과 오른쪽의 높이 차이가 항상 1보다 작거나 같아야(≤1)** 한다.

<img width=500 src='https://user-images.githubusercontent.com/62924471/214096770-2d869edd-d4ca-46d6-98a5-ec51a258dde0.png'>

- 상단 좌측의 트리에서 왼쪽과 오른쪽의 높이의 차이가 1보다 크기 때문에, 즉, 2가 되므로 **AVL 트리의 규칙을 위반**한다.

# 노드

```java
public class AVLTree<E> {

    Node<E> root;
    int currentSize;

    public AVLTree() { // AVL 트리의 클래스 생성자
        root = null;
        currentSize = 0;
    }

    class Node<T> {
        T data;
        Node<T> left;
        Node<T> right;
        Node<T> parent; // 트리 구현을 간단히 하기 위해 부모 포인터 추가

        public Node(T obj) {
            data = obj;
            parent = left = right = null;
        }
    }
}
```

# add 메소드

```java
/*
* 트리에 요소를 추가하는 메소드
* */
public void add(E obj) {
    Node<E> node = new Node<E>(obj);
    if (root==null) { // 트리가 비어있으면 노드를 루트에 추가
        root = node;
        currentSize++;
        return;
    }
    // 트리에 노드가 있을 경우, add 메소드를 재귀로 호출
    add(root, node);
}

/*
* 재귀 add 메소드
* */
private void add(Node<E> parent, Node<E> newNode) {

    // newNode의 data가 parent의 data보다 크면, 트리의 오른쪽에 추가
    if ( ((Comparable<E>) newNode.data).compareTo(parent.data) > 0 ) {
        if (parent.right == null) { // parent의 right가 비어있다면,
            parent.right = newNode;
            newNode.parent = parent;
            currentSize++;
        } else { // parent의 right가 비어있지 않다면, 재귀 호출
            add(parent.right, newNode);
        }
    // newNode의 data가 parent의 data보다 작거나 같으면, 트리의 왼쪽에 추가
    } else {
        if (parent.left == null) {
            parent.left = newNode;
            newNode.parent = parent;
            currentSize++;
        } else {
            add(parent.left, newNode);
        }
    }
    // 요소를 추가한 다음, AVL트리 규칙에 잘 맞는지 확인
    checkBalance(newNode);
}
```

# 균형 확인 메소드

균형 확인 메소드를 이용하여 AVL 트리 규칙을 만족하는지 확인한다.

- AVL 트리에서는 왼쪽과 오른쪽의 높이 차이가 항상 1보다 작거나 같아야 한다.
- 노드를 추가하였을 때, 균형을 확인하여 불균형이 있다면, 회전을 통해 트리의 균형을 맞춰준다.

```java
/*
* AVL 트리 규칙을 만족하는지 확인한다.
* */
private void checkBalance(Node<E> node) {
    if (((height(node.left) - height(node.right)) > 1) ||
            ((height(node.left) - height(node.right)) < -1)) {
        rebalance(node);
    }
    if (node.parent == null) return; // 부모 노드가 없다면, 리턴
    checkBalance(node.parent);
}
```

# rebalance 메소드

AVL 트리 규칙을 만족하도록 회전을 수행한다.

```java
/*
 * AVL 트리 규칙을 만족하도록 트리의 회전을 수행한다.
 * 어느 쪽에서 균형이 깨졌는지 확인하고 그에 따라 적절히 회전을 하여 균형을 유지하는 기능을 수행한다.
 * */
private void rebalance(Node<E> node) {
    if (((height(node.left) - height(node.right)) > 1)) {
        // 좌편향 트리인 경우, 우측 회전
        if (heigt(node.left.left) > height(node.left.right)) node = rightRotate(node);
        // 왼쪽 자식의 오른쪽 서브트리가 불균형을 야기한 경우, 좌측-우측 회전
        else node = leftRightRotate(node);
    } else {
        // 우편향 트리인 경우, 좌측 회전
        if (heigt(node.right.right) > height(node.right.left)) node = lefttRotate(node);
        // 오른쪽 자식의 왼쪽 서브트리가 불균형을 야기한 경우, 우측-좌측 회전
        else node = rightLeftRotate(node);
    }
    if (node.parent == null) root = node;
}
```

# adding data 예제

```java

```
