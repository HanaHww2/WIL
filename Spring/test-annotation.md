# @SpringBootTest 
- for bootstrapping the full application to run an integration test.
- the use of webEnvironment=RANDOM_PORT to start the server with a random port (useful to avoid conflicts in test environments) and the injection of the port with @LocalServerPort. 
- Also, note that Spring Boot has automatically provided a `TestRestTemplate` for you. (webEnvironment NONE 설정시 사용 불가)
- 웹 테스트 환경 구성이 가능하다.
- webEnvironment 파라미터를 이용하여 손쉽게 웹 테스트 환경을 선택할 수 있다.

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
public class HttpRequestTest {

	@LocalServerPort // deprecated
	private int port;

	@Autowired
	private TestRestTemplate restTemplate;
```

## WebEnvironment
 
1. Mock
   - Mock 타입은 Servlet Container(톰캣, jetty 등등)를 테스트용으로 띄우지 않고, Mockup1을 해서 Servlet을 Mocking2한 것을 띄워준다. dispatcherServlet이 생성은 되지만 Mockup이 되기 때문에, dispatcherServlet에 요청을 보낸 것‘처럼’ 테스트를 할 수 있다. 이 때 mockup 된 Servlet과 상호작용을 하려면 MockMVC라는 클라이언트를 사용해야 한다.
   - 실제 객체를 만들기엔 비용과 시간이 많이 들거나 의존성이 길게 걸쳐져 있어 제대로 구현하기 어려울 경우 가짜 객체를 만들어 사용한다.
   - WebApplicationContext를 로드하며 내장된 서블릿 컨테이너가 아닌 Mock 서블릿을 제공한다.
   - 별도로 지정하지 않으면 기본값은 Mock 서블릿을 로드하여 구동하게 된다.
   - @AutoConfigureMockMvc 어노테이션을 함께 사용하면 별다른 설정 없이 간편하게 MockMvc를 사용한 테스트를 진행할 수 있다.
   - MockMvc는 브라우저에서 요청과 응답을 의미하는 객체로서 Controller 테스테 사용을 용이하게 해주는 라이브러리이다.

1. RANDOM_PORT
   - EmbeddedWebApplicationContext를 로드하며 실제 서블릿 환경을 구성 한다.
   - 임의의 port listen
   - useful to avoid conflicts in test environments
2. DEFINED_PORT
   - RAMDOM_PORT와 동일하게 실제 서블릿 환경을 구성하지만, 포트는 애플리케이션 프로퍼티에서 지정한 포트를 listen 한다.
3. NONE
   - 기본적인 ApplicationContext를 로드한다.

# @WebMvcTest

- presentation, web 레이어 관련 빈들만 로드(등록)하여 테스트를 수행한다.
- What you want is a sliced test for the web, so instead of @SpringBootTest use @WebMvcTest this will make your test considerably faster.
- @AutoConfigureMockMvc as that is added by default and More
    ```java
    @Target(ElementType.TYPE)
    @Retention(RetentionPolicy.RUNTIME)
    @Documented
    @Inherited
    @BootstrapWith(WebMvcTestContextBootstrapper.class)
    @ExtendWith(SpringExtension.class)
    @OverrideAutoConfiguration(enabled = false)
    @TypeExcludeFilters(WebMvcTypeExcludeFilter.class)
    @AutoConfigureCache
    @AutoConfigureWebMvc
    @AutoConfigureMockMvc
    @ImportAutoConfiguration
    public @interface WebMvcTest {

    ```
## @WebMvcTest vs. @SpringBootTest with @AutoConfigureMockMvc and @MockBean (when you testing)
```java
@SpringBootTest
@AutoConfigureMockMvc
public class TestingWebApplicationTest {

	@Autowired
	private MockMvc mockMvc;
   @MockBean
	private GreetingService service;
```
- 목으로 지정된 객체 외 모든 컨텍스트가 로드될 것
- 특별한 이유(외부 api 사용 등)가 있는 것이 아니고서야 모킹테스트를 수행하는데, 굳이 @SpringBootTest를 쓸 이유가 없을 것 같다.

```java
@WebMvcTest // 특정 클래스 지정 가능(GreetingController.class)
public class WebLayerTest {

	@Autowired
	private MockMvc mockMvc;
   @MockBean
	private GreetingService service;

```
- 목으로 지정된 객체 외 모든 웹 레이어 컨텍스트가 로드될 것
  
# Sliced Test

#### 참고자료
- https://spring.io/guides/gs/testing-web/
- https://stackoverflow.com/questions/72874685/mockmvc-with-springboottest-is-throwing-exception-httpmediatypenotsupportedexcep
- https://yadon079.github.io/2021/spring%20boot/boot-test
- https://goddaehee.tistory.com/211?category=367461