# 특징

포인터를 사용하여 여러 개의 노드를 연결하는 자료 구조를 연결 리스트라고 한다. 스택과 큐를 만들기 위해 사용할 수 있다.

- 연결 리스트의 기본 구성 요소는 **노드**이다.
    - 노드는 두 가지 정보를 포함한다.
        - 인접한 노드를 가리키는 **next**라는 이름의 포인터
            - 마지막 노드의 next는 가리킬 다음 노드가 없으므로, null 값을 갖는다.
        - 노드에 넣는 **데이터**(객체)를 가리키는 포인터
- 리스트는 **head**라는 이름의 포인터에서 시작하며, 우리가 아는 정보는 head 뿐이다.
    - head는 리스트의 첫 번째 노드를 가리키는 포인터다.
    - head.next 혹은 head.next.data 와 같이 노드의 내용을 탐색할 수 있다.
    - 편의를 위해 위와 같은 방식 대신, 임시 포인터를 이용해 탐색할 수 있다.
- 자바에서 구현된 ArrayList와 비교하면, 인덱스가 없어서 탐색 속도가 떨어진다.
- 자바에서 구현된 LinkedList(양방향 연결 이용)를 이용하면 인덱스 검색 메소드 존재하는 것 같으나, 내부적으로 실제로는 순차 탐색을 이용해 검색하게 된다.
- 탐색 또는 정렬을 자주 하는 경우엔 배열을 사용하고 데이터의 추가/삭제가 많은 경우 연결 리스트를 사용하는 것이 좋다.

# 구현

### LinkedList 클래스

```java
public class LinkedList<E> implements ListI<E> {

    // 노드 정의
    // TODO 내부 클래스
    // 내부 클래스로 외부에서 접근할 수 없다.
    class Node<E> {
        E data;
        Node<E> next;
        public Node(E obj){
            data=obj;
            next=null;
        }
    }
    private Node<E> head;
    private Node<E> tail;
    /*
    노드 개수를 세는 변수
    크기 변수를 만들어둠으로써, 리스트의 크기 확인이 필요한 경우, O(n)에서 O(1)로 시간이 단축된다.
    즉, 연결 리스트의 크기를 상수 시간으로 알 수 있게 해준다.
    */
    private int currentSize;

    // default 연결리스트 생성자
    public LinkedList() {
        head = tail = null;
        currentSize = 0;
    }
    public int getCurrentSize() {
        return this.currentSize;
    }
    /*
    리스트의 처음에 새 노드 추가
    시간 복잡도는 상수 시간, O(1)이다.
    head가 기존에 가리키던 node 요소가 있었다면, 이를 새로운 노드가 가리키게 한 다음에 head가 새로운 노드를 가리키도록 한다.
    head가 먼저 새로운 node를 가리키게 한다면, 기존에 head가 가리키던 노드의 주소가 유실되고 기존 노드를 참조하는 곳이 사라져서
    이 기존 요소는 가비지 컬렉션의 대상이 될 것이다. 즉, 자료의 손실이 발생한다.
     */
    public void addFirst(E obj) {
        Node<E> node = new Node<E>(obj);
        if (head==null) tail = node;
        node.next = head;
        head = node;
        currentSize++;
    }

    /*
    * 임시 포인터를 이용해 리스트의 마지막에 새 노드 추가
    * 시간 복잡도는 O(n)이다.
    * head 가 null인 경우, 분기를 해서 NullPointerException을 회피한다.
    * 임시 포인터를 이용해 head가 가리키는 첫번째 노드부터 while 반복문을 이용해 그 다음 노드를 확인한다. 다음 노드가 없다면, 그 위치에
    * 새롭게 생성한 노드를 삽입한다.
    * */
    public void addLastWithoutTail(E obj) {
        Node<E> tmp = head;
        Node<E> node = new Node<E>(obj);
        if (head==null) {
            head = node;
            currentSize++;
            return;
        }
        while (tmp.next!=null) {
            tmp = tmp.next;
        }
        tmp.next = node;
    }
    /*
    * tail 포인터를 이용해 리스트 마지막에 새 노드 추가
    * 시간 복잡도는 O(1)이다.
    * tail 포인터를 글로벌 변수로 생성한다. 리스트에서 노드의 추가/삭제가 있을 때마다 포인터를 수정해야 하므로,
    * 이를 구현하기 위한 복잡도가 증가한다. 그러나, 여전히 tail 포인터를 활용하는 것이 보다 효율적이다.
    * */
    public void addLast(E obj) {
        Node<E> node = new Node<E>(obj);
        if (head==null) {
            head = tail = node;
            currentSize++;
            return;
        }
        tail = tail.next = node;
        currentSize++;
    }

    /*
    *
    * */
    public E removeFirst() {
        // 1. 자료구조가 비었을 경우, NullPointerException 방지
        if (head==null) return null;

        E tmp = head.data;

        //2. 요소가 한 개인 경우, if (head.next = null) or if (currentSize == 1) 등의 조건문으로 확인 후 처리
        if (head==tail) head = tail = null;
        else head = head.next; // 기존에 head 객체가 가리키던 노드는 가리키는 포인터가 사라져 가비지 컬렉션의 대상이 된다.

        currentSize--;
        return tmp; // 삭제 대상 노드 반환
    }

    /**/
    public E removeLast() {
        // 1.
        if (head == null) return null;
        // 2. && 3.
        if (head == tail) return removeFirst();

        // 2가지 임시 포인터 선언
        // 현재 위치 노드를 가리키는 포인터와 그 이전 노드를 가리키는 포인터
        Node <E> current = head, previous = null;

        // 4. 마지막 노드 탐색, (current.next!=null)로 대체 가능
        while (current!=tail) {
            previous = current;
            current = current.next;
        }
        previous.next = null; // 삭제될 노드를 가리키는 포인터 제거
        tail = previous; // tail 포인터가 가리키는 마지막 노드 변경

        currentSize--;
        return current.data;
    }

    public E remove(E obj) {
        Node <E> current = head, previous = null;

        while (current!=null) { // 1. 빈 자료구조일 경우 while 구문을 거치지 않고 null 리턴
            if (((Comparable<E>) obj).compareTo(current.data) == 0) {
                // 2. && 3.
                if (current == head) return removeFirst();
                // 4.
                if (current == tail) tail = previous; // return removeLast();

                // 5. 중간에 있는 데이터 다루기기
               previous.next = current.next;
                currentSize--;
                return current.data;
            }
            previous = current;
            current = current.next;
        }
        // 지우고자 하는 데이터가 없을 경우
        return null;
    }

    /*
    * Comparable 인터페이스를 사용하여 노드를 찾는다.
    * 객체의 타입에 따라 실제로 compareTo() 메소드의 구현이 필요할 것이다.
    * 객체의 주소값 비교가 아닌, 객체가 가진 id와 같은 고유한 값으로 비교할 수 있게 한다.
    * */
    public boolean contains(E obj) { // find(), has() 등으로 함수를 네이밍 할 수 있다.
        Node <E> current = head;

        // 1. 빈 자료구조일 경우 while 구문을 거치지 않고 false 리턴
        while (current!=null) {
            if (((Comparable<E>) obj).compareTo(current.data) == 0) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    /*
    * 하나의 요소를 살펴보기 위해 쓰는 메소드
    * */
    public E peekFirst() {
        if (head == null) return null;
        return head.data;
    }
    /*
    * O(1)의 상수 시간 복잡도를 가진다.
    *  */
    public E peekLast() {
        if (tail==null) return null;
        return tail.data;
    }
    /*
    * 처음부터 끝 노드까지 탐색하므로, O(n)의 시간 복잡도를 가진다.
    * */
    public E peekLastWithoutTail() {
        if (head==null) return null;
        Node <E> tmp = head;

        while (tmp.next!=null) {
            tmp = tmp.next;
        }
        return tmp.data;
    }
}
```

### ListI 인터페이스

```java
public interface ListI<E> extends Iterable<E> {
    void addFirst(E i);
    void addLast(E obj);
    E removeFirst();
    E removeLast();
    E remove(E obj);
    boolean contains(E obj);
    E peekFirst();
    E peekLast();
}
```

### 테스트

```java
// 메인 메서드를 이용한 간단 테스트
import me.study.structure.LinkedList;
import me.study.structure.ListI;

public class LinkedListTest {
    public static void main(String[] args) {
        ListI<Integer> list = new LinkedList<>();
        int n = 10;

        // 연결 리스트를 만든다
        for(int i=0; i<n; i++) list.addFirst(i);

        // 연결 리스트를 제거한다
        for(int i=n-1; i>=0; i--) {
            int x = list.removeFirst(); // removeLast도 가능
            boolean y = (i==x)? true:false;
            System.out.println(x + ", "+ y);
        }

        for(int i=0; i<n; i++) list.addLast(i);
        System.out.println(((LinkedList<Integer>) list).getCurrentSize());

        // 구현체에만 정의된 메소드의 경우
        ((LinkedList<Integer>)list).addLastWithoutTail(100);
    }
}
```

# Iterable 인터페이스

Iterable 인터페이스를 구현하면, for(E item : list) 형태의 for-each 구문을 사용할 수 있다. 

```java
public class IterableEx{
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        for (int i = 0, len = arr.length; i < len; i++) {
            System.out.println(arr[i]);
        }
        for (int x : arr) { // Iterable 인터페이스 구현시 가능한 for each문
            System.out.println(x);
        }
    }
}
```

## Iterable<E> 관련 구현 추가

Iterable<E> 인터페이스를 ListI<E> 인터페이스가 상속하고 있다.

- Iterable 인터페이스를 구현하기 위해서는, Iterator 구현 객체를 반환하는 iterator() 메소드를 구현해야 한다.
    - 그 외 메소드들은 디폴트 메소드로 인터페이스 내에 구현되어 있다.
    - iterator() 메소드 구현을 위해 자료 구조 객체 내에 Iterator 인터페이스를 구현하는 클래스를 작성한다.
        - 이하 작성된 메소드 외의 메소드들은 인터페이스 내에 디폴트로 구현되어 있다.

```java
public class LinkedList<E> implements ListI<E> {

    // Iterator 인터페이스를 구현한 IteratorHelper 내부 클래스
    class IteratorHelper implements Iterator<E> {
        Node<E> index;
        public IteratorHelper() { // 생성자
            index = head;
        }
        @Override
        public boolean hasNext() {
            return (index!=null);
        }
        @Override
        public E next() {
            if (!hasNext())  throw new NoSuchElementException();
            E val = index.data;
            index = index.next;
            return val;
        }
    }
    // Iterable 인터페이스(ListI 인터페이스가 상속)의 구현 메소드
    @Override
    public Iterator<E> iterator() {
        return new IteratorHelper();
    }
		...
		// 이하 상단 구현과 동일
}
```

# Doubly Linked Lists 이중 연결 리스트

**단일 연결 리스트에 바로 전의 노드를 가리키는 previous 포인터를 추가한 연결 리스트**다.

노드의 추가/삭제 과정에서 next와 prev 포인터를 동시에 업데이트해 주어야 하므로, 구현이 복잡해진다는 단점이 있다.

![image](https://user-images.githubusercontent.com/62924471/214089790-1f144192-906d-4b0c-a7a4-9d36a344edf5.png)
	
### removeLast() 메소드 시간 복잡도

- **단일 연결 리스트**는 tail 포인터가 있더라도 모든 노드를 한 번씩 거쳐야 한다는 단점이 있었다.  **O(n)의 시간 복잡도**를 가진다.
- **이중 연결 리스트**는 tail 포인터가 가리키는 노드에서 **previous 포인터**가 가리키는 노드를 찾으면 되기 때문에 **시간 복잡도가 O(1)**이 된다.

```java
import java.util.Iterator;

public class DoublyLinkedList<E> implements ListI<E> {

    // 노드 정의
    // 내부 클래스로 외부에서 접근할 수 없다.
    class Node<E> {
        E data;
        Node<E> next;
        Node<E> prev;
        public Node(E obj){
            data=obj;
            next=null;
            prev=null; // 바로 전의 노드를 가리키는 포인터 추가
        }
    }

    private Node<E> head;
    private Node<E> tail;

    /*
    노드 개수를 세는 변수
    크기 변수를 만들어둠으로써, 리스트의 크기 확인이 필요한 경우, O(n)에서 O(1)로 시간이 단축된다.
    즉, 연결 리스트의 크기를 상수 시간으로 알 수 있게 해준다.
    */
    private int currentSize;

    // default 연결리스트 생성자
    public DoublyLinkedList() {
        head = tail = null;
        currentSize = 0;
    }

    /*
    * prev 포인터를 활용하므로, O(1) 시간 복잡도 소요
    * */
    @Override
    public E removeLast() {
        // 경계 조건 1.
        if (head == null) return null;
        // 2. && 3.
        if (head == tail) return removeFirst();

        E tmp = tail.data;

        tail.prev.next = null; // 삭제될 노드를 가리키는 이전 노드의 next 포인터 제거
        tail = tail.prev; // tail 포인터가 이전 노드를 가리키도록 변경, 마지막 노드는 가비지 컬렉션 대상이 된다.

        currentSize--;
        return tmp;
    }

    @Override
    public void addFirst(E obj) {
        Node<E> node = new Node<E>(obj);
        if (head==null) tail = node;

        node.next = head;
        head.prev = node; // 기존 첫 노드(head or node.next)의 prev가 삽입된 노드를 가리키도록 설정
        head = node; // head가 가리키는 위치를 새로 삽입된 노드로 이동
        currentSize++;
    }

    /*
    * 리스트 중간에 삽입하는 경우
   * */
    public void add(E obj, int index) {
        if (index == 0) {
            addFirst(obj); // 1. 2. 3.
            return;
        } else if (index==currentSize) {
            addLast(obj); // 4.
            return;
        } else if (index>currentSize) throw new IndexOutOfBoundsException();

        Node<E> node = new Node<E>(obj);

        // 삽입할 위치의 노드 찾기
        Node<E> tmp = head;
        for(int i = 0; i < index; i++) tmp = tmp.next;

        // 포인터 스왑
        node.next = tmp;
        node.prev = tmp.prev;
        node.prev.next = node;
        tmp.prev = node;
        currentSize++;
    }

		... 이하 구현 생략
}
```

# Circular Linked Lists

원형 연결 리스트는 **마지막 노드의 next 포인터가 연결 리스트의 다른 노드를 가리키는 연결 리스트**를 말한다.

<img src='https://user-images.githubusercontent.com/62924471/214090050-161ac11e-0203-4e05-899a-cae2b8757e5e.png' width='400'>
			 
### 원형 구조 파악

- 마지막 노드의 next 포인터가 **head**를 가리키는 경우
    - tail 포인터를 사용할 경우, 시간 복잡도는 O(1)이다.
        - if ( tail.next == head) 와 같이 조건을 주어 확인할 수 있다.
    - tail 포인터가 없는 경우, head에서 시작하여 임시 포인터를 이동시키며 전체 리스트를 탐색한다. 시간 복잡도는 O(n)이다.
        - iterate until tmp == null || tmp == head ( 또는 tmp.next == null )
- 마지막 노드의 next 포인터가 **임의의 노드**를 가리키는 경우
    - tail에서 시작하여, tail.next가 null이 아닌지 우선 확인하다. 
    null 이 아니면, 리스트를 순회하여 tail 포인터가 다시 나타나는지 확인한다. 시간 복잡도는 O(n)이다.
    - tail 포인터가 없는 경우에는, 임시 포인터 2개를 사용한다. 
    순회 시작 노드(head)에 임시 고정 포인터를 두고, currentSize만큼 떨어진 노드까지 임시 포인터를 이동시키며 순회하며 임시 고정 포인터를 다시 만나는지 확인한다. 
    임시 고정 포인터를 다시 만나지 못했다면,  임시 고정 포인터를 다음 노드로 옮기고, 다시 순회하며, 임시 고정 포인터를 만나는지 확인한다. 
    원형 구조를 파악하기 위해, 임시 고정 포인터를 옮겨가며 반복한다. 시간 복잡도는 O(n^2)이다.
