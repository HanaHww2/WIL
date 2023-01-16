# 도커를 활용한 젠킨스 설치

## DooD(Docker Out of Docker)?
- 도커의 컨테이너 내부에서 도커를 다시 활용하는 방법 중 하나를 말한다.
- 도커의 컨테이너 내부에서 외부 호스트(도커 엔진이 설치된 컴퓨터)의 도커 엔진을 `/var/run/docker.sock` 파일의 공유를 통해 활용할 수 있다. (이 때 도커 그룹 권한 설정이 필요하므로 주의한다.)

### DinD(Docker in Docker)
- 도커 컨테이너 안에 도커 엔진을 다시 설치하는 방식을 말한다.
- Docker 공식 사이트에서 비권장하는 방식이라는 글을 서치했었다.(시기가 언제인지 불명확하나 현재에도 그런지 확인하기 전이다.)
  > -> 여기서 쿠버네티스의 내부 동작에 또 의문이 생긴다. 쿠버네티스도 컨테이너 엔진을 활용하고, 하나의 컨테이너 내부에서 파드라는 단위의 서버를 동작시킨다.   
  쿠버네티스에서 각 컨테이너는 독립적인 엔진을 가지고 있고, 그 엔진으로 모든 파드를 관리하는 걸까? 
  파드 내부에서 컨테이너 엔진을 활용하는 일은 없나?.. 적고 나서 보니, 굉장히 추상적인 궁금증이다.  
  어쨌든, 실제로 클라우드 서버에서는 도커를 설치하기도 하니까... 그 뒷단이 새삼 궁금해진다.

### 결론
- 다만 사용자(나)의 컴퓨터에 한계가 있으므로 DooD 방식을 채택해본다.
- 또한 두 경우 모두 보안상 취약점이 있다고 한다.   
  - 특히 DooD는 그럴만도 한게, 내부에서 외부 docker engine 조작이 가능하기 때문에 경우에 따라 보안에 위협이 될 수도 있을 것이다.
  
#### 참고자료
https://rainbound.tistory.com/entry/docker-in-docker

### 도커로 젠킨스 설치
#### Dockerfile
```docker
FROM jenkins/jenkins

# 서치해본 결과 젠킨스 이미지는 데비안 OS를 활용하는 듯 하다.
# 이하 컨테이너 내부에 docker cli를 설치하기 위한 설정을 시행하고, 설치한다. 편리한 설치를 위해 root 계정 활용
USER root 
RUN apt-get update \
    && apt-get -y install lsb-release \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update \
    && apt-get -y install docker-ce-cli
# 호스트의 도커를 연결할 것이므로, 도커 엔진 등은 설치 생략한다. 
# docker-ce containerd.io

RUN groupadd docker && \
    groupmod -g 1001 docker && \
    usermod -aG docker jenkins
# 1001 은 volume 속성으로 전달해주는 docker.sock 에게 할당되는 그룹 아이디이다.
# ( 그룹 정보는 /etc/group 파일에서 확인 가능하다. )
# 컨테이너 내부에 docker라는 그룹명이 없어서 그룹 아이디로 확인된다고 하는데, 현재 그룹명을 생성해주었으니 한 번 결과를 살펴보아야 겠다.

USER jenkins
```
#### docker-compose.yml
```docker
version: "3"
services:
    jenkins:
        container_name: 'jenkins'
        image: 'jenkins-test'
        restart: unless-stopped
        ports:
            - '9090:8080'
            - '50000:50000'
        volumes:
            - './jenkins_home:/var/jenkins_home'
            - '/var/run/docker.sock:/var/run/docker.sock'
        user: root
```
- 현재 위와 같이 도커 이미지를 생성하고 컨테이너를 실행한 결과, jenkins 정상 동작 확인하였으며, 도커까지 DooD로 잘 연결된 것을 확인했다.
- 도커 컴포즈 버전에 대해서는 학습이 필요하다.

#### 기타 기록
- ubuntu docker 설치시 Package 'docker-ce' has no installation candidate 해결
  - apt-get -y install docker-ce-cli 명령어만 입력했을 때 패키지를 찾지 못했다는 오류가 발생한다. 공홈에서 하라는 대로 명령어를 실행한다. 아래 링크 참조
  - https://boying-blog.tistory.com/82
- cli를 설치해야 한다는 글을 보고, 실제로 cli 설치 전에 도커 명령어가 적용되지 않는 것을 확인했다.
> wsl 리눅스 서버를 통해서 /var/run 디렉토리를 확인해보니, docker.sock 외에도 docker-cli.sock이 있었다.   
> 그래서 docker-cli.sock 도 볼륨에 등록해보았는데.. 명령어는 동작하지 않았다.   
> 권한 문제가 아니라 cli 관련 에러가 나왔던 것으로 기억한다.  
> (역시 이래서, 그 때 그 때 캡쳐를 해둬야 한다. 벌써 가물가물... 작업 마무리하고 나중에 다시 테스트해보겠다.)

#### 참고자료
- https://postlude.github.io/2020/12/26/docker-in-docker/
- https://bitgadak.tistory.com/3

#### 최종 결론
- 진짜 결론: 젠킨스를 설치까지 했으나, 로컬에서 서버를 만들려면 포트 포워딩이 필요하고, 항상 컴퓨터를 켜두기 힘들다는 점,   
그리고 ec2 프리티어에 추가로 젠킨스 서버를 올리기엔 부담이 된다는 점(그냥 심적으로)을 이유로 github-action을 활용하는 것으로 결정했다.
