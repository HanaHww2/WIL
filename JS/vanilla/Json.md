- 참고) [https://tools.learningcontainer.com/json-validator/](https://tools.learningcontainer.com/json-validator/)
- 데이터 포맷, 통신 용도 외에도 object를 파일 시스템에 저장하는 용도로도 활용된다.
    - 가장 간단한 데이터를 주고 받을 수 있는 포맷
    - 가벼운 텍스트 기반 구조
    - 읽기 편리하다.
    - key-value 쌍 구조
    - 데이터 직렬화(Serialization)와 전송에 활용한다.
    - 프로그램 언어나 플랫폼에 독립적이다.

## 1. Object to JSON (Serialize)

- JSON.stringify(obj)

```jsx
'use strict';

let json = JSON.stringify(true);
console.log(json);

json = JSON.stringify(['apple', 'banana']);
console.log(json); // ["apple", "banana"] 더블쿼트를 가진 JSON 구조로 변경됨

const rabbit = { // Object
  name: 'tori', 
  color: 'white',
  size: null,
  birthDate: new Date(),
	symbol: Symbol("id"),
  jump: function () {
    console.log(`${this.name} can jump!`);
  },
};

json = JSON.stringify(rabbit);
console.log(json); 
// 함수 jump는 데이터가 아니므로, JSON에 포함되지 않는다
// Symbol과 같은 자바스크립트에만 있는 특별한 데이터의 경우에도 JSON에 포함되지 않는다.

json = JSON.stringify(rabbit, ['name', 'color', 'size']); // 배열로 특정 property 지정 가능
console.log(json);

json = JSON.stringify(rabbit, (key, value) => { // 콜백 함수를 이용해 조작
  console.log(`key: ${key}, value: ${value}`);
  return key === 'name' ? 'ellie' : value;
});
console.log(json);
```

## 2. JSON to Object (deSerialize)

- JSON.parse(json)

```jsx
json = JSON.stringify(rabbit);
console.log(json);

const obj = JSON.parse(json);
console.log(obj);
rabbit.jump();
// obj.jump(); 에러 발생, jump 함수는 JSON 타입으로 변환시 포함되지 않았기 때문이다.

console.log(rabbit.birthDate.getDate());
// 에러 발생, JSON 타입으로 변환되면서 데이터들은 string이 되기 때문이다.
console.log(obj.birthDate.getDate());

// 콜백함수를 활용해, 데이터의 타입을 변환해 파싱한다.
const obj = JSON.parse(json, (key, value) => { 
  console.log(`key: ${key}, value: ${value}`);
  return key === 'birthDate' ? new Date(value) : value;
});
```

## 3. 참고

- HTTP (Hypertext Transfer Protocol)
    - w3(웹) 상에서 서버와 클라이언트가 데이터(Hypertext, 문서, 이미지, 파일 등 여러 리소스를 일컫는다)를 주고받기 위한 프로토콜
    - request, response로 구성
- AJAX (Asynchronous Javascript And Xml)
    - HTTP 프로토콜에서 클라이언트가 서버에 동적으로 데이터를 요청해 받아오는 방법, 기술
    - XMLHttpRequest라는 브라우저 Web API에서 제공하는 객체(오브젝트)를 이용한다.
        - XML 외에 JSON 등 다양한 문서 형식을 이용할 수 있다.
        - 해당 기술을 개발하던 개발자들이 객체명을 지을 때, 너무 좁은 의미를 담게 작명했다. 객체나 API 명은 언제나 명료하게 짓도록 하자.
- 참고) 최근 브라우저에서는 fetch() API라는 더욱 간편한 기능을 제공한다.
- XML
    - HTML과 같은 마크업 언어 중 하나, 데이터를 표현하는 문서 방식
    - 불필요한 태그가 많아 가독성이 좋지 못하고, 파일 크기도 커진다는 단점이 있어 더는 많이 사용되지 않는다.
    - 대안으로 JSON이 활용된다.