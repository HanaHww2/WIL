# Docker 도커 기본 cheet-sheet
```bash
docker pull {image} # 이미지 가져오기

docker image ls # 저장한 이미지 조회
docker image rm {이미지 아이디} # 저장한 이미지 삭제

docker run # 컨테이너 설치
docker ps # 현재 컨테이너 조회
docker ps -a # 설치된 전체 컨테이너 조회

docker start
```
### 도커 컨테이너 내부 Bash 접속
```
docker exec -it {컨테이너명} bash
```
- exec은 실행 중인 컨테이너를 다루는 명령어이다.

### 도커 로그 보기
```bash
sudo docker logs jenkins # 로그 보기
```
### Dockerfile 예시
```Dockerfile
FROM node:16.13.2
WORKDIR /app
# package.json을 복사해서 디펜던시를 재설정 및 설치하는 레이어를 분리하여 최적화
COPY package.json . 
# npm 업그레이드를 수행하라고 도커가 시켜서 업그레이드 수행
RUN npm install -g npm@8.19.0
# 버전 오류가 났을 경우 해결을 위해 옵션
RUN npm install --save --legacy-peer-deps 
# 전체 파일 복사
COPY . .
EXPOSE 3000
CMD ["npm", "start"]

# docker build . 명령어 수행 - 현재 위치의 Dockerfile 을 실행한다.
```

### Dockerfile 을 이용한 이미지 생성
```
# 현재 위치의 기본 Dockerfile을 읽어서 빌드
docker build . 

# 도커 이미지의 이름 지정
docker build . -t {}

# 특정 도커 파일을 실행하기 위한 옵션
docker build -f {도커파일명} .
```

## 환경변수 설정
```
# in Dockerfile
ENV {환경변수명}={환경변수값}

# bash 명령어
-e {환경변수명}={환경변수값}

# 설정할 환경변수가 많다면 .env 파일을 생성해 활용한다.
# 와 같이 나열해서 설정할 수 있다.
{환경변수명}={환경변수값}

# 명령어에 파일 정보를 전달한다
--env-file ./.env
```

## 도커의 이미지 레이어
- Dockerfile을 이용할 때, 각 line 마다 이미지 레이어를 갖게 되고, 이 각 명령어 결과물은 캐싱이 된다.

## Volumes
- 공식문서 참고: https://docs.docker.com/storage/volumes/
- 도커의 bind mounts 보다 확장된 기능을 제공한다.
    - 호스트와 도커 컨테이너의 특정 디렉토리를 매핑하여 이를 싱크할 수 있다.
- volume을 생성해서 사용한다.

- 자세한 것은 더 학습이 필요함
  
```bash
# 윈도우 환경에서 잘 동작하지 않는 경우 아래의
# -e CHOKIDAR_USEPOLLING=true 를 명시하여 환경변수 수정 필요 
# 아래는 파워쉘 명령어이며, cmd에서는 %cd% 사용
# 혹은 전체 절대 경로 입력하여 사용 가능
docker run -e CHOKIDAR_USEPOLLING=true -v ${pwd}\src:/app/src -d -p 3000:3000 --name {컨테이너명} {이미지명}

# 리눅스 환경에서는 ${pwd} 대신 $(pwd)를 사용한다.
docker run -e CHOKIDAR_USEPOLLING=true -v $(pwd)/src:/app/src -d -p 3000:3000 --name {컨테이너명} {이미지명}

# read only 설정
# 매핑하는 경로 뒤 :ro 를 작성해두면,
# 컨테이너 내부에서 발생한 변경은 호스트 경로에 반영되지 않는다.
docker run -e CHOKIDAR_USEPOLLING=true -v ${pwd}\src:/app/src:ro -d -p 3000:3000 --name {컨테이너명} {이미지명}
```

## Dockerfile STAGE 설정

# Docker-compose
- docker-compose.yml 파일을 생성해 필요한 명령을 작성한다.
- docker-compose 명령어를 활용한다.
  - 🚩 **`docker compose`** 는 다른 명령어이므로 유의한다.
```
# 필요한 기능에 따라 선택
version: "3"
services:
  mylog-front:
    # 아래 두 설정을 통해서 -it 옵션을 설정할 수 있다
    stdin_open: true
    tty: true
    build: .
    ports:
      - "3000:3000"
    volumes:
      - ./src:/app/src:ro # 상대 경로 사용 가능, read only 설정
    environment:
      - CHOKIDAR_USEPOLLING=true
    # env_file:
    #   - ./.env
```

```
# 네트워크 생성, 설정한 컨테이너 전체 생성 및 실행
# but, Dockerfile의 변경 감지를 하지 못한다.
# 같은 명칭의 이미지가 있다면 그 이미지를 이용한다.
docker-compose up

# --build 옵션을 쓴다면 이미지를 새로 만든다.
docker-compose up --build

# 설정한 컨테이너 전체 중단 및 삭제
docker-compose down

# 특정 docker-compose 파일 지정 옵션
# 파일을 2개 지정하면, 후자가 전자를 덮어쓰면서 도커가 동작한다.
docker-compose -f {파일명} -f {또다른 파일명} up -d --build
```

### 빌드 설정
```
version: "3"
services:
  mylog-front:
    build:
      context: .
      dockerfile: Dockerfile.prod
      args:
        - REACT_APP_NAME=mylog
    ports:
      - "8080:80"
```
- Dockerfile에서 앱의 빌드가 수행되고 도커 컨테이너를 통해 동적으로 환경 변수(ENV) 값을 전달할 수 없는 경우에는 args 옵션을 사용해서 빌드 동작(RUN npm run build) 전에 환경 변수로 설정하려는 값을 전달할 수 있다.

#### 참고 자료
- [docker/docker-compose/nginx-react](https://www.youtube.com/watch?v=3xDAU5cvi5E&t=4365s)
  - 기초를 쌓기에 좋은 강의

### WSL 리눅스 OS에서 도커 활용하기
- https://docs.microsoft.com/ko-kr/windows/wsl/tutorials/wsl-containers
- 위 공식 문서 링크를 참고해 도커 데스크탑에서 설정만 해두면 된다! (다 해주는 WSL 덕에 편리해진다...)

### 우분투에서 도커 설치하기
- 공식 홈페이지 튜토리얼이 베스트/필수
```bash

```

#### permission denied 발생시 도커 그룹의 권한 부여
```bash
sudo usermod -aG docker $USER
# 특정 사용자에게 주는 경우
sudo usermod -aG docker {호스트명} 
```
- 재시작 필요함

#### 참고자료
- [초보를 위한 도커 안내서-subicura님](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html)
