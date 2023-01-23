# Object
- one of the JavaScript's data types.
- a collection of related data and/or functionality.
- Nearly all objects in JavaScript are instances of Object
- object = { key : value };

## 1. Literals and properties

```jsx
'use strict';

const obj1 = {}; // 'object literal' syntax
const obj2 = new Object(); // 'object constructor' syntax

function print(person) {
  console.log(person.name);
  console.log(person.age);
}

const ellie = { name: 'ellie', age: 4 };
print(ellie);

// with JavaScript magic (dynamically typed language)
// can add properties later
ellie.hasJob = true;
console.log(ellie.hasJob);

// can delete properties later
delete ellie.hasJob;
console.log(ellie.hasJob);
```

## 2. Computed properties

```jsx
// key should be always string
console.log(ellie.name); // dot 연산자, 일반적으로 사용

// Computed properties ->  object['key'], 동적으로 키 값을 받아올 때 활용
console.log(ellie['name']);

ellie['hasJob'] = true;
console.log(ellie.hasJob);

function printValue(obj, key) {
  console.log(obj[key]);
	// console.log(obj.key);
	// 동적으로 변수를 조작할 수 없다. obj에 key라는 이름의 프로퍼티를 확인해 undefiend를 반환.
}
printValue(ellie, 'name');
printValue(ellie, 'age');
```

## 3. Property value shorthand

- key와 value의 이름이 동일하다면, key의 명칭을 생략해주어도 JS 엔진이 자동적으로 key 값을 동일하게 설정한다.

```jsx
const person1 = { name: 'bob', age: 2 };
const person2 = { name: 'steve', age: 3 };
const person3 = { name: 'dave', age: 4 };

const person4 = makePerson('elile', 30);
console.log(person4);

function makePerson(name, age) {
	return {
		name,	// name: name, Property value shorthand
		age
	};	
} // 오브젝트를 생성하는 역할만 하는 함수이므로, 아래와 같이 Constructor Function으로 수정한다.
```

## 4. Constructor Function

- 오브젝트를 생성하는 함수
- 동일한 property를 갖는 오브젝트를 여러 개 만들 때 유용하다.

```jsx
const person5 = new Person('elile', 30);

function Person(name, age) {
  // this = {};
  this.name = name;
  this.age = age;
  // return this;
}
```

## 5. in operator: property existence check (key in obj)

```jsx
console.log('name' in ellie); // true
console.log('age' in ellie); // true
console.log('random' in ellie); // false
console.log(ellie.random); // undefined
```

## 6. for .. in vs for .. of

```jsx
// for (key in obj)
for (let key in ellie) {
  console.log(key);
}

// for (value of iterable)
const array = [1, 2, 4, 5];
for (let value of array) {
  console.log(value);
}
```

## 7. Fun cloning

```jsx
const user = { name: 'ellie', age: '20' };
const user2 = user;
user2.name = 'coder';

console.log(user);

// 1) old way, 매뉴얼하게 복제된다.
const user3 = {};
for (let key in user) {
  user3[key] = user[key];
}
console.clear();
console.log(user3);

// 2) Object.assign(target, [obj1, obj2, obj3...])
const user4 = Object.assign({}, user);
console.log(user4);

// another example
const fruit1 = { color: 'red' };
const fruit2 = { color: 'blue', size: 'big' };

const mixed = Object.assign({}, fruit1, fruit2);
console.log(mixed.color); // blue
console.log(mixed.size); // big
```


## +) 추가
TODO
### 출처
- [https://www.boostcourse.org/web316/lecture/16795?isDesc=false](https://www.boostcourse.org/web316/lecture/16795?isDesc=false)
- [https://www.youtube.com/watch?v=cTR00wW-kZo&list=PLuHgQVnccGMAMctarDlPyv6upFUUnpSO3&index=8&t=11s](https://www.youtube.com/watch?v=cTR00wW-kZo&list=PLuHgQVnccGMAMctarDlPyv6upFUUnpSO3&index=8&t=11s)

## 8. prototype
