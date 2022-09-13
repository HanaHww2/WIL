# React 시작하기

- nodeJs를 설치할 필요가 있다.
    - npm(Node Package Module)이 함께 설치된다.
- npm 버전 5.2.0 이상이면 기본적으로 npx를 포함한다.
  - (그 이하 버전의 경우에는 npm의 CLI 도구인 npx를 추가로 설치한다.)
  - npx는 npm 레지스트리에 올라가 있는 패키지를 쉽게 설치하고 관리, 실행할 수 있도록 도와주는 CLI 도구이다. 
  - Package Runner 역할을 한다.
- 브라우저가 ReactJs를 이해할 수 있도록 Web pack 과 Babel을 함께 설치하여 활용한다.
  - create-react-app을 이용해서 필요한 모듈을 Set up 할 수 있다.
    - boiler plate를 제공한다.
  ```bash
  # 리액트 앱 설치 명령어
  npx create-react-app [APP_FOLDER_NAME]
  
  # 리액트 앱 실행
  npm start
  ```
### npm
패키지 의존성 관리 툴(라이브러리를 다운로드해서 빌드한다)이다. 
- 자바 언어에서의 maven, gradle과 같은 역할을 수행한다.
- 다운받은 라이브러리가 유지된다.
- 라이브러리 관리를 프로젝트별 혹은 글로벌하게 지정해서 할 수 있다.
  
### npx
npm 이후 새롭게 나온 의존성 관리 툴이다.

- 여러 프로젝트가 동일한 라이브러리를 사용한다면, 전역적으로 공통 라이브러리를 (캐싱하여) 활용하므로 중복해서 다운로드 받지 않고 재사용한다. (러너, 실행 위주)
- 필요한 라이브러리를 다운받아 실행시키고 난 이후에는 라이브러리를 삭제한다. (가벼움)

### Babel
- 자바스크립트 컴파일러
- JSX를 자바스크립트 문법으로 컴파일해주는 라이브러리
### Webpack
- 다수의 자바스크립트 파일을 하나의 파일로 합쳐주는 모듈 번들 라이브러리, 모듈 번들러

# React란?

- Node.js 기반의 JS UI 라이브러리
- 브라우저가 화면을 렌더링하는 성능을 높이기 위해 고안된 FrontEnd 라이브러리로, facebook에서 운영하는 프로젝트이다.
- 빈 HTML을 먼저 로딩한 뒤, 개발자가 생성한 **component**를 화면에 렌더링하는 방식을 이용해 성능을 높인다.
  - UI의 컴포넌트화를 통해서 코드의 중복을 줄이고, 용이하게 관리할 수 있다.
- **Virtual DOM**을 이용한다.
  - 브라우저의 소스코드(마우스 우클릭 > 페이지 소스 보기로 확인 가능하다) 상에서는 React가 렌더링한 component가 확인되지 않는다.
- 옵저버 패턴을 활용해 전달 받은 응답을 화면에 반영한다.
  - 데이터가 변경되면 리액트가 이를 감지하고 자동으로 화면 상태(UI)를 업데이트한다.
  - 리액트는 변경을 감지하는 **엔진(데몬 프로세스, Daemon)** 이다.
  - 그러므로, Node.js 서버를 통해 계속 구동되어야 한다.

- 간단히 말하면, React는 component를 이용해 HTML을 작성한다.
- **JSX** : React가 도입한 개념으로 JS와 HTML의 조합을 일컫는다.
    - 예를 들어 ``<App />`` 과 같이 사용하는 경우
  
### 실행 과정 
1. npm start 명령어를 입력하면, “react-scripts start” 명령어가 실행된다. 
    1. package.json에 설정되어 있다. 
    2. package.json에는 프로젝트에 관한 설정들이 담겨져 있다.
2. 실행된 위 명령어는 보통 index.js를 실행한다.
3. index.js 파일 내의 ReactDOM.render() 함수가 실행된다.
    1. 매개변수로 function 컴포넌트(JSX 문법 이용)와 rendering이 일어날 대상 DOM(public/index.html 내부의 요소)을 전달한다.
4. 결국 화면에 보여지는 화면(파일)은 **public/index.html** 이 된다.
    1. 이러한 특징으로 인해 리액트는 SPA(Single Page Application)라고 불린다.
    2. ``<a>`` 태그 등을 이용한 페이지 이동이 불가하므로 이를 대체하는 JSX 태그들이 존재한다.

# JSX
- JavaScript와 HTML의 조합/변형, JS 확장 문법
  - HTML과 유사한 구조를 갖고 있어 직관적이고 사용하기 간편하다.
  - HTML 코드를 JS 코드 내에서 사용하는 것으로 간주할 수도 있다.
- UI의 컴포넌트화를 쉽게 진행할 수 있다.
### 문법
1. return 시 하나의 DOM 요소만 리턴할 수 있다.
2. 변수 선언은 let(변수) 혹은 const(상수)로만 한다.
   a. HTML 태그 안에 {} 대괄호로 JS 변수의 변수명을 감싸 JS 변수를 활용할 수 있다.
3. if 문 사용이 불가능하다. 대신, 대괄호 내에 삼항 연산자를 쓸 수 있다.
4. 조건부 렌더링을 할 수 있다. ( { 조건 && 값(true인 경우 출력) } )
   1. {} 대괄호 내의 논리식이 true인 경우에만 렌더링이 수행된다.
5. css 디자인을 위한 2가지 방식
   1. 내부에 적는 방식
      1. 태그 내부에 style 속성값을 주는 방법 ( 권장하지 않음 )
         - <tag style={{ color : red }}>와 같이 작성할 수 있다.
         - const style = { color : red, }; 라는 상수를 생성해서 { style } 대괄호를 활용해 바인딩할 수도 있다.
   2. 외부 파일에 적는 방식 ( 권장 )
      1. css 파일을 작성하고 import 한다. 
         - 선택자를 클래스로 지정할 경우, 속성 className을 활용한다.
   3. 라이브러리를 사용하는 방식 ( 부트스트랩, **component-styled(추천)** )

<추가>
- 닫기 규칙 : 태그를 명확히 닫아준다. 
  - self-closing 태그를 활용할 수 있다.
- 최상위 태그 : 최상위 태그가 필요하다.
  - <React.Fragment> 태그로 대체 가능하다.
  - <> 빈 태그를 대신 사용할 수 있다.
- **{} curly brace(중괄호)** 를 활용하여, 스트링, 숫자, 함수 등을 전달받을 수 있으며, 삼항 연산자를 활용해 조건부 렌더링을 수행할 수 있다.

 
# Component와 Props

- JSX에서 Component는 대문자로 시작하는 class 혹은 funtion으로 생성할 수 있다.
    - function component
    
    ```jsx
    function Example(props) { // 전달된 property를 매개변수로 받을 수 있다.
    	return <h1>This is type {props.type}</h1>;
    }
    
    function App() {
    	return(
    	<div>
    		<Example type="A" /> <!-- 부모 component에서 자식 component로 property를 전달할 수 있다. -->
    	</div>
    	);
    }
    ```
    
    - class component
    
    ```jsx
    class App extends React.Component{ //React.Component를 상속한다.
    	// function이 아니므로 return 값이 없다. 대신 render 메소드를 상속받아 사용
    	render() { // 생성자처럼 자동 실행된다.
    		return <h1>It's a class component</h1>
    	}
    }
    ```
    
### Props
- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달하는 방식
### PropTypes 라이브러리

- 자식 component에 전달한 prop에 문제가 있는지 확인하는 것을 돕는다!

```jsx
Example.propTypes = {
	something: PropTypes.string,
	type: PropTypes.string.isRequired
};
```

# State

- class component가 가지고 있는 오브젝트 필드이다.
    - 동적 데이터를 담을 수 있다.
    - 그러나, 아래와 같이 state에 의존적인 것은 성능 문제 등을 유발할 수 있으므로, 좋은 코딩 방식은 아니다.

```jsx
class App extends React.Component {
  state = {
    count: 0
  };
  add= () => {
    // this.state.count = 1 로 작성시, 동작하지 않는다.
    // 직접 state를 변경하지 않고, setState를 사용해야,
    // state를 변경하며 render()을 수행해 변경된 사항을 함께 화면에 rendering한다.
		// 이때, react의 virtual DOM을 사용해, react는 변경된 부분만 빠르게 수정한다.
	  // this.setState({count: this.state.count + 1}); 와 같은 코드는
    // state에 의존적이며 성능 문제 등을 유발할 수 있어 좋은 코딩방식은 아니므로
		// 아래와 같이 코딩하는 것이 바람직하다.
    this.setState(current =>({count: current.count + 1})); 
  }
  minus= () => {
    this.setState(current =>({count: current.count + 1}));
  }
  render() {
    return (
      <div>
        <h1>The number is: {this.state.count}</h1>
        <button onClick={this.add}>Add</button>
        <button onClick={this.minus}>Minus</button>
      </div>);
  }
}
```

# Component Life Cycle 생명주기

docs 참고) [https://reactjs.org/docs/react-component.html#mounting](https://reactjs.org/docs/react-component.html#mounting)

### Mounting
- 컴포넌트가 생성될 때
    - 아래는 실행되는 메소드들 중 대표적인 몇 가지이다.
    - constructor()
    - render()
    - componentDidMount()

### Updating
- 컴포넌트가 수정될 때
    - 예를 들어 setState() 메서드를 이용해 state가 변경되어 컴포넌트가 수정될 때를 말한다.
    - render()
    - componentDidUpdate()

### Unmounting
- 컴포넌트가 DOM에서 삭제될 때를 말한다.
    - 페이지가 변경될 때, component를 교체할 때 등 다양한 경우를 일컫는다.
    - componentWillUnmount()

# React Hooks
- 클래스형 컴포넌트에서 사용하는 기능들을 함수형 컴포넌트에서도 사용할 수 있도록 도와주는 API

### useState
- 컴포넌트의 상태를 조작할 수 있다.

### useEffect
- 컴포넌트의 라이프사이클 변화에 따라 이벤트를 트리거할 수 있게 돕는다.
  - 의존 배열(dependency array) 매개변수에 [] 빈 배열로 전달하면 mounting 되는 순간의 이벤트를 제어할 수 있다.
  - 의존 배열을 전달하지 않고, 콜백함수만 전달하면, mounting, updating 순간의 이벤트를 제어할 수 있다.
  - 의존 배열에 특정한 상태 변수를 입력하면, 해당 상태가 mounting, updating 될 때 이벤트가 트리거된다.
  - useEffect의 콜백함수에서 반환하는 함수는 Unmount 시에 트리거 된다.

### useRef

참고자료) 
- NomadCoder, React JS 영화 앱 강의
- 메타코딩
- https://www.inflearn.com/course/%ED%95%9C%EC%9E%85-%EB%A6%AC%EC%95%A1%ED%8A%B8
