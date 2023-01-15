# @WithSecurityContext 활용
- 스프링 시큐리티를 활용하는 서비스를 테스트할 때, 간단하게는 @WithMockUser를 활용한다.
- 그러나 해당 애노테이션은 기본 Principal 객체를 반환하므로, 사용자가 커스텀한 Principal 객체(a custom Authentication principal)를 활용하는 경우에는 적합하지 못하다.
- 이를 보완하기 위해서 @WithSecurityContext 애노테이션을 활용하는 코드를 작성할 수 있다.

```java
// 이하 WithMockCustomUser.java
@Retention(RetentionPolicy.RUNTIME)
@WithSecurityContext(factory = WithMockCustomUserSecurityContextFactory.class)
public @interface WithMockCustomUser {
    long id() default 1l;
    String email() default "test@example.com";
    String name() default "test user";
}

// 이하 WithMockCustomUserSecurityContextFactory.java
public class WithMockCustomUserSecurityContextFactory implements WithSecurityContextFactory<WithMockCustomUser> {

    @Override
    public SecurityContext createSecurityContext(WithMockCustomUser customUserPrincipal) {
        SecurityContext context = SecurityContextHolder.createEmptyContext();

        UserPrincipal principal = UserPrincipal.builder()
                .id(customUserPrincipal.id())
                .email(customUserPrincipal.email())
                .build();

        var authorities = Collections.
                singletonList(new SimpleGrantedAuthority(RoleType.USER.getCode()));

        Authentication auth =
                UsernamePasswordAuthenticationToken.authenticated(principal, "password", authorities);
        context.setAuthentication(auth);
        return context;
    }
}
```
- @WithSecurityContext() 어노테이션을 적용할 WithMockCustomUser 어노테이션 인터페이스 생성한다.
- @WithSecurityContext() 에서 활용할 SecurityContextFactory 를 지정해준다.
  - 이 때, WithSecurityContextFactory 인터페이스를 구현해 제공한다.
    - 커스텀 한 새로운 SecurityContext 를 반환하는 팩토리 구현체가 된다.
    - 이 컨텍스트에는 우리가 사용하고자 하는 커스텀한 Principal 의 정보가 담길 것이다.

### 다른 방식(하드 코딩)
```java
UserPrincipal userPrincipal = UserPrincipal.builder()
        .id(1L)
        .build();
var authorities = Collections.
        singletonList(new SimpleGrantedAuthority(RoleType.USER.getCode()));
SecurityContextHolder.getContext()
        .setAuthentication(new UsernamePasswordAuthenticationToken(userPrincipal, "", authorities));
```
- @BeforeEach 를 활용해, 시큐리티 컨텍스트에 커스텀한 Principal 객체를 저장해두고 테스트에 활용하는 방식
- @WithSecurityContext 를 활용한 커스텀한 애노테이션을 생성해두면 해당 애노테이션을 활용하는 것으로 대체 가능

### 참고 자료
- 공식 문서 : https://docs.spring.io/spring-security/reference/servlet/test/method.html#test-method-withsecuritycontext
- https://gaemi606.tistory.com/entry/Spring-Boot-Spring-Security-Test-WithMockUser%EB%A5%BC-%EC%BB%A4%EC%8A%A4%ED%84%B0%EB%A7%88%EC%9D%B4%EC%A7%95-%ED%95%B4%EC%84%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EC%9E%90
- https://yoon0120.tistory.com/51
