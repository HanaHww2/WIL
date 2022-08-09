# Spring MVC 구성요소

## Spring MVC 기본 동작 흐름

![Spring MVC 기본](https://blog.kakaocdn.net/dn/NUAiF/btq9fmVFT25/4QS9OYh1CHJRkxrUxixtA0/img.png)

Spring MVC 기본

- 위 이미지에서 **database 파트를 제외한 파란색 상자들은 모두 Spring MVC가 제공하는 부분들**이다.
- **개발자의 영역은 보라색 상자**이다.
- **녹색 상자, 즉 View 영역**은 Spring이 제공하는 부분 외에 개발자가 만들어야 하는 부분도 존재한다.

### 동작 흐름

1. 클라이언트의 **모든 요청을 DispatcherServlet 객체**가 받는다.
2. DispatcherServlet는 요청을 처리할 **컨트롤러와 메소드**를 HandlerMapping을 통해 확인한다.
    - **매핑 정보**는 xml 파일 혹은 java 파일에 등록된 어노테이션을 이용해 설정하며, 이를 **HandlerMapping 객체들이 관리**하게 된다.
3. DispatcherServlet은 결정된 컨트롤러와 메소드의 **실행을 Handler Adapter에게 요청**한다.
4. 
5. **결과를 Model**에 담아 DispatcherServlet에 전달한다.
6. DispatcherServlet은 컨트롤러가 리턴한 view name과 **ViewResolver를 이용해 적절한 View**를 확인한다.
7. 해당 View에 결과를 출력해 **응답을 완료**한다.

---
## DispatcherServlet

- 프론트 컨트롤러 (Front Controller)
    - 이론적으로는 한 개 이상 사용될 수 있다고 하나, 보통 한 개만 선언해서 사용한다.
- **클라이언트의 모든 요청**을 받아 이를 처리할 핸들러에게 넘기고, 핸들러가 처리한 결과를 다시 받아 **사용자에게 응답 결과**를 보여준다.
- **Spring MVC를 이해**한다는 것은 **DispatcherServlet이 어떻게 동작하는지를 이해**하는 것이라고도 말할 수 있다.
- DispathcerServlet은 여러 컴포넌트를 이용해 작업을 처리한다.

## DispatcherServlet 내부 동작 흐름

![DispatcherServlet 내부 동작 흐름](https://blog.kakaocdn.net/dn/k19Az/btq9e7qYOnK/wSZc2ecDbqOKlTIYFv4KI0/img.png)

## DispatcherServlet 내부 동작흐름 상세
### 요청 선처리 작업

![DispatcherServlet 내부 동작흐름 상세 - 요청 선처리 작업](https://blog.kakaocdn.net/dn/bveUP3/btq9hArIaZy/BNsheFKiX3n5ajD2Y3SVd0/img.png)

#### 요청 선처리 작업시 사용된 컴포넌트

- org.springframework.web.servlet.**LocaleResolver**
    - **지역화, 지역 정보를 결정해주는 전략 오브젝트**이다.
      - 지역화 기능은 화면에 보이는 언어를 설정하는 처리를 지원한다.
    - 디폴트인 AcceptHeaderLocalResolver는 HTTP 헤더의 정보(브라우저에 설정된 지역정보 등)를 보고 지역정보를 설정해준다.

- org.springframework.web.context.request.**RequestContextHolder**
    - **스레드 로컬 객체**
    - 요청을 받아서 응답할 때까지 일반 빈(스프링이 관리하는 객체)에서 **HttpServletRequest, HttpServletResponse, HttpSession 등**을 사용할 수 있도록 한다.
        - 해당 객체들을 일반 빈에서 사용하게 되면, Web 기술에 종속적이 될 수 있다는 문제점도 있다. 
        - 스프링에서 제공하는 다른 기능을 활용해 대체할 수 있으므로, 권장되는 방법은 아니다. 
  
- org.springframework.web.servlet.**FlashMapManager**
    - FlashMap 객체를 조회(retrieve, 복원) & 저장을 위한 인터페이스
        - **FlashMap 객체는 redirect로 값을 전달할 때, 딱 한 번 값을 유지할 수 있는 기능을 지원**하므로, redirect 시 값을 전달하기 위해 사용한다. 
        - 리다이렉트 후 조회를 하면 바로 정보는 삭제된다.
          - 리다이렉트시 url 파라미터를 활용할 수도 있지만, 길이 제한 등의 이유로 지양되며, FlashMap이 지원된다.
    - RedirectAttributes의 addFlashAttribute메소드를 이용해서 저장한다.

- org.springframework.web.multipart.**MultipartResolver**
    - **멀티파트 파일 업로드를 처리하는 전략**
        - 파일 업로드시 멀티파트 파일에 따라 특수한 request 객체가 필요하므로, MultipartResolver가 이를 결정한다.

### 요청 전달

![DispatcherServlet 내부 동작흐름 상세 - 요청 전달](https://blog.kakaocdn.net/dn/bnNq5n/btq9gzz47ch/AiynMkbQImWt1IV5a5jOmk/img.png)

#### 요청 전달시 사용된 컴포넌트

- org.springframework.web.servlet.**HandlerMapping**
    - HandlerMapping 구현체는 **어떤 핸들러가 요청을 처리할지에 대한 정보**를 알고 있다.
    - 디폴트로 설정되는 있는 핸들러매핑은 BeanNameHandlerMapping 과 DefaultAnnotationHandlerMapping 2가지가 설정되어 있다.
    - HandlerExecutionChain을 결정한다.

- org.springframework.web.servlet.**HandlerExecutionChain**
    - HandlerExecutionChain 구현체는 **실제로 호출된 핸들러에 대한 참조**를 가지고 있다.
    - **핸들러 실행 전, 후에 수행될 HandlerInterceptor도 참조**하고 있다.
    - HandlerAdapter 를 결정한다.
    - HandlerExecutionChain 객체가 없으면 http 404 (Not Found) 에러가 발생한다.

- org.springframework.web.servlet.**HandlerAdapter**
  - **실제 핸들러를 실행하는 역할**을 담당한다.
  - 핸들러 어댑터는 선택된 핸들러를 실행하는 방법과 응답을 ModelAndView로 변화하는 방법에 대해 알고 있다.
  - 디폴트로 설정되어 있는 핸들러어댑터는 HttpRequestHandlerAdapter, SimpleControllerHandlerAdapter, AnnotationMethodHanlderAdapter 3가지이다.
      - 예를 들어, @RequestMapping과 @Controller 어노테이션을 통해 정의되는 컨트롤러의 경우 **DefaultAnnotationHandlerMapping**에 의해 핸들러가 결정되고, 그에 대응되는 **AnnotationMethodHandlerAdapter**에 의해 호출이 일어난다.
  - HandlerAdapter 객체가 없다면, 서버 내에서 ServletException 에러가 발생한다.

### 요청 처리

![https://blog.kakaocdn.net/dn/seWWb/btq9e7dpQfU/NnxN7IJbwzxnpkfMxKq9gK/img.png](https://blog.kakaocdn.net/dn/seWWb/btq9e7dpQfU/NnxN7IJbwzxnpkfMxKq9gK/img.png)

- 각 요청의 비즈니스 로직 관련된 처리 전후로 인터셉터의 preHandle이나 postHandle이 필요한 경우 실행된다.

#### 요청 처리시 사용된 컴포넌트

- org.springframework.web.servlet.ModelAndView
    - ModelAndView는 Controller의 처리 결과를 보여줄 view와 view에서 사용할 값을 전달하는 클래스이다.
    - 핸들러가 실행된 후에 리턴하는 결과값에 해당한다.
        - Request 객체에 직접 값을 넣어서 전달하여, Web 기술에 종속되는 것을 방지하기 위해 제공되는 스프링 기술이다.
- org.springframework.web.servlet.RequestToViewNameTranslator
    - 핸들러 실행 후 리턴 된 ModelAndView 객체가 뷰를 갖고 있지 않을 때 동작한다.
    - 컨트롤러에서 뷰 이름이나 뷰 오브젝트를 제공해주지 않았을 경우 URL과 같은 요청정보를 참조해서 자동으로 뷰 이름을 생성해주는 전략 오브젝트이다.
    - 디폴트는 DefaultRequestToViewNameTranslator이다.

### 예외처리

![https://blog.kakaocdn.net/dn/cNqqeh/btq9e5GHCd9/S0ke9wdGXKkv8hZPCXDXOk/img.png](https://blog.kakaocdn.net/dn/cNqqeh/btq9e5GHCd9/S0ke9wdGXKkv8hZPCXDXOk/img.png)

#### 예외 처리시 사용된 컴포넌트

- org.springframework.web.servlet.**handlerexceptionresolver**
    - 기본적으로 DispatcherServlet이 DefaultHandlerExceptionResolver를 등록한다.
    - HandlerExceptionResolver는 예외가 던져졌을 때, 어떤 핸들러를 실행할 것인지에 대한 정보를 제공한다.
    - ModelAndView가 있다면 요청처리를 재개

### 뷰 렌더링 과정

![https://blog.kakaocdn.net/dn/xAPFX/btq9iAE0Ii1/YD10ivSIbvYmx3gREvXhv1/img.png](https://blog.kakaocdn.net/dn/xAPFX/btq9iAE0Ii1/YD10ivSIbvYmx3gREvXhv1/img.png)

#### 뷰 렌더링 과정시 사용된 컴포넌트

- org.springframework.web.servlet.ViewResolver
    - 컨트롤러가 리턴한 뷰 이름(String)을 참고해서 적절한 뷰 오브젝트를 찾아주는 로직을 가진 전략 오프젝트이다.
    - 뷰의 종류에 따라 적절한 뷰 리졸버를 추가로 설정해줄 수 있다.

### 요청 처리 종료

![https://blog.kakaocdn.net/dn/ICEZB/btq9gXUYOMq/TfixQ8uebBWMgFJvKkgiSK/img.png](https://blog.kakaocdn.net/dn/ICEZB/btq9gXUYOMq/TfixQ8uebBWMgFJvKkgiSK/img.png)

### 출처)
- [부스트코스 풀스택 강의](https://www.boostcourse.org/web316/lecture/254347/?isDesc=false)