## 0. Class

- Object-oriendted programming
    - class
        - template, 청사진
        - field, method를 가질 수 있다.
        - encapsulation : 관련 있는 변수, 함수들을 묶어두고, 이를 내부적으로만 이용하거나, 외부에도 공개될 수 있도록 지정해 관리한다.
        - 상속, 다형성
    - object
        - instance of a class
- JavaScript classes
    - introduced in ES6
    - syntactical sugar over **prototype-based inheritance**

## 1. Class declarations

```jsx
'use strict';

class Person {
	// constructor
  constructor(name, age) {
    // fields
    this.name = name;
    this.age = age;
  }

  // methods
  speak() {
    console.log(`${this.name}: hello!`);
  }
}

const ellie = new Person('ellie', 20);
console.log(ellie.name);
console.log(ellie.age);
ellie.speak();
```

## 2. Getter and setters

```jsx
class User {
	// User의 필드는 firstName, lastName, _age 3가지
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }

  get age() {
		// 변수명을 age(this.age)로 두면, 재귀적으로 getter, setter의 호출을 반복하므로
		// 이(콜스택 크기를 초과한 호출)를 방지하기 위해, 변수명을 조금 다르게 작성한다.
    return this._age;
  }

  set age(value) {
		// 공격적으로 경고 메세지 출력
    // if (value < 0) {
    //   throw Error('age can not be negative');
    // }
    this._age = value < 0 ? 0 : value;
  }
}

const user1 = new User('Steve', 'Job', -1);// 나이는 음수가 될 수 없다
// .age를 이용하면, _age 필드에 바로 접근하는 것이 아니라 getter 연산자(age())가 호출된다.
console.log(user1.age); 
```

## 3. Fields (public, private)

```jsx
// Too soon!
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Class_fields
class Experiment {
  // 생성자 없이 필드 정의
	publicField = 2; // public
  #privateField = 0; // private
}
const experiment = new Experiment();
console.log(experiment.publicField); // 2
console.log(experiment.privateField); // undefined
```

## 4. Static properties and methods

- 클래스의 정적 변수, 메소드

```jsx
// Too soon!
class Article {
  static publisher = 'Dream Coding';
  constructor(articleNumber) {
    this.articleNumber = articleNumber;
  }

  static printPublisher() {
    console.log(Article.publisher);
  }
}

const article1 = new Article(1);
const article2 = new Article(2);
console.log(article1.publisher); // undefined

// 클래스에서 호출할 수 있는 변수와 메소드
// 클래스에서 공통적으로 사용할 수 있도록 한다.
console.log(Article.publisher);
Article.printPublisher();
```

## 5. Inheritance

- 상속, 다형성

```jsx
// a way for one class to extend another class.
class Shape {
  constructor(width, height, color) {
    this.width = width;
    this.height = height;
    this.color = color;
  }

  draw() {
    console.log(`drawing ${this.color} color!`);
  }
  getArea() {
    return this.width * this.height;
  }
}

class Rectangle extends Shape {}
class Triangle extends Shape {
	// 오버라이딩, 부모 메소드 재정의!
  draw() {
    super.draw(); // 부모의 메소드 그대로 호출
    console.log('🔺');
  }
  getArea() { 
    return (this.width * this.height) / 2;
  }
	// Object 클래스의 메소드 오버라이딩
  toString() {
    return `Triangle: color: ${this.color}`;
  }
}

const rectangle = new Rectangle(20, 20, 'blue');
rectangle.draw();
console.log(rectangle.getArea());

const triangle = new Triangle(20, 20, 'red');
triangle.draw();
console.log(triangle.getArea());
```

## 6. Class checking: instanceOf

```jsx
console.log(rectangle instanceof Rectangle); // true
console.log(triangle instanceof Rectangle); // false
console.log(triangle instanceof Triangle); // true

console.log(triangle instanceof Shape); // true
console.log(triangle instanceof Object); // true, JS의 모든 오브젝트의 root class
console.log(triangle.toString());

let obj = { value: 5 };
function change(value) {
  value.value = 7;
}
change(obj);
console.log(obj);
```