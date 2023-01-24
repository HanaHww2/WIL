## 시작
첫번째 과정은 짤막한 조각 영상들로 구성되어 있다.

자료구조를 학습하기 전 알아야 할 기본적인 지식들을 제공하는 파트로, 알아야 할 필수적인 부분만 간략히 볼 수 있게 영상을 편집한 것 같다.

그렇다 보니, 정리 노트도 단편적으로 작성이 되었다.😂

# Generic Programming

- Class 를 만들면, Object 클래스의 equals(), toString(), hashcode() 를 오버라이딩한다.
- Object 클래스는 객체의 메모리 위치만으로 위 메소드들을 수행한다.

## Parameterized Type / Generic Type

- 컬렉션은 제네릭 타입이다.
- 보통 E, T 기호를 이용한다. 각각 Element, Type를 의미한다.
- 주의) Constructor 생성자에는 제네릭 타입을 작성하지 않는다.

```java
public class LinkedList<E> implements List<E> {

    class Node<E>{
        E data;
        Node<E> next;
        public Node(E obj){
            data=obj;
            next=null;
        }
    }

    private Node<E> head;
    private Integer currentSize;

    public LinkedList() {
        head=null;
        currentSize = null;
    }
}
```

- 제네릭 타입을 이용해 배열을 생성할 때도 주의가 필요하다.

```java
E[] storage = (E[]) new Object[size]; // 이용 가능
E[] storage = new E[size]; // 컴파일되지 않는다.
```

- 참고) [https://www.baeldung.com/java-generic-array](https://www.baeldung.com/java-generic-array)

- 아래 코드는 위 글에서 가져왔다. 아래는 어설픈 번역이므로 원문을 참고하길 바란다.
- 원문에서는 컴파일 오류가 나지 않을 거라 가정하고, 제네릭 타입 배열 작성법에 대한 이유를 설명한다.

```java
public <T> T[] getArray(int size) {
    T[] genericArray = new T[size]; // suppose this is allowed
    return genericArray;
}

String[] myArray = getArray(5);
```

- unbound generic type은 런타임에서 **Object 타입**으로 해석될 것이다.
- 위와 같이 getArray() 메소드 호출시, 컴파일러에 의한 암시적 형변환(cast)은 실패하게 된다.
- 결과적으로 ClassCastException 라는 런타임 오류가 발생한다.

# Comparisons

### equals()

- Object 클래스의 equals는 메모리 주소를 비교한다.
- String 클래스는 equals를 오버라이드해서, 메모리 주소 대신 문자열을 비교한다.

## Comparable<T> 인터페이스

- compareTo라는 하나의 method를 갖는다. 즉, 구현 시에 compareTo() method만 구현하면 된다.

```java
public int compareTo(T obj)
...
// 사용 예시
a.compareTo(b);
```

- 리턴하는 결과값은 아래를 따른다.
    - if( a < b ) retrun < 0;
    - if( a = b ) retrun 0;
    - if( a > b ) retrun > 0;

```java
if( ((Comparable<T>) data).compareTo(obj)==0 )
```

- 위와 같이 활용할 수 있다.

# Autoboxing

- primitive 타입에 대해 Java 가상 머신은 정확하게 필요한 만큼의 메모리를 할당한다. 하지만 객체에 대해서는 이 객체를 가리키는 4바이트짜리 포인터와 힙의 공간을 할당하게 된다.
- Java 컴파일러는 autoboxing을 이용해서 이 둘을 적절히 바꾸는 과정을 거쳐 코드를 수행한다. (비용 발생)

# Exception 처리

```java
public class YourException extends Exception {
  public YourException() {
    super();
  }
  public YourException(String s) {
    super(s);
  }
}

throw new YourException("Your code sucks!");
//으로 에러를 발생시켜서 활용할 수 있다.
//이런 에러 메세지 보면 눈물날 거 같...
```

# Iterable, Iterator 인터페이스 구현 관련

### 자바 1.8 에서의 주요 변경사항

이었던 것...ㅎㅎ

1. 인터페이스가 기본으로 구현된 메소드를 가질 수 있게 되었다.
    - Iterator 인터페이스에는 remove() 메소드가 정의되어 있다.
    - 자바 1.8의 기본 구현은 UnsupportedOperationException을 발생 시킨다.
        
        ```java
        public void remove() // 사용되지 않는 메소드
        		throw new UnsupportedOperationException("remove");
        ```
        
        - 만약 **1.8 이전 버전**을 사용한다면, 이를 직접 구현해주면 된다.
2. Iterator 인터페이스에 forEachRemaining() default 메소드가 존재한다.

### 출처
- [자바로 구현하고 배우는 자료구조](https://www.boostcourse.org/cs204), 부스트코스
