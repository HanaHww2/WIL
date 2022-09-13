# 시작하기 전에
### 참고 자료)

- 드림코딩 엘리님 JS 기초 강의
    - [https://www.youtube.com/playlist?list=PLv2d7VI9OotTVOL4QmPfvJWPJvkmv6h-2](https://www.youtube.com/playlist?list=PLv2d7VI9OotTVOL4QmPfvJWPJvkmv6h-2)
- 부스트코스 윤지수님 풀스택 강의 
    - [https://www.boostcourse.org/web316/joinLectures/12943](https://www.boostcourse.org/web316/joinLectures/12943)


🥳 
- 모던 JS 튜토리얼 (KO) [https://ko.javascript.info/](https://ko.javascript.info/)

- 타입스크립트 참고) [https://www.typescriptlang.org/](https://www.typescriptlang.org/)

- 플레이그라운드를 활용해보자!
- 타입을 지정한 명확한 코딩이 가능하다!

> ES 6 이상을 모던JS라고 하며, 현대 JS의 기본 문법이라고 볼 수 있다. (일반적으로 사용된다)

> 💡 참고) [https://developer.mozilla.org/ko/docs/orphaned/Web/JavaScript/Reference](https://developer.mozilla.org/ko/>docs/orphaned/Web/JavaScript/Reference)

---
# 몇 가지 알아두면 좋은 것들

## 자바스크립트 관련 문서

- 자바스크립트의 공식 사이트
    - [https://www.ecma-international.org](https://www.ecma-international.org/)
- 조금 더 보기 쉬운 사이트
    - [https://developer.mozilla.org](https://developer.mozilla.org/)

## Developer Tool in Chrome

- ctrl + shift + i : Dev tool (in 크롬 브라우저)
- Elements탭은 HTML 작성시 활용
- Console탭에서 js를 동적으로 테스트해 볼 수도 있다.
- Sources탭은 디버깅에 유용 (breakpoint)
- Network탭은 네트워크의 발생과 데이터 전송에 대해 체크 가능
- 기타 : 퍼포먼스, 메모리 등 분석

# Wep API(Application Programming Interface)s?

- 브라우저가 제공하고 이해하는 함수들의 모음
- js와 별개 (js에 포함된 것이 아님)
- console api의 log 함수를 이용해서 메세지 출력 가능
- node.js를 설치하면, **Web APIs**(브라우저가 제공하는 함수들!, JS 언어에 포함되는 것이 아님) 중 Console api가 함께 설치되므로 로컬 환경(커맨드 창)에서 바로 JS 실행 결과를 확인할 수 있다.
    - node.js, Wep api가 동일한 인터페이스의 console 관련된 api를 가진다.
        - 통상적으로 많이 사용하는 api
        - Console api 관련 문서
            - [https://console.spec.whatwg.org/](https://console.spec.whatwg.org/)
            - [https://developer.mozilla.org/ko/docs/Web/API/Console_API](https://developer.mozilla.org/ko/docs/Web/API/Console_API)
            - [https://nodejs.org/api/console.html](https://nodejs.org/api/console.html)

# async vs defer

1. ``<head>`` 태그 안에 ``<script>`` 태그(js 파일)를 두는 경우
    - parsing HTML -> blocked -> fetching js -> executing js -> parsing HTML and then page is ready
    - js 파일이 너무 크다면, 클라이언트에 페이지가 출력될 때까지 너무 오랜 시간이 걸리기에 좋지 않다.
2. ``<body>`` 태그 가장 마지막 줄에 ``<script>`` 태그(js 파일)를 두는 경우
    - parsing HTML -> page is ready -> fetching js -> executing js
    - js가 fetching 되기 전에 사용자는 페이지의 컨텐츠를 먼저 확인 가능하다
    - 해당 웹사이트가 js에 의존적(의미있는 컨텐츠를 보려면 js를 이용한 동적 요소들이 필수적이라면)이라면 미완된 페이지에만 미리 접근이 가능하다
3. head + async 속성
    - parsing HTML + fetching js -> blocked -> executing js -> parsing HTML -> page is ready
    - async는 불리언 타입의 속성값이다
    - fetching이 parsing하는 동안 병렬적으로 진행, 다운로드 속도 향상된다.
    - js가 동적 변경/조작을 원하는 DOM 요소가 정의되기도 전에(HTML을 parsing하는 중간에) executing 된다
    - 다수의 스크립트 사용시, 먼저 fetching(다운로드)된 js를 실행하여 여러 번의 HTML parsing 도중 blocked 상태가 발생해 화면의 출력에 시간이 걸린다.
        - 정의된 순서와 무관하게 다운로드가 완료된 js 파일 순으로 실행된다.
        - 사용할 스크립트가 순서에 의존적인 경우에는 async 옵션 사용을 지양한다.
    - js를 실행하기 위해 parsing이 blocked 될 수 있어 페이지가 나타날 때까지 시간이 소요될 수 있다.
4. **head + defer 속성**
    - parsing HTML + fetching js -> page is ready -> executing js
    - 가장 안전하고 효율적인 옵션
    - HTML을 parsing 하는 동안 필요한 js 파일들을 모두 먼저 다운로드 한 다음, 페이지가 준비가 되면 등록된 순서대로 js 파일을 실행한다.
        - 다수 스크립트 사용시, 정의한 순서대로 스크립트를 실행한다

# ‘use strict’;

- 바닐라js 사용시 적용 추천
    - 타입스크립트에서는 필요 없는 옵션
- Whole-script strict mode syntax
- JavaScript is very flexible
    - flexible === dangerous
    - ex. 선언되지 않은 변수에 값을 할당, 기존의 프로토타입 변경
- added ECMAScript 5
- js 엔진이 조금 더 효율적으로 js 파일을 번역하므로 실행하는데 성능 개선이 가능하다.

### 출처

- 드림코딩 엘리님 강의
    - [https://www.youtube.com/watch?v=tJieVCgGzhs&list=PLv2d7VI9OotTVOL4QmPfvJWPJvkmv6h-2&index=2](https://www.youtube.com/watch?v=tJieVCgGzhs&list=PLv2d7VI9OotTVOL4QmPfvJWPJvkmv6h-2&index=2)