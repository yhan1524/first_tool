# 개발 워크스테이션 구축

## 1. 프로젝트 개요
- 터미널, Docker, Git/GitHub를 사용해 재현 가능한 개발 환경 구축

## 2. 실행 환경
- OS: Windows_NT
- Shell: 5.1.26100.9711
- Docker version: 29.9.2, build a82e528
- Git version: 2.56.0.windows.4

## 3. 수행 항목 체크리스트
- [ ] 터미널 기본 조작
- [ ] 파일/디렉토리 권한 실습
- [ ] Docker 설치 및 점검
- [ ] Docker 기본 운영 명령
- [ ] hello-world 실행
- [ ] ubuntu 컨테이너 진입
- [ ] Dockerfile 기반 커스텀 이미지 빌드
- [ ] 포트 매핑 접속 확인
- [ ] 바인드 마운트 반영 확인
- [ ] Docker 볼륨 영속성 확인
- [ ] Git 설정
- [ ] GitHub/VSCode 연동

## 4. 터미널 조작 로그
Get-Location(현재위치 확인)
![현재위치 확인](screenshot/pwd.png)

ls -Force(목록확인) *Get-ChildItem -Force
![목록 확인](screenshot/ls.png)

Set-Location 폴더명(이동) *cd 폴더명
![폴더 이동](screenshot/cd.png)
*상위 폴더로 이동은 cd ..
![폴더 이동](screenshot/cd_up.png)

New-Item -ItemType Directory 폴더명(폴더 만들기)
![폴더 만들기](screenshot/newfolder.png)

New-Item -ItemType File 파일명(파일 만들기)
![파일 만들기](screenshot/newfile.png)

Copy-Item a b (복사)
![복사](screenshot/copy.png)
폴더 안의 내용까지 복사는 뒤에  -Recurse를 붙인다

Move-Item 원본 대상경로(이동)
![이동](screenshot/move.png)

Rename-Item 기존이름 새이름(이름변경)
![이름변경](screenshot/rename.png)

Remove-Item 파일명(삭제)
![삭제](screenshot/remove.png)

Get-Content 파일명(파일 내용 확인) *cat 파일명
![파일내용확인](screenshot/cat.png)

New-Item -ItemType File 파일명(빈 파일 생성)
![빈파일 생성](screenshot/bin.png)

## 5. 권한 실습
icacls(권한 확인)
![권한 확인](screenshot/chmod.png)

/grant:r(권한 변경)
![권한 변경](screenshot/grant1.png)
![권한 변경](screenshot/grant2.png)

## 6. Docker 설치 및 점검
docker --version
![버전확인](screenshot/dockerver.png)

docker info
![동작여부확인](screenshot/dockerinfo.png)

## 7. Docker 기본 운영 명령

docker run hello-world
![helld-world 생성](screenshot/dockerhello.png)

docker images
docker ps -a
![이미지 및 목록 확인](screenshot/dockerimg.png)

docker run -it ubuntu bash
![ubuntu 컨테이너 실행 및 진입](screenshot/dockerbash.png)

ls, echo exit
![컨테이너 진입 후 간단 명령](screenshot/dockerls.png)

docker run -d --name my-nginx-container -p 8080:80 
![포트매핑 실행명령](screenshot/dockermapping.png)

curl http://localhost:8080 
![호스트 포트 접속](screenshot/dockercurl.png)

docker volume create my-nginx-data
docker run -d --name my-nginx-volume -p 8082:80   -v my-nginx-data:/usr/share/nginx/html   nginx:alpine
![Docker 볼륨 생성 및 ](screenshot/dockercurl.png)

## 8. 커스텀 이미지 제작
## 9. 포트 매핑 검증
## 10. 바인드 마운트 검증
## 11. Docker 볼륨 영속성 검증
## 12. Git 설정 및 GitHub 연동
## 13. 트러블슈팅
## 14. 핵심 개념 정리