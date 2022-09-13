# react-router-dom v6
### Route에서 props 전달하기
```jsx
<Route path="경로" element={<컴포넌트 props={props} />} />
```

### Routing시 상태 전달하기

```jss
# 링크 태그 이용시 상태 전달
<Link to={'/page1'} state={{ state: 'mystate' }} >Page 1</Link>
# 네비게이트 이용시 상태 전달
const navigate = useNavigate();
navigate('/posts', {state: { test: 'test'}})

# 라우팅 이후, 상태값 확인
import { useLocation } from 'react-router-dom';
const { state } = useLocation();

# 혹은
const location = useLocation();
const state = location.state;
```


### useEffect 사용 주의
- useEffect는 컴포넌트의 side effect를 처리하기 위한 함수
- 컴포넌트의 상태 (props, state)의 변화에 따라 상태를 이용해 리액트와 관련 없는 부수 작업(side effect, dom 직접변경, api호출 등)를 처리하기 위한 것

#### 참고자료
- https://velog.io/@commitnpush/useEffect%EC%9D%98-dependency-array