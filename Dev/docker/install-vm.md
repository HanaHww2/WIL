- 1년도 더 전에 작성한 내용이라 업데이트 필요함

## 도커의 설치 단계

1. 오라클이 지원하는 Hypervisor인 Virtual Box를 이용해 VM(가상머신)을 만들어 준다.
2. VM 간 통신이 지원되어야 하며, 외부와의 통신도 가능하도록 NAT 네트워크를 구성한다.
3. 리눅스 OS를 설치하고, 도커를 구성한다.
- wsl2 는 아직까지 Docker Desktop 버전만 지원하므로, 서버 역할보다는 개발 환경 설정에 목적을 두고 있다. 즉, vmware(유료) 혹은 Virtual Box를 설치해 구성한다.

### VM 생성
### Virtual Box 다운로드 후 설치

- [https://www.virtualbox.org/](https://www.virtualbox.org/)
- 디폴트 설정 그대로 설치

### Virtual Box 의 Network 구성

- VM 간 통신과 외부 통신을 위한 **NAT 네트워크** 구성
- 파일 - 환경설정 - 네트워크 - 추가 GUI를 이용해 NAT 네트워크를 추가
- NAT 네트워크 이름과 CIDR(네트워크 대역폭) 설정, DHCP 지원
- 가상 머신의 원격 로그인 지원을 위해 22번 포트(SSH 데몬)을 이용하는 포트 포워딩 구성

<img width=700 src="https://user-images.githubusercontent.com/62924471/211177169-136bb8a2-03d7-4762-8434-fdeeaab31ff0.png">

### 가상 머신 만들기

- virtual box GUI를 이용해 이용자의 Bare Metal 성능에 맞게 적절히 CPU 코어와 메모리, 저장소 크기를 지정해 VM을 구성한다.
    - 최소 CPU 2core, Memory 4GB(4096), disk(20GB)
    - 도커 GUI를 이용하려면 메모리가 최소 4GB는 필요하다.

## VM에 OS 설치하기

### ubuntu 20.04(LTS) 설치

- 매년 4월에 출시되는 버전이 LTS (Long Term Support)로 장기간에 지원되므로, LTS 버전을 권장한다.
    - 그 외 버전은 9개월 지원한다.
- [https://ubuntu.com/](https://ubuntu.com/) 에서 desktop 버전(GUI 포함)으로 iso 파일을 다운로드한다.

### 기본 구성

- 설치 된 우분투의 디스플레이 설정을 조정해 화면 크기를 조절할 수 있다.

### 네트워크 구성

- 네트워크 설정을 DHCP(동적 아이피 할당, 우분투 default)에서 static IP로 변경한다.
    - 네트마스크는 CIDR 값을 준다.
    - 게이트웨이는 VirtualBox에 설정한 네트워크 대역에서 가장 앞 번호로 설정하게 된다. (선택할 수 있는 것이 아님)
    - DNS도 게이트웨이와 같은 주소를 갖는다.
    
    <img width=400 src="https://user-images.githubusercontent.com/62924471/211177160-4541a0d3-207e-4a63-a100-2d84bbadb906.png">

- 터미널을 이용해 정보를 확인하고 필요한 설정을 등록/변경한다.
    
    ```bash
    # ip addr 확인 - 10.100.0.105/24
    ip addr
    # hostname 확인 - docker-ubuntu 로 vb에 설정한 이름 확인됨
    # docker-ubuntu.example.com으로 수정한다.
    hostname
    
    # hostname 변경하기 위해서 파일 수정
    sudo vi /etc/hostname
    
    # docker-centos와 docker-ubuntu 간의 통신을 위해서,
    # 각각의 ip addr과 hostname을 등록 (아래 이미지 첨부)
    sudo vi etc/hosts
    
    # 외부 네트워크( 8.8.8.8 > 구글 DNS주소 이용)와 통신 확인
    # -c 3 카운터 3개 이용
    ping -c 3 8.8.8.8
    ```

    <img width=500 src="https://user-images.githubusercontent.com/62924471/211177081-2f931cc0-2ed4-43be-adbc-3a025a36ceda.png">


### cli(텍스트) 환경으로 디폴트를 변경(하드웨어 리소스 절약)

### +) 루트 사용자 설정

```bash
# 루트 사용자 활성화를 위해 루트 계정 비밀번호 설정
sudo passwd root
# 루트 사용자로 전환
su - root

# 텍스트 모드로 디폴트 설정을 변경
systemctl set-default multi-user.target
```

### 원격 접속을 위한 구성

```bash
# 애플리케이션 레파지토리 버전 등 확인 위해 업데이트 실시
apt-get update

# -y 옵션은 yes, 중간 질문이 있으면 모두 yes
# openssh-server, curl 커맨드, tree 커맨드, vim 에디터 설치
apt-get install -y openssh-server curl tree vim
```

- openssh 서버 설치
    - openssh 서버는 remote 시스템에서 해당 서버에 접속할 수 있도록, port를 열어서 대기하는 서비스 데몬이다.
    - 예를 들어 윈도우에서 우분투 서버에 접속이 가능하다.
- curl 은 커맨드 라인에서 웹 브라우징을 제공한다.

```bash
# opnssh-server 설치 후 ssh 데몬 동작 확인해보기
systemctl status sshd

# 실행 접속 test를 통해 확인
# 최초 접속시 fingerprint를 입력받는다고 한다. yes 
ssh hanah@localhost

# 로그아웃
exit
```

### window 터미널 에뮬레이터

- xshell, putty, secure crt 등 다양한 윈도우 프로그램 중 하나를 이용한다.
- 윈도우 powershell 에서 제공하는 ssh 명령어를 활용할 수도 있다.

### linux 명령어

```bash
su - # 루트 사용자로 전환
exit # 다시 일반 사용자로
ip addr # ip addr
cat /etc/os-release # os 확인
free -h # 현재 시스템의 메모리 사용량 정보를 humanreadable 사이즈로 확인 
uname -r  # 설치된 커널의 버전 확인
sudo systemctl isolate graphical.target # gui 모드로 전환, multiuser.target은 cli 모드
```

#### 참고) 따배런 도커 시리즈
- [https://www.youtube.com/playlist?list=PLApuRlvrZKogb78kKq1wRvrjg1VMwYrvi](https://www.youtube.com/playlist?list=PLApuRlvrZKogb78kKq1wRvrjg1VMwYrvi)

### WSL2에 DockerDesktop 설치하기

- 검색해보다가 virtual box와 wsl2 충돌 관련 글(하나의 가상화 툴(HyeprV)만 동작이 가능하기 때문이라고 함. )을 보았지만, 최신 업데이트 이후로 충돌이 없다고 한다. 나란 쫄보🤣 여하간 이제 안심하고 데탑에도 wsl2 설치한다 Yeyy!!
    - 출처) [https://velog.io/@ynoolee/wsl-2와-hyper-v-그리고-virtualbox-충돌](https://velog.io/@ynoolee/wsl-2%EC%99%80-hyper-v-%EA%B7%B8%EB%A6%AC%EA%B3%A0-virtualbox-%EC%B6%A9%EB%8F%8C)
