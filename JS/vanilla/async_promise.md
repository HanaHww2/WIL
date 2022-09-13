- 비동기의 간편한 처리 기능을 제공하는 자바스크립트 객체
- State: pending(오퍼레이션 수행 중) -> fulfilled(성공) or rejected(실패)
- Producer vs Consumer

## 1. Producer

- 정보 제공자
- 프로미스 객체가 생성될 때, 동시에 인자로 받는 executor(콜백 함수)가 바로 실행된다.

```jsx
'use strict';

const promise = new Promise((resolve, reject) => {
  // doing some heavy work (with network, reading files)
  console.log('doing something...');
  setTimeout(() => {
    resolve('ellie');
    // reject(new Error('no network'));
  }, 2000);
});
```

## 2. Consumers: then, catch, finally

- 정보를 받고 소비하는 입장

```jsx
promise 
  .then(value => { // 정상 수행시, resolve 콜백함수에서 전달된 값을 받아와 수행한다.
    console.log(value);
  })
  .catch(error => { // 실패시, 에러 핸들링
    console.log(error);
  })
  .finally(() => { // 성공, 실패와 무관하게 무조건 실행된다.
    console.log('finally');
  });
// chaining : then 과 catch 함수의 리턴값은 promise이기에 연이어서 관련 함수를 체이닝할 수 있다.
```

## 3. Promise chaining

```jsx
const fetchNumber = new Promise((resolve, reject) => {
  setTimeout(() => resolve(1), 1000);
});

fetchNumber // then에서는 결과값 혹은 또 다른 Promise 비동기 객체를 반환할 수 있다.
  .then(num => num * 2)
  .then(num => num * 3)
  .then(num => {
    return new Promise((resolve, reject) => {
      setTimeout(() => resolve(num - 1), 1000);
    });
  })
  .then(num => console.log(num)); // 5
```

## 4. Error Handling

```jsx
const getHen = () =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve('🐓'), 1000);
  });
const getEgg = hen =>
  new Promise((resolve, reject) => {
		//setTimeout(() => resolve(`${hen} => 🥚`), 1000);
    setTimeout(() => reject(new Error(`error! ${hen} => 🥚`)), 1000);
  });
const cook = egg =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve(`${egg} => 🍳`), 1000);
  });

getHen() //
  .then(getEgg)
	//.catch(error => return '🎁';
	//.then(hen => getEgg(hen)) 위와 같다. 콜백 함수에서 하나의 매개변수 전달은 생략 가능
  .then(cook)
  .then(console.log)
  .catch(console.log);
```

## 5. callback to promise

```jsx
// Callback Hell example 리팩토링
class UserStorage {
  loginUser(id, password) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (
          (id === 'ellie' && password === 'dream') ||
          (id === 'coder' && password === 'academy')
        ) {
          resolve(id);
        } else {
          reject(new Error('not found'));
        }
      }, 2000);
    });
  }

  getRoles(user) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (user === 'ellie') {
          resolve({ name: 'ellie', role: 'admin' });
        } else {
          reject(new Error('no access'));
        }
      }, 1000);
    });
  }

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your passrod');
userStorage
  .loginUser(id, password)
  .then(userStorage.getRoles)
  .then(user => alert(`Hello ${user.name}, you have a ${user.role} role`))
  .catch(console.log);
```