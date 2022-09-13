## 1. String concatenation

```jsx
console.log('my' + ' cat');
console.log('1' + 2);
console.log(`string literals: 1 + 2 = ${1 + 2}`); 
// String literals를 이용하면, 따옴표나 특수기호(\n, \t 등)도 바로 인식 가능 (아래 예시)
console.log(`string literals:

	''1 + 2 = ${1 + 2}''`);
```

## 2. Numeric operators

```jsx
console.log(1 + 1); // add
console.log(1 - 1); // substract
console.log(1 / 1); // divide
console.log(1 * 1); // multiply
console.log(5 % 2); // remainder
console.log(2 ** 3); // exponentiation
```

## 3. Increment and decrement operators

```jsx
let counter = 2;
const preIncrement = ++counter;
// counter = counter + 1; 값의 증가 먼저
// preIncrement = counter;
console.log(`preIncrement: ${preIncrement}, counter: ${counter}`);
// preIncrement: 3, counter: 3

const postIncrement = counter++;
// postIncrement = counter; 할당 먼저
// counter = counter + 1;
console.log(`postIncrement: ${postIncrement}, counter: ${counter}`); 
// postIncrement: 3 , counter: 4

const preDecrement = --counter;
console.log(`preDecrement: ${preDecrement}, counter: ${counter}`);
// preDecrement: 3, counter: 3
const postDecrement = counter--;
console.log(`postDecrement: ${postDecrement}, counter: ${counter}`);
// postDecrement: 3, counter: 2
```

## 4. Assignment operators

```jsx
let x = 3;
let y = 6;
x += y; // x = x + y;
x -= y;
x *= y;
x /= y;
```

## 5. Comparison operators

```jsx
console.log(10 < 6); // less than
console.log(10 <= 6); // less than or equal
console.log(10 > 6); // greater than
console.log(10 >= 6); // greater than or equal
```

## 6. Logical operators: || (or), && (and), ! (not)

```jsx
const value1 = true;
const value2 = 4 < 2; // false

// || (or), 📌finds the first truthy value
// 가벼운 연산 혹은 true일 가능성이 큰 연산부터 나열한다.
console.log(`or: ${value1 || value2 || check()}`);

// && (and), finds the first falsy value
// 가벼운 값, 연산 혹은 false일 가능성이 큰 연산부터 나열한다.
console.log(`and: ${value1 && value2 && check()}`);

// often used to compress long if-statement
if (nullableObject != null) {
	if (nullableObject.something != null) console.log(nullableObject.something);
}
// 압축하면 nullableObject && nullableObject.something

function check() {
  for (let i = 0; i < 10; i++) {
    //wasting time
    console.log('😱');
  }
  return true;
}

// ! (not)
console.log(!value1); // false
```

## 7. Equality

```jsx
const stringFive = '5';
const numberFive = 5;

// == loose equality, with type conversion
console.log(stringFive == numberFive); // true
console.log(stringFive != numberFive); // false

// === strict equality, no type conversion
// 권장되는 방식
console.log(stringFive === numberFive); // flase
console.log(stringFive !== numberFive); // true

// object equality by reference
const ellie1 = { name: 'ellie' };
const ellie2 = { name: 'ellie' };
const ellie3 = ellie1;
console.log(ellie1 == ellie2); // false, reference가 다르다
console.log(ellie1 === ellie2); // false
console.log(ellie1 === ellie3); // true

// equality - puzzler
console.log(0 == false); // true
console.log(0 === false); // false, 타입이 다름
console.log('' == false); // true
console.log('' === false); // false

console.log(null == undefined); // true
console.log(null === undefined); // false 다른 타입
// 참고
console.log(undefined == false); // false
```

## 8. Conditional operators: if

```jsx
// if, else if, else
const name = 'df';
if (name === 'ellie') {
  console.log('Welcome, Ellie!');
} else if (name === 'coder') {
  console.log('You are amazing coder');
} else {
  console.log('unkwnon');
}
```

## 9. Ternary operator: ?

```jsx
// 간단한 조건문에 사용 권장
// condition ? value1(true) : value2(false);
console.log(name === 'ellie' ? 'yes' : 'no');
```

## 10. Switch statement

```jsx
// use for multiple if checks
// use for enum-like value check
// use for multiple type checks in TS
const browser = 'IE';
switch (browser) {
  case 'IE':
    console.log('go away!');
    break;
  case 'Chrome':
		//console.log('love you!');
    //break;
		//아래 케이스와 중복되므로 생략이 가능
  case 'Firefox':
    console.log('love you!');
    break;
  default:
    console.log('same all!');
    break;
}

```

## 11. Loops

```jsx
// while loop, while the condition is truthy,
// body code is executed.
let i = 3;
while (i > 0) {
  console.log(`while: ${i}`);
  i--;
} // 3, 2, 1 출력

// do while loop, body code is executed first,
// then check the condition.
do {
  console.log(`do while: ${i}`);
  i--;
} while (i > 0); // 3, 2, 1, 0 까지 출력

// for loop, for(begin; condition; step)
// 처음 begin은 딱 한 번만 실행된다.
for (i = 3; i > 0; i--) {
  console.log(`for: ${i}`);
}

for (let i = 3; i > 0; i = i - 2) {
  // inline variable declaration, 블록 내 지역변수로 선언
  console.log(`inline variable for: ${i}`);
}

// nested loops
// O(n^2)로 빅오가 커진다. 성능에 좋지 않다.
for (let i = 0; i < 10; i++) {
  for (let j = 0; j < 10; j++) {
    console.log(`i: ${i}, j:${j}`);
  }
}

// break(전체 루프 종료), continue(현재 루프 중단 후 다음 루프로 넘어간다)
// Q1. iterate from 0 to 10 and print only even numbers (use continue)
for (let i = 0; i < 11; i++) {
  if (i % 2 !== 0) {
    continue;
  }
  console.log(`q1. ${i}`); // 실제로는 짝수인 경우만 출력하는 방식을 권장
}

// Q2. iterate from 0 to 10 and print numbers until reaching 8 (use break), 8까지 출력
for (let i = 0; i < 11; i++) {
  if (i > 8) {
    break;
  }
  console.log(`q2. ${i}`);
}

// label을 이용한 loop 활용 구문도 있으나 현업에서는 그다지 활용하지 않는다.
// label을 이용하지 않아도 충분히 기능이 구현 가능하다.
// 참고) label이란? https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/label
```