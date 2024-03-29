# ☘스프링

객체 지향적 설계 원칙과 디자인 패턴에 나타난 장점을 자연스럽게 개발자들이 활용할 수 있게 해주는 프레임워크다.

**IoC를 모든 기능의 기초가 되는 기반 기술**로 삼고 있으며, IoC를 극한까지 적용하고 있는 프레임워크다.

- 스프링의 핵심은 **빈 팩토리 또는 애플리케이션 컨텍스트**가 담당한다.
    - 별도의 정보를 참고해 빈(오브젝트)의 생성과 관계 설정 등의 제어 작업을 총괄한다.
    - 스프링에서 빈의 생성과 관계 설정 같은 제어를 담당하는 IoC 오브젝트를 **빈 팩토리**라고 부른다. 보통 빈 팩토리를 더 확장한 **애플리케이션 컨텍스트**를 사용한다.
    - 빈 팩토리 : 빈을 생성하고 관계를 설정하는 IoC의 기본 기능에 초점을 맞춘 용어다.
    - 애플리케이션 컨텍스트 : 애플리케이션 전반에 걸친 구성 요소의 제어를 담당하는 IoC 엔진이라는 의미가 좀 더 부각되는 말이다.
- **스프링 빈**은 스프링 컨테이너가 생성과 관계 설정, 사용 등을 제어하는 **제어의 역전이 적용된 오브젝트**를 가리키는 말이다. 
여기서 빈bean은 자바빈에서 말하는 빈과 비슷한 **오브젝트 단위의 애플리케이션 컴포넌트**를 말한다.

### 프레임워크

프레임워크에서 애플리케이션 코드는 프레임워크에 의해 사용된다.

프레임워크 위에 개발한 클래스를 등록해두고, 프레임워크가 흐름을 주도하는 중에 개발자가 만든 등록된 애플리케이션 코드를 사용하도록 만드는 방식이다.

---
# 자바빈

자바빈(JavaBean)은 원래 비주얼 툴에서 조작 가능한 컴포넌트를 지칭했다. 
그러나, 자바의 주력 개발 플랫폼이 웹 기반의 엔터프라이즈 방식으로 바뀌었고, 자바빈은 자바빈 스타일의 오브젝트를 사용하는 JSP 빈, EJB과 같은 표준 기술과 다양한 오픈소스 기술을 통해 계속 이어져 왔다고 한다.

- 자바빈은 두 가지 관례를 따라 만들어진 오브젝트를 가리킨다.
    - 디폴트 생성자: 파라미터가 없는 디폴트 생성자를 갖고 있어야 한다. 툴이나 프레임워크에서 리플렉션을 이용해 오브젝트를 생성하기 때문이다.
    - 프로퍼티: 자바빈이 노출하는 이름을 가진 속성을 프로퍼티라고 한다. 프로퍼티는 setter, getter 메소드를 이용해 수정 또는 조작할 수 있다.
- 추가로 검색해 본 결과 이외에도, 필드의 접근자는 private으로 하며, 필드의 수정/접근 메소드는 public 접근자를 부여하는 규약이 있다. 또한, 빈이 디폴트 패키지가 아닌 특정 패키지에 속해 있어야 하는 규약들을 확인할 수 있다.

### EJB(Enterprise JavaBeans)

- 엔터프라이즈 자바빈즈는 기업 환경의 시스템을 구현하기 위한 서버 측 컴포넌트 모델이다. 즉, EJB는 애플리케이션의 업무 로직을 가지고 있는 서버 애플리케이션이다.
- 출처) [https://ko.wikipedia.org/wiki/엔터프라이즈_자바빈즈](https://ko.wikipedia.org/wiki/%EC%97%94%ED%84%B0%ED%94%84%EB%9D%BC%EC%9D%B4%EC%A6%88_%EC%9E%90%EB%B0%94%EB%B9%88%EC%A6%88)
  
### 오브젝트 팩토리

객체의 생성 방법을 결정하고, 그렇게 만들어진 오브젝트를 돌려주는 역할을 하는 오브젝트를 **팩토리factory**라고 부른다. 
(이 팩토리는 디자인 패턴에서 말하는 추상 팩토리 패턴이나, 팩토리 메소드 패턴과는 관계없다.)

오브젝트를 생성하는 쪽과 오브젝트를 사용하는 쪽의 역할과 책임을 깔끔하게 분리하는 목적으로 사용한다.

실질적인 로직을 담당하는 컴포넌트, 즉 애플리케이션을 구성하는 컴포넌트의 구조와 관계(의존 관계)를 정의한 설계도 역할을 한다고 볼 수 있다.

---
# 제어의 역전(IoC, Inversion of Control)

스프링 이전부터 존재했던 개념으로, GoF 디자인 패턴 책에서도 이 용어를 볼 수 있다.

- 간단하게는 프로그램의 제어 흐름 구조를 거꾸로 뒤집는 것이라고 설명할 수 있다.
    - 일반적인 프로그램 흐름에서 모든 오브젝트는 프로그램 흐름을 결정하거나 사용할 오브젝트를 구성하는 작업에 능동적으로 참여하며, 모든 종류의 작업을 사용하는 쪽에서 제어한다.
    - main()과 같은 엔트리 포인트를 제외하면 모든 오브젝트는 이렇게 위임받은 제어 권한을 갖는 특별한 오브젝트에 의해 생성되고 사용 및 제어된다.
- IoC를 적용하면 설계가 깔끔해지고, 유연성이 증가해 확장성 또한 좋아진다.
- 제어의 역전에서는 프레임워크 또는 컨테이너와 같이 애플리케이션 컴포넌트의 생성과 관계 설정, 사용, 생명주기 관리 등을 관장하는 존재가 필요하다.
- 폭넓게 사용되는 프로그래밍 모델이다.
    - 책에 나오는 DaoFactory 예제 또한 단순한 IoC 컨테이너 혹은 프레임워크라고 불릴 수 있다.
    - 서블릿이나 JSP, EJB 처럼 컨테이너 안에서 동작하는 구조는 제어의 역전 개념이 적용되어 있다고 볼 수 있다.
        - 서블릿은 그에 대한 제어 권한을 컨테이너가 적절한 시점에 서블릿 클래스의 오브젝트를 만들고, 그 안의 메소드를 호출한다.
    - 템플릿 메소드 패턴이 **제어의 역전**을 활용해 문제를 해결하는 디자인 패턴이라고 볼 수 있다. 
    제어권을  상위 템플릿 메소드에 넘기고, 자신(하위 구현 클래스)은 필요할 때 호출되어 사용되는 방식 때문이다.
    - 프레임워크가 제어의 역전 개념이 적용된 대표적인 기술이다.

### 참고자료)
- 토비의 스프링