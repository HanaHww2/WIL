# TestRestTemplate
- 

# RestAssured
- RestAssured is a completely different framework. This has nothing to do with Spring. 
- This is a library, which provides various ways to test any REST service with fluent BDD style interface.
- 기능, 역할 측면에서는 TestRestTemplate와 크게 다를 것이 없다.

# MockMvc
- 별도의 구성없이도 @WebMvcTest로 테스트를 수행할 수 있다. 
- 물론 @SpringBootTest에서도 환경을 Mock으로 구성하여 수행할 수 있다.

# WebTestClient
- WebClient 를 테스트하기 위해 활용된다.