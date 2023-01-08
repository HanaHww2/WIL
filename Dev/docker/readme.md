## contents
- [도커 / 도커 컴포즈 기본](./basic.md)
- [도커로 젠킨스 설치해보기](./install-jenkins.md)
- [vm에 도커 설치해보기](./install-vm.md)

## Docker?

### 간단 인프라 역사

- 과거 Bare Metal 환경
- Virtualization(가상화) 환경
  - Hypervisor X

- 현재 선호되는 환경
  - 어플리케이션 운영 서버의 자유로운 Scale IN & OUT (클라이언트 수요에 따라)
      - MSA(Micro Service Architecture)와 DevOps 환경에 적합하다.
  - 무중단 배포, 자동화 된 서비스 운영을 지원한다.
  - Bare Metal 혹은 Any Infrastructure 위에서 Container Engine 이용
      - 도커는 컨테이너 엔진 중 하나다.
      - 컨테이너로 운영되는 Application은 용량이 작다.
          - 최소화 된 환경과 Application을 포함하므로 작은 용량으로 운영이 가능하다.
          - OS는 컨테이너 엔진의 외부에 존재하므로, 컨테이너는 OS에 독립적이다.
          - 어플리케이션 운영 환경의 독립성을 갖는다.
      - 하나의 프로그램화가 되어서 isolate한 환경을 가지며, 확장성이 좋다. 또한 배포가 쉽다.

## 소프트웨어의 컨테이너
- Application을 운영하기 위해 필요한 환경을 담고 있는 독립된 공간을 말한다.
    - 라이브러리, 소프트웨어 플랫폼 등을 포함한다.

## Hypervisor

- vmware, virtual box, kvm, 젠서버 등의 Hypervisor 프로그램이 존재한다.
- 가상 머신(컴퓨터)을 생성할 수 있게 지원한다.
    - 하드웨어적으로는 분리되지 않았으나, 소프트웨어적으로 구분된 가상 머신

## 리눅스
- 컨테이너는 "리눅스 커널 기능"을 이용해 만들어졌기 때문에 리눅스 환경이 필요하다.
    - chroot : 독립된 공간 형성
    - namespace : 독립적으로 형성된 공간 내 6가지 isolate 기능 지원
    - cgroup : 필요한 만큼의 HW 지원
    - 리눅스 커널의 Storage, Namespaces, Networking 기능들을 도커 컨테이너 플랫폼에서 사용할 수 있게 컨테이너 엔진이 지원한다.
- 윈도우와 Mac OS에서는 시스템의 Hypervisor를 활성화 시켜 리눅스 커널 기능을 지원하고 그 위에서 컨테이너를 구동한다.
    - 실제 현업에서는 Hypervisor를 이용할 필요 없이 리눅스 기반으로 서비스를 운영한다.
