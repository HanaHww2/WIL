# 인덱스 (mySql 기준)
- 보통 인덱스가 db 저장 공간의 10~20 % 정도 (최소 5%)를 차지한다.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/62924471/204018349-84f9554e-44c7-412f-b1fc-5bea3e96b6eb.png">

### 인덱스 자동 생성 기준
<img width="600" alt="image" src="https://user-images.githubusercontent.com/62924471/204028401-afd176a6-417b-461b-926a-97bba727683a.png">

## 클러스터드 인덱스
- 테이블당 한 개만 생성할 수 있다.
- 헹 데이터를 인덱스로 지정한 컬럼(열)에 맞춰서 정렬된 상태로 저장한다.
- PRIMARY KEY를 지정하면 해당 컬럼으로 클러스터형 인덱스를 생성한다.

<img width="600" alt="image" src="https://user-images.githubusercontent.com/62924471/204032475-4125e42d-293e-4722-9711-0697d7cb3f48.png">
<img width="650" alt="image" src="https://user-images.githubusercontent.com/62924471/204032151-3a8c0796-9de7-4298-93e9-e0176044894b.png">

## 보조 인덱스 (Secondary Index, 논클러스터드 인덱스)
- 테이블당 여러 개 생성할 수 있다.
- Unique 속성을 지정하면 해당 컬럼을 이용해 보조 인덱스를 생성한다.

<img width="600" alt="image" src="https://user-images.githubusercontent.com/62924471/204032517-fef21208-8dc3-4be0-90d4-36dc0a48075f.png">

## B-Tree 구조
<img width="600" alt="image" src="https://user-images.githubusercontent.com/62924471/204028557-a63d359a-34d3-4d65-9ae6-89a98b3fe323.png">

### 페이지 분할 - 인덱스의 단점
- 삽입과 수정이 발생할 때, 경우에 따라 인덱스 자료구조의 변경이 유도되면서 작업의 효율이 떨어지게 된다.

### 인덱스 구조 예시
#### 인덱스가 없는 경우
<img width="600" alt="image" src="https://user-images.githubusercontent.com/62924471/204029259-101df0b5-d771-4e83-8a59-3ec6ff48f901.png">

#### 클러스터드 인덱스(userId)가 생성된 경우
<img width="600" alt="image" src="https://user-images.githubusercontent.com/62924471/204029308-7f563c7c-6c84-4312-b493-1fe4c9863da5.png">

- 데이터 페이지도 인덱스 구조에 포함된다.

#### 보조 인덱스(userId)를 생성하는 경우
<img width="600" alt="image" src="https://user-images.githubusercontent.com/62924471/204029608-ce896d5b-8ee8-4a75-a460-6fa47a9b16a8.png">

- 데이터 영역을 정렬하지 않는다.
- 리프 페이지를 별도로 생성한다.
- 조회시 클러스터드 인덱스에 비해 한 레벨을 더 거쳐서 실제 데이터에 접근하게 된다. (I/O 추가 발생)
- 범위 검색에서도 마찬가지로 클러스터드 인덱스에 비해 추가적으로 I/O가 더 발생하게 된다.

### 데이터 삽입 예
<img width="600" alt="image" src="https://user-images.githubusercontent.com/62924471/204031713-e4300f8e-7794-4270-b173-ea31326d4644.png">
<img width="600" alt="image" src="https://user-images.githubusercontent.com/62924471/204031737-35946cbb-5d78-4d0f-94c2-641c75461250.png">

- 보조 인덱스의 경우 데이터 페이지를 정렬할 필요가 없으므로, 새로운 데이터는 바로 기존 데이터 페이지의 가장 마지막 다음 빈 부분에 삽입이 된다.
  - 즉, 데이터 구조가 크게 변경될 여지가 적어 성능에 주는 부하도 적다.

#### OLTP/OLAP 시스템에서의 인덱스
<img width="700" alt="image" src="https://user-images.githubusercontent.com/62924471/204032720-256ce4cb-e942-4354-b33b-1b906d72528e.png">

### 클러스터드 인덱스와 보조 인덱스를 동시에 사용하는 경우
- 실무에서 사용하는 대부분의 db 테이블이 여기 해당함

### 참고 강의
- [2020개정판]이것이 MySQL이다 : https://www.youtube.com/watch?v=THZjyppzu90&list=PLVsNizTWUw7Hox7NMhenT-bulldCp9HP9&index=37
