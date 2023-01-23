# 스프링에서 예외(에러) 제어하기

스프링에서는 다양한 에러 제어 방식을 제공한다.  
그 중 몇 가지만 간단히 알아보자.
### Controller-Level @ExceptionHandler
```
public class FooController{
    
    //...
    @ExceptionHandler({ CustomException1.class, CustomException2.class })
    public void handleException() {
        //
    }
```

### @ControllerAdvice @RestControllerAdvice
> Spring 3.2 brings support for a global @ExceptionHandler with the @ControllerAdvice annotation.

```java
@ControllerAdvice
public class RestResponseEntityExceptionHandler 
  extends ResponseEntityExceptionHandler {

    @ExceptionHandler(value 
      = { IllegalArgumentException.class, IllegalStateException.class })
    protected ResponseEntity<Object> handleConflict(
      RuntimeException ex, WebRequest request) {
        String bodyOfResponse = "This should be application specific";
        return handleExceptionInternal(ex, bodyOfResponse, 
          new HttpHeaders(), HttpStatus.CONFLICT, request);
    }


    // 참고 ResponseEntityExceptionHandler 내부의 handleExceptionInternal 메소드
	protected ResponseEntity<Object> handleExceptionInternal(
			Exception ex, @Nullable Object body, HttpHeaders headers, HttpStatus status, WebRequest request) {

		if (HttpStatus.INTERNAL_SERVER_ERROR.equals(status)) {
			request.setAttribute(WebUtils.ERROR_EXCEPTION_ATTRIBUTE, ex, WebRequest.SCOPE_REQUEST);
		}
		return new ResponseEntity<>(body, headers, status);
	}

}
```
### ResponseStatusException (Spring 5 and Above)
- ResponseEntity의 친구 느낌이랄까...
- 에러 응답을 위한 객체를 스프링 5 이상에서 제공한다.
- 글로벌한 예외 핸들러를 만드는 것에 비해 간단한 편이다. 하지만 관리의 어려움이 있을 수 있다.
- ResponseStatusExceptionResolver 에서 해당 예외를 처리한다.

```java
@GetMapping(value = "/{id}")
public Foo findById(@PathVariable("id") Long id, HttpServletResponse response) {
    try {
        Foo resourceById = RestPreconditions.checkFound(service.findOne(id));

        eventPublisher.publishEvent(new SingleResourceRetrievedEvent(this, response));
        return resourceById;
     }
    catch (MyResourceNotFoundException exc) {
         throw new ResponseStatusException(
           HttpStatus.NOT_FOUND, "Foo Not Found", exc);
    }
```

### 활용 결과
- 자료들을 참고하며 통합된 예외 핸들링 코드를 작성했다.
- 결과적으로 ResponseStatusException 과 유사한 형태의 커스텀 Exception을 하나 만들었다. 처리 동작은 조금 다르지만 말이다. 
  - 즉, 커스텀 예외가 HttpStatus 코드를 멤버로 갖도록 구성했다.
- 그리고 ResponseEntityExceptionHandler를 상속한 핸들러에서 해당 예외를 처리할 수 있게 간단히 구현했다.
- 참고했던 자료들처럼 커스텀 예외를 상속한 추가 예외들을 만들지, 커스텀 예외 하나로 통합해서 예외를 제어할지 고민이 된다. 

```java
@Getter
public class CustomApiException extends RuntimeException{
    private HttpStatus status;

    // 응답처리에 활용할 상태값을 미리 지정해둔다.
    public CustomApiException(String message, HttpStatus status) {
        super(message);
        this.status= status;
    }
    public CustomApiException(String message) {
        super(message);
    }

    public CustomApiException() {
        super();
    }
    public CustomApiException(String message, Throwable cause) {
        super(message, cause);
    }
    public CustomApiException(Throwable cause) { super(cause); }
}

@RestControllerAdvice
public class GlobalExceptionHandler extends ResponseEntityExceptionHandler {

    // 공통 커스텀 예외를 기준으로 오류를 제어한다.
    
    @ExceptionHandler(CustomApiException.class)
    protected ResponseEntity<?> handleCustomApiException(CustomApiException e, WebRequest request) {

        HttpHeaders headers = new HttpHeaders();
        return handleExceptionInternal(e, new CommonResult<>(e.getMessage(), null), headers, e.getStatus(), request);
    }

    // 나머지 예외 처리는 오버라이드해서 커스텀할 수 있다.
}
```

## 예외처리 내부 로직


#### 참고자료
- https://blog.naver.com/PostView.naver?blogId=writer0713&logNo=221605253778&parentCategoryNo=&categoryNo=83&viewDate=&isShowPopularPosts=true&from=search
- https://www.baeldung.com/exception-handling-for-rest-with-spring
- https://mangkyu.tistory.com/204
  - 다시보기!
- https://mangkyu.tistory.com/205