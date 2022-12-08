### 스프링 시큐리티를 활용하면서 확인한 오류 혹은 이슈들을 기록합니다.

### allowCredentials with wildcard
<img width="689" alt="image" src="https://user-images.githubusercontent.com/62924471/206460631-4a959597-69d1-4f0c-a07f-b2a047826899.png">

- When allowCredentials is true, allowedOrigins cannot contain the special value "*" since that cannot be set on the "Access-Control-Allow-Origin" response header.

  - 명쾌한 에러 메시지
  - 테스트 프로파일이라 간단히 "*" 와일드카드로 지정해두었습니다만, 크레덴셜 옵션 설정으로 인해 오류가 발생
  - 해결을 위 'http://localhost:3000' 와 같이 허용 주소를 지정

    <img width="342" alt="image" src="https://user-images.githubusercontent.com/62924471/206464131-0a7e7004-8334-4120-8e0d-94bb77884a79.png">

### csrf (one of default setting)

<img width="710" alt="image" src="https://user-images.githubusercontent.com/62924471/206464694-d6184375-3f47-434d-8113-982edf005b31.png">

- Invalid CSRF token found for http://localhost/api/v1/categories/3
  - 명백한 로그 메세지
  - csrf 토큰은 프로젝트에서 활용하지 않을 예정이므로 일단 SecurityConfig 파일에 이에 대한 설정을 작성하는 것으로 해결
  - csrf 토큰을 활용하는 경우라면 아래와 같이 테스트 코드 작성 가능
  
    ```java
    
      mockMvc.perform(delete("/api/v1/categories/3").with(csrf()))
                  .andExpect(status().isOk())
                  .andExpect(content().contentTypeCompatibleWith(MediaType.APPLICATION_JSON))
                  .andDo(print());
    ```
