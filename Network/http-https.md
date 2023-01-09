# HTTP(HyperText Transfer Protocol)

<img width=500 src="https://user-images.githubusercontent.com/62924471/211206622-1bc0f20f-230a-4502-abce-377de4c67678.png">

- **하이퍼 텍스트 전송 프로토콜(HTTP)** 은 HTML과 같은 **하이퍼 미디어 문서를 전송하기 위한 애플리케이션 레이어 프로토콜**이다.
- HTTP는 웹사이트를 방문하면 서버와의 통신에서 이용한다. 
  - 웹 브라우저와 웹 서버 간의 커뮤니케이션을 위해 디자인 되었지만, 다른 목적으로도 사용될 수 있다.
- HTTP는 클라이언트가 요청을 생성하기 위한 연결을 연 다음, 응답을 받을 때 까지 대기하는 **전통적인 클라이언트-서버 모델**을 따른다. 

- HTTP는 **무상태 프로토콜**이며, 이는 서버가 두 요청 간에 어떠한 데이터(상태)도 유지하지 않음을 의미한다. 
- 일반적으로 안정적인 전송 레이어(transport layer, 통신 계층 중 하나)로 UDP와 달리 `메세지를 잃지 않는 프로토콜인 TCP/IP 레이어`를 기반으로 사용한다.

### HTTP 통신을 통해 데이터 전송

거의 모든 형태의 데이터 전송이 가능하다. 서버 간에 데이터를 주고 받을 때도 대부분 HTTP 사용한다.
- HTML, TEXT, IMAGE, 음성, 영상, 파일, JSON, XML (API) 등

## HTTP 기반 시스템의 구성요소

- 요청은 하나의 개체, 사용자 에이전트(또는 그것을 대신하는 프록시)에 의해 전송됩니다. 
-   대부분의 경우, 사용자 에이전트는 브라우저지만, 무엇이든 될 수 있습니다. 예를 들어, 검색 엔진 인덱스를 채워넣고 유지하기 위해 웹을 돌아다니는 로봇이 그러한 경우다.
- 각각의 개별적인 요청들은 서버로 보내지며, 서버는 요청을 처리하고 *response* 라고 불리는 응답을 제공합니다. 
-   이 **요청과 응답 사이에는 여러 개체들**이 있는데, 예를 들면 **다양한 작업을 수행하는 게이트웨이 또는 [캐시](https://developer.mozilla.org/ko/docs/Glossary/Cache) 역할을 하는 프록시 등**이 있습니다.

![https://mdn.mozillademos.org/files/13679/Client-server-chain.png](https://mdn.mozillademos.org/files/13679/Client-server-chain.png)

- 브라우저와 요청을 처리하는 서버 사이에는 좀 더 많은 컴퓨터들이 존재합니다. 
  - 라우터, 모뎀 등 
  - 웹의 계층적인 설계 덕분에, 이들은 네트워크와 전송 계층 내로 숨겨지게 됩니다. 
- HTTP은 애플리케이션 계층의 최상 위에 있으며, 기본(하위) 레이어들은 HTTP의 명세와는 거의 관련이 없습니다.

## 무상태 프로토콜

### 스테이스리스(Stateless) ↔ Stateful

- 서버가 클라이언트의 상태를 보존하지 않는다.
- **장점: 서버 확장성 높다.** (스케일 아웃)
    - 갑자기 클라이언트 요청이 증가해도 (상태를 기억하지 않아도 되니까) 서버를 대거 투입할 수 있다. (스케일아웃, 수평확장에 유리)
    - 무상태는 응답 서버를 쉽게 바꿀 수 있다. -> 무한한 서버 증설 가능
    - 최대한 스테이리스한 설계를 해야지만 이런 대용량 트래픽 이벤트가 생겼을 때 스케일아웃(서버 확 늘려서)으로 대응 가능하다.
- **단점: 클라이언트가 반복적으로 상태 정보를 전송**해야 한다.

### Stateless에서의 상태 유지

- 일반적으로 **브라우저 쿠키와 서버 세션 등을 사용**해서 상태 유지합니다.
    - 클라이언트에서 데이터를 많이 보내야 한다는 니단점이 있습니다. (상태를 보관할 수 없으니 감안하여 모두 보내는 꼴이다.)
    - 상태 유지는 최소한만 사용합니다.

## 비연결성(connectionless)

- HTTP는 기본이 연결을 유지하지 않는 모델이다. 
  - 일반적으로 초 단위의 이하의 **빠른 속도로 응답이 가능**합니다. 
  - 즉, 서버 자원을 매우 효율적으로 사용할 수 있습니다.

### 한계와 극복

- 매번 TCP/IP 연결을 새로 맺어야 하므로 - **3 way handshake 시간**이 추가적으로 소요된다.
- 웹 브라우저로 사이트를 요청하면, HTML 뿐만 아니라 자바스크립트, css, 추가 이미지 등등 **수많은 자원이 함께 다운로드** 되므로 자원이 소모된다.
  - 지금은 **HTTP 지속 연결(Persistent Connections)**로 문제 해결!!
  - **HTTP/2, HTTP/3**에서 더 많은 최적화

## HTTP 메시지

<img width=600 src="https://blog.kakaocdn.net/dn/qCkwg/btral7n0Ado/vLrCR0IPKNNILsC1sqYsR0/img.png">

### 시작 라인(start-line) - 빨간 박스

- 시작 라인은 요청 시에는 `request-line` , 응답 시에는 `status-line` 으로 구성된다.

**요청 메시지**

ex) `GET /search?q=hello&hl=ko HTTP/1.1`

- 메서드 : GET
- 요청대상(path) : /search?q=hello&hl=ko, 보통 절대 경로로 구성
- HTTP 버전 : HTTP/1.1

**응답 메시지** : 응답 결과 코드를 포함한다.

### HTTP Header - 노란 박스

- HTTP 전송에 필요한 모든 부가 정보를 말합니다. (메타 정보 덩어리)
  - 예) 메시지 바디의 내용, 메시지 바디의 크기, 압축 여부, 인증, 요청 클라이언트(브라우저) 정보, 서버 애플리케이션 정보, 캐시 관리 정보 등을 담을 수 있다.
- 표준으로 이용되는 헤더가 굉장히 많으며, 필요 시 임의의 헤더 추가가 가능합니다.

### HTTP Message Body - 파란 박스
- 바이트로 표현할 수 있는 모든 정보가 전송 가능하며, 압축하여 이용할 수도 있다.


---
# HTTP version

### HTTP 역사

1. 1990년 말 세계 첫 웹페이지가 등장하고 이듬해인 1991년 **HTTP/0.9**가 등장했습니다.   
당시에는 단순히 서버에서 특정 문서를 다운로드하는 간단한 것이었습니다.  
이 때는 GET 메서드만 지원하고 HTTP 헤더가 없었습니다.  
2. 1996년에 이르러 업로드에 대응하는 등의 메서드, 헤더를 추가해 기능을 확대, 업데이트한 **HTTP/1.0** 프로토콜이 책정됩니다.   
이는 **오늘날 HTTP 통신의 원형**이라고 할 수 있습니다.   
HTTP/1.0에선 모든 요청에서 새로운 TCP 연결을 만드는 형태로 되어 있기 때문에 **핸드셰이크(handshake)로 인한 지연이 문제**가 됩니다.  
3. 이 문제를 해결하기 위해 HTTP/1.0이 나오고 반년 뒤에 이를 수정한 **HTTP/1.1**이 정립됩니다.   
HTTP/1.1에는 **킵어라이브(keepalive)를 도입**해 **여러 요청을 하나의 연결로 처리**할 수 있게 되었습니다.  
HTTP/1.1은 오랫동안 웹 통신을 지원해오고 있으며, 2015년 다음 버전인 HTTP/2가 공식 사양이 되었음에도, HTTP/2 수립 이후에도 HTTP/1.1 통신을 하는 사이트가 많습니다.  

---
# HTTP 1.1

## HTTP 1.1의 개선 사항
### **1. Persistent Connection**
#### 참고 : 3 way handshake
<img width=600 src="https://blog.kakaocdn.net/dn/ctv08f/btq5tpIHpIx/RsYUVbL5oe8VEjm3CEjIA1/img.png">
<img width=600 src="https://blog.kakaocdn.net/dn/bfHrRM/btq5tEr0fkD/VGbFEVID66U0HJhYg1lemk/img.png">

- HTTP 통신을 통해 여러 오브젝트를 요청 및 응답해야 하는 경우, **HTTP 1.0 초기**에는 **요청 때마다 TCP연결을 3-Way handshake 방식으로 맺어야** 하는 단점이 존재했습니다.
- 웹의 초창기 때는 콘텐츠의 수가 많지 않았기 때문에 부담이 크지 않았지만 웹 사이트의 콘텐츠가 늘어나면서, **TCP 연결의 재사용**이 필요성이 점차 증가하였습니다. 
  - 이때 나온 기술이 바로 **Persistent Connection** 기술입니다. (**keep-alive**라고도 한다.)
- Persistent Connection의 사용을 원하고 이를 지원하는 클라이언트는 서버에 HTTP 메세지를 전달할 때 아래와 같은 **헤더를 추가**하게 됩니다.
- 이를 지원하는 서버는 클라이언트의 요청을 받고 TCP 연결을 HTTP 응답 이후에 끊지 않고 계속 사용하겠다는 약속으로 동일한 헤더를 HTTP 응답response에 포함하여 보냅니다.
> **Connection : keep-alive**

- **HTTP 1.1**에서는 굳이 Connection **헤더를 지정하지 않아도, 모든 요청과 응답은 기본적으로 Persistent Connection을 지원**하고 있습니다.
  - 그래서 **연결 지속이 필요 없을 경우에만** 아래와 같은 Connection 헤더를 사용하게 됩니다.
> **Connection : close**

- **Persistent Connection을 사용하지 말아야 할 경우** 
  - 서버에 연결된 클라이언트의 TCP연결이 계속해서 늘어나면 서버의 자원이 고갈되어 다른 클라이언트들의 접속에 대처할 수 없는 상황이 발생할 수 있습니다.
  - 클라이언트의 접속이 제일 잦은 메인 페이지와 같은 URL에서는 **서버의 가용성을 고려**해 Persistent Connection을 사용할지 말지를 고민해야 합니다.

- **장점**은 서버의 단일 시간내 TCP 연결의 수를 적게 해서 자원을 절약할 수 있고 네트워크 혼잡이나, 지연의 경우의 수를 줄일 수 있다. 또한 속도가 빨라진다.

### **2. Pipelining**
![https://blog.kakaocdn.net/dn/vWH3t/btq5u44Cyij/OfwqHIcZi0ZJN43g9VLQIK/img.png](https://blog.kakaocdn.net/dn/vWH3t/btq5u44Cyij/OfwqHIcZi0ZJN43g9VLQIK/img.png)

- HTTP Request 들은 **연속적**으로 발생하며, **순차적**으로 동작합니다.
- 즉, HTTP/1.1은 한 번의 연결에 여러 리소스를 다운로드 할 수 있는 특징이 있습니다.
  - 그러나 여러 리소스를 **병렬적**으로 가져오려면 **여러 HTTP/1.1 연결**을 만들고, **매번 핸드셰이크를 수행**해야 하므로, 이전의 HTTP/1.0 와 다를 바가 없게 되어 버린다.
- 파이프라이닝은 HTTP1.1에서 클라이언트와 서버 간 요청과 응답의 효율성을 개선하기 위해 만들어진 개념이다. 
  - HTTP/1.1 에서 클라이언트는 각 요청에 대한 **응답을 기다리지 않고, 여러개의 HTTP Request 를 하나의 TCP/IP Packet 으로 연속적으로 Packing 해서 요청**을 보낸다.
  - **파이프라이닝**이 적용되면, 하나의 Connection으로 다수의 Request 와 Response 를 처리할 수 있게끔하여 **Network Latency를 줄일 수** 있습니다.
- 그러나 이 기법은 실제로 구현에 어려움이 있습니다.

## **HTTP/1.1의 문제점**

### **1. HOL ( Head Of Line ) Blocking - 특정 응답의 지연**
- 예를 들어 Pipelining기능을 통해 (a.png, b.png, c.png)를 받으려고 하는 경우 HTTP의 요청 순서는 아래와 같습니다.
  - 순서대로 첫번째 이미지의 요청을 응답하고 두번째의 요청에 대해 응답을 하게 됩니다. 
<img width=400 src='https://blog.kakaocdn.net/dn/bm6Nea/btq5yBtPppL/0g8ReMI314lbSz7Va3zz1K/img.png'>

- 그러나 만약 a.png에 대한 요청이 지연된다면, 아래와 같이 b.png, c.png의 요청은 a.png에 대한 응답이 완료될 때까지 계속 대기해야 합니다.
<img width=600 src='https://blog.kakaocdn.net/dn/DoOeN/btq5tpaOE5X/RiH1f5I8N5vPKUBM4Gb8BK/img.png'>

### **2. RTT (Round Trip Time) 증가**

> RTT는 통신에서 왕복 지연 또는 왕복 시간은 신호가 전송되는데 걸리는 시간과 해당 신호가 수신되었음을 확인하는 데 걸리는 시간을 더한 것을 얘기합니다.

- TCP 상에서 동작하는 HTTP의 특성 상 3-way Handshake가 반복적으로 일어나야 하며, 이는 불필요한 RTT 증가와 네트워크 지연을 초래하여 성능을 지연시키게 됩니다.

### **3. 무거운 Header 구조**

- HTTP/1.1의 `헤더`에는 `많은 메타 정보들`이 저장되어 있습니다. 
  - 요청이 여러 번 발생하는 경우, 클라이언트가 서버로 보내는 매 HTTP 요청 때마다 중복된 헤더 값을 전송하게 된다. 
  - 서버 도메인에 관련된 쿠키 정보도 헤더에 함께 포함되어 전송된다. 
- 이러한 **반복적인 헤더 전송, 쿠키 정보로 인한 헤더 크기 증가로 오버헤드가 발생**한다.

## HTTP/1.1 프로토콜 내 **개선 시도**

### **1. Image Spriting**

- 웹 페이지를 구성하는 다양한 아이콘 이미지 파일의 요청 횟수를 줄이기 위해, 아이콘을 **하나의 큰 이미지**로 만든 다음 CSS에서 해당 이미지의 좌표 값을 지정하여 표시한다.

![https://blog.kakaocdn.net/dn/LvpXl/btq5ugLdDwx/wvU8NrA2l1sbTBZNUodvk0/img.png](https://blog.kakaocdn.net/dn/LvpXl/btq5ugLdDwx/wvU8NrA2l1sbTBZNUodvk0/img.png)

### **2. Domain Sharding**
- 브라우저들은 HTTP/1.1의 단점을 극복하기 위해 **여러 개의 Connection을 생성해서 병렬로 요청**을 보내기도 한다. 
- 하지만 브라우저 별로 도메인 당 Connection 개수 제한이 존재하기 때문에 근본적인 해결책은 아니다. 
- 또한 여러 HTTP/1.1 연결을 실시하는 건 각각의 연결에서 매번 핸드셰이크를 수행하므로 원래 HTTP/1.0 상태가 되는 격이다.

### **3.Load Faster**
- async / defer 키워드를 이용해서 문서를 로드하는 방식을 html 태그 내에 지정할 수 있다. 
  - 이 방법은 브라우저에서 문서를 어떻게 빨리 로드하는가에 대한 정보다. 
- 참고 : [async VS defer](https://dkwjdi.tistory.com/188)

---
# **HTTP/2.0**
<img width=600 src='https://techrecipe.co.kr/wp-content/uploads/2019/09/190930_http_003.png'>

- HTTP/2는 기본적으로 HTTP/1.1 프로토콜을 바탕으로 이용되며, 단지 프로토콜의 성능에 초점을 맞추어 수정한 버전이다.

### **Multiplexed Streams**
- HTTP/2는 Multiplexed Streams를 이용해 Connection 한 개로 동시에 여러 개의 메시지를 주고 받을 수 있으며 응답은 순서에 상관없이 Stream으로 주고 받는다. 
- HTTP/1.1의 **Persistent Connection, PipeLining의 개선 버전**이라 할 수 있다.

### **Header Compression**
- HTTP/2는 헤더 정보를 압축해서 전송할 수 있도록 한다. 
- Header Table과 Huffman Encoding기법을 사용해 처리하는데 이를 **HPACK 압축 방식**이라 부르며, 별도의 명세서로 관리하고 있다.

### **Stream Prioritization(우선 순위)**
- HTTP/2에서는 **리소스 간의 의존 관계에 따라 우선순위를 설정**할 수 있다. 
  - 이를 이용해 리소스 로드시 발생하는 의존 관계 문제를 해결한다.

### **Server Push**
- 서버는 **클라이언트가 요청하지 않은 리소스(그러나 차후에 사용하게 될 리소스)를 사전에 push를 통해 전송**할 수 있다. 
  - 이를 통해 해당 문서 내의 리소스를 사전에 클라이언트에서 요청을 전송하지 않고도, 다운로드 할 수 있도록 하여 **클라이언트의 요청 발생을 최소화**할 수 있다.

# HTTP/3

- 2015년 HTTP/2가 등장하면서 하나의 연결에서 여러 자원을 동시에 다운로드할 수 있게 되었습니다. 
  - HTTP/2 등장으로 하나의 TCP 연결을 효율적으로 이용하는 게 가능하게 된 것이다. 하지만 이번에는 이 통신이 TCP에서 이뤄지고 있는 게 문제가 됐다. 
- 그러나 TCP는 데이터 전체를 올바른 순서로 전송하기 위한 프로토콜이며 TCP 패킷 일부가 네트워크에서 끊어질 때 그 패킷이 재전송될 때까지 후속 패킷을 차단해버린다. 
- 다른 리소스에 대한 요청을 하나의 TCP 연결로 정리하는 사정상 뭔가 리소스에 대한 요청 패킷 손실이 발생하면, 동일한 TCP 연결을 이용하는 다른 리소스에 대한 요청까지 모조리 중단되어 버린다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/190b44f8-14b5-4c2d-8751-64eccae4a48e/Untitled.png)

- 위와 같은 이유로 HTTP/3에선 새롭게 **QUIC**이라는 프로토콜이 개발되었으며, 이 프로토콜이 TCP 대신 이용된다. 
  - 이론상 QUIC는 TCP와 UDP에 함께 전송 프로토콜로 만들어도 좋지만, 새로운 전송 프로토콜을 보급하려면 현재 네트워크 장비를 모두 바꿔야 할 만큼 노력과 시간이 필요하다. 
  - 이 문제로 QUIC는 **UDP**를 이용해 구현되어 있다.
- QUIC는 여러 요청을 차단하지 않고 흘릴 뿐(❗이해 안되는 부분) 아니라 통신을 시작할 때의 핸드셰이크도 단축되고 있다. 
- 이전 버전까지는 TCP나 TLS 핸드셰이크를 따로 실시했지만, QUIC을 이용하면 **연결 인증과 암호화를 함께 해 서버와의 통신 횟수를 줄일 수 있다**.

![https://techrecipe.co.kr/wp-content/uploads/2019/09/190930_http_004.png](https://techrecipe.co.kr/wp-content/uploads/2019/09/190930_http_004.png)

---
# HTTPS
![https://techrecipe.co.kr/wp-content/uploads/2019/09/190930_http_002.png](https://techrecipe.co.kr/wp-content/uploads/2019/09/190930_http_002.png)
- **HTTPS** (*HTTP Secure*) 는 [HTTP](https://developer.mozilla.org/ko/docs/Glossary/HTTP) protocol의 암호화된 버전이다. 이것은 대개 클라이언트와 서버 간의 모든 커뮤니케이션을 암호화 하기 위하여 [SSL](https://developer.mozilla.org/ko/docs/Glossary/SSL) 이나 [TLS](https://developer.mozilla.org/ko/docs/Glossary/TLS)을 사용한다. 이 커넥션은 클라이언트가 민감한 정보를 서버와 안전하게 주고받도록 해준다. 예를들면 금융 활동 이나 온라인 쇼핑이 있을 수 있다.

## 전송 계층 보안 (TLS)

- [Secure Sockets Layer (SSL)](https://developer.mozilla.org/ko/docs/Glossary/SSL)로 알려진 **Transport Layer Security (TLS)**는 어플리케이션들이 네트워크 상에서 안전하게 통신하기 위해 사용된 [protocol](https://developer.mozilla.org/ko/docs/Glossary/Protocol)입니다.
- 이메일, 웹 브라우징, 메세징, 그리고 다른 프로토콜들의 감청을 통한 정보의 변형을 방지한다. SSL과 TLS 모두 네트워크 상에서 보안을 제공하는 cryptographic 프로토콜을 사용한 클라이언트 / 서버 프로토콜이다. 서버와 클라이언트가 TLS로 통신을 할때, 어떠한 제 3자도 메세지를 변형시키거나 감청할 수 없도록 한다.
- 모든 모던 브라우저들을 TLS를 지원하고, 안전한 연결을 하기위해서 서버가 유효한 [digital certificate (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Digital_certificate) 를 제공하기를 요구한다. 
  - 클라이언트와 서버 둘 다 각자 digital certificate을 제공하면, 서로를 인증해줄 수 있다.

## Secure Sockets Layer (SSL)

- Secure Sockets Layer(SSL)는 클라이언트와 서버 간의 안전한 링크를 통해 송수신되는 모든 데이터를 안전하게 보장하는 과거의 보안 표준 기술이었다. SSL 버전 3.0은 Netscape가 1999년에 발표했으며 현재에는 [Transport Layer Security (TLS)](https://developer.mozilla.org/ko/docs/Glossary/TLS) 로 대체되었다.


### 참고자료
- [HTTP 개요 - HTTP | MDN](https://developer.mozilla.org/ko/docs/Web/HTTP/Overview#http_%EA%B8%B0%EB%B0%98_%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98_%EA%B5%AC%EC%84%B1%EC%9A%94%EC%86%8C) 👈 해당 mdn 문서를 읽어보는 것을 추천합니다. 요약하기 어려울 정도로 설명, 정리가 잘 되어있습니다.
- [[HTTP] HTTP 기본](https://prohannah.tistory.com/152)
- [https://dkwjdi.tistory.com/252](https://dkwjdi.tistory.com/252)
- [HTTP 통신은 어떻게 진화하고 있나 - 테크레시피](https://techrecipe.co.kr/posts/11122)
- [HTTP/1 부터 HTTP/3 까지 알아보기](https://velog.io/@ziyoonee/HTTP1-%EB%B6%80%ED%84%B0-HTTP3-%EA%B9%8C%EC%A7%80-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0)
- [Understand HTTP3 in 5 minutes](https://www.jesuisundev.com/en/understand-http3-in-5-minutes/)
- [HTTP/3: the past, the present, and the future](https://blog.cloudflare.com/http3-the-past-present-and-future/)
- [https://dkwjdi.tistory.com/252](https://dkwjdi.tistory.com/252)
