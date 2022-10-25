# 인덱스
- 테이블과 클러스터와 연관된 독립적인 객체(object)
- DB에 저장된 자료를 더욱 빠르게 조회하기 위해 활용
- 적절하게 사용하면, 조회 속도의 개선 뿐만이 아닌 디스크 I/O를 줄일 수 있는 수단이 된다.
 
## B*Tree 인덱스
- RDB에서 가장 많이 사용하고 있는 인덱스
  - B+Tree를 가장 많이 활용
  - MongoDB에서도 B+Tree를 활용한 인덱스 지원
- 인덱스 컬럼의 값이 **정렬**된 채로 저장
- Null 값은 저장하지 않음

### 구조
<img width='400' src='https://user-images.githubusercontent.com/62924471/197801794-fef04af0-0154-46ff-a34a-2e69af8572ee.png'>
<img width='400' src='https://user-images.githubusercontent.com/62924471/197801878-aa4fa93c-b387-4ec6-ab8f-73799bdee844.png'>

### ROWID
<img width='400' src='https://user-images.githubusercontent.com/62924471/197802062-87538592-9119-46c3-863f-051c3b0138a4.png'>

- 각 데이터의 저장 주소를 담고 있다.  
- 실행계획을 통해서 인덱스가 활용되는 것을 확인해 볼 수 있다.
<img width='400' src='https://user-images.githubusercontent.com/62924471/197802126-e6192fbb-7142-41bb-8c70-9da91dc220db.png'>

### 논리적 구조
- 리프노드에는 인덱스 컬럼의 모든 값이 정렬된 상태로 저장된다.
<img width='400' src='https://user-images.githubusercontent.com/62924471/197802258-c448f6d0-96b4-44e2-aab2-174aeb202f10.png'>

## B*Tree 인덱스 활용

### ORDER BY 정렬 작업 수행
- 인덱스를 활용한 오름차순/내림차순 범위 검색으로 정렬 수행
<img width='500' src='https://user-images.githubusercontent.com/62924471/197811207-59f89ee7-196b-436b-8b08-a368e6eabdfc.png'>

### MIN/MAX 값 탐색 수행
<img width='500' src='https://user-images.githubusercontent.com/62924471/197811966-80624363-956d-4334-b6c7-a615a7c88f64.png'>

- 이미 정렬되어 있는 인덱스 데이터를 (힌트로) 활용해 최대/최솟값에 조회 수행(ROWNUM으로 최대/최소값만 조회)

# 인덱스 스캔의 동작원리
<img width='600' src='https://user-images.githubusercontent.com/62924471/197803555-c119dfd5-1a62-4e63-b75f-0e8b201fb723.png'>

- ROWID에 의존
  - 각 ROWID는 하나의 블록 정보를 갖는다.

## 인덱스 선정 기준
- 일반적으로 컬럼의 카디널리티가 10~15% 미만인 경우에 효율적이다.
<img width='400' src='https://user-images.githubusercontent.com/62924471/197803705-2521a3c4-128b-40e1-85e2-aa401e7505aa.png'>


### cardinality와 분포도

## 인덱스가 활용되지 않는 경우 (B-Tree 기준)
### NOT 연산자
<img width='400' src='https://user-images.githubusercontent.com/62924471/197804114-f7b48870-77bb-4896-a6a3-4c6ff1e47e1b.png'>

### IS NULL or IS NOT NULL
- 인덱스는 Null 값을 갖지 않기 때문에 무용하다.
<img width='400' src='https://user-images.githubusercontent.com/62924471/197804203-076d73e3-235a-499d-8bcf-c4dc33db61d9.png'>

### External Suppressing
- 인덱스 컬럼의 값에 변형을 수행하여, 인덱스를 활용할 수 없게 되는 경우
<img width='400' src='https://user-images.githubusercontent.com/62924471/197804381-d140561e-813f-4316-beb0-e6af6739ca83.png'>

### Internal suppressing
- 서로 다른 타입의 값끼리 비교하게 되는 경우에 발생한다.
  - 컬럼의 데이터 타입이 변환되는 경우 
<img width='400' src='https://user-images.githubusercontent.com/62924471/197804427-169d136f-d9cb-4c75-b8f4-a467d98f52ba.png'>

## 결합인덱스
<img width='400' src='https://user-images.githubusercontent.com/62924471/197804565-2bed84c4-b454-41d0-8e54-134d3d0bb348.png'>

### 결합 인덱스 활용 예시
- 결합 인덱스의 활용이 가능한 조건절 예시
  - 결합 인덱스 중 첫번째 컬럼이 정상적인 조건을 가진 채로 이어진다면, 결합 인덱스를 활용하게 된다.
<img width='400' src='https://user-images.githubusercontent.com/62924471/197814636-9239d70c-2902-4af4-a1cf-4b974d7fc1fb.png'>

- 결합 인덱스의 활용이 불가능한 조건절 예시
  - 결합 인덱스 중 첫번째 컬럼의 조건이 없거나 부적절한 조건인 경우
<img width='400' src='https://user-images.githubusercontent.com/62924471/197805012-7ffbba9f-5f2c-4a1c-bf0e-ae206b367daf.png'>

### Index Skip Scanning
<img width='400' src='https://user-images.githubusercontent.com/62924471/197814870-7b09a229-e369-4d0a-9463-76b4f2d2fb04.png'>

### 칼럼 순서 결정
- 인덱스의 컬럼은 순서순으로 중요하다.
<img width='400' src='https://user-images.githubusercontent.com/62924471/197815367-2fc46f18-824a-40d3-a3df-60569498b104.png'>

### 결합 인덱스 사용시 범위 조건과 '=' 조건 사용 캐이스
<img width='500' src='https://user-images.githubusercontent.com/62924471/197805672-825ecb16-3c10-49ae-b4ea-5031f9824c2c.png'>
<img width='500' src='https://user-images.githubusercontent.com/62924471/197805938-e4ffb5b8-d681-4699-a809-b95905e14186.png'>

### 참고내용
- youtube.com/watch?v=db7Gk3K1Ru0&t=601s
