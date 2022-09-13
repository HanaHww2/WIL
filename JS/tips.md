# 쿼리스트링
```js
// 인코딩된 쿼리 파라미터
Object.entries(obj).map(([key, val]) => `${key}=${encodeURIComponent(val)}`).join('&')

// URLSearchParams 객체를 사용하는 경우
let params = new URLSearchParams();
params.append('categoryId', encodeURIComponent(searchParams.categoryId));
```