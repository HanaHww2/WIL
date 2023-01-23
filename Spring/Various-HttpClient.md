# RestTemplate
- deprecated
> 2021년 팀플젝을 수행했던 시기의 일이다. 당시 공공 api를 호출하는 작업을 수행하기 위해 HttpClient를 활용해야 했다. 인터넷을 서치하면서 RestTemplate을 알게 되었다. 그런데, 이 기능이 deprecated 된다는 것을 확인하고 나는 reactive에 대해서 거의 알지 못한 상태로 WebClient를 사용하기로 결정했다.ㅎㅎ;   
(이 때는 당장 이 클래스/API가 더는 서비스되지 않을 수 있다고 생각했다. 프로젝트를 수행할 때, 라이브러리가 잘 유지 및 관리가 되는지 확인하는 것도 중요하다는 이야기를 여러번 확인했었고, 특히 개인 오픈소스 중에 그렇게 관리가 소홀해지다가, 어느 순간 더 이상 업데이트를 더는 수행하지 않아서 프레임워크 등과 호환되지 않는다거나 기타 사유로 사용하지 못하게 되는 경우가 있다는 것을 글과 책으로 배운 상태였기 때문이다.   
그러나 사실 RestTemplate은 스프링 프로젝트에서 지원하는 라이브러리에 속하고, 앞으로 업데이트가 중단이 될 지언정 당장의 사용엔 큰 무리가 없다고 지금은 알고 있다.  
물론 스프링 버전이 올라가면서 결국 더 이상 지원하지 않게 될 것이다. 이 때, 자신의 프로젝트가 사용하는 스프링 버전도 이에 맞춰 업데이트를 수행한다면 그 때를 미리미리 대비할 수는 있을 것이다.   
Servlet 스택에서는 WebClient를 블록 방식(.block())으로 호출할 수 있다. 과거 나는 Reactive 스택이 Servlet과 WAS(사실 WAS 에 대해서도 거의 무지했다.)부터 다르게 구성되는 것을 몰랐고, block() 방식을 지양하라는 글을 보고 내가 쓴 방법이 잘못된 방식인 줄 알았다. )


# FeignClient
- RestTemplate과 마찬가지로 Blocking 방식
- reactive 스택(nio 서버)을 갖춘 것이 아니라면, RestTemplate의 다른 대안이 될 수 있다.

# WebClient
- 논블록킹/비동기

#### 참고자료
- https://stackoverflow.com/questions/67191617/springboot-feignclient-vs-webclient
- https://stackoverflow.com/questions/58513071/spring-mvc-to-spring-webflux-migration-block-vs-subscribe
- https://www.inflearn.com/questions/482908 (백기선님 질답)
- https://stackoverflow.com/questions/67191617/springboot-feignclient-vs-webclient
    > To be able to answer “when” one needs to understand the capabilities of each.  
    > 
    > Spring WebClient is a non-blocking reactive client to make HTTP requests. Hence if you intend to use Spring Reactive Stream API to stream data asynchronously then this is the way to go. Think event-driven architecture. WebClient is part of the Spring WebFlux library.  
    > 
    > [Feign]3 is a declarative REST library that uses annotations based architecture with thread-per-request model. This means that the thread will block until the feign client receives the response. The problem with the blocking code is it must wait until the consuming thread completes, hence think memory and CPU cycles.
    > 
    > So use Spring WebClient when needing non-blocking HTTP requests otherwise Feign due to simple usage model.
    > 
    > (Note: There is no reason as to why one cannot use WebClient for blocking operations but Feign is more mature and it’s annotation based model makes it easier)