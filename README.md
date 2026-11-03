# 개발 워크스테이션 구축

## 1. 프로젝트 개요
터미널, Docker, Git/GitHub를 사용해 재현 가능한 개발 환경 구축

---

## 2. 실행 환경

| 항목 | 내용 |
|---|---|
| OS | Windows_NT |
| Shell | 5.1.26100.9711 |
| Docker version | 29.9.2, build a82e528 |
| Git version | 2.56.0.windows.4 |

### 2-1 프로젝트 디렉토리 구조
```
first_tool/
├─ README.md
├─ Dockerfile
├─ app/
   └─ index.html
└─ assets/
```
단순하게 나누어 저장함
'assets/' 출력할 실행 증거 이미지모음
'app/' index 파일

---

## 3. 수행 항목 체크리스트

- [x] 터미널 기본 조작
- [x] 파일/디렉토리 권한 실습
- [x] Docker 설치 및 점검
- [x] Docker 기본 운영 명령
- [x] hello-world 실행
- [x] ubuntu 컨테이너 진입
- [x] Dockerfile 기반 커스텀 이미지 빌드
- [x] 포트 매핑 접속 확인
- [x] 바인드 마운트 반영 확인
- [x] Docker 볼륨 영속성 확인
- [x] Git 설정
- [x] GitHub/VSCode 연동

---

## 4. 터미널 조작 로그

### 4-1. 현재위치 확인
```powershell
Get-Location
```

![현재위치 확인](assets/pwd.png)

### 4-2. 목록 확인
```powershell
ls -Force
```
`Get-ChildItem -Force`

![목록 확인](assets/ls.png)

### 4-3. 폴더 이동
```powershell
Set-Location 폴더명
```
`cd 폴더명`

![폴더 이동](assets/cd.png)

상위 폴더로 이동:
```powershell
cd ..
```

![폴더 이동](assets/cd_up.png)

### 4-4. 폴더 만들기
```powershell
New-Item -ItemType Directory 폴더명
```

![폴더 만들기](assets/newfolder.png)

### 4-5. 파일 만들기
```powershell
New-Item -ItemType File 파일명
```

![파일 만들기](assets/newfile.png)

### 4-6. 복사
```powershell
Copy-Item a b
```

![복사](assets/copy.png)

폴더 안의 내용까지 복사할 때는 뒤에 `-Recurse`를 붙인다.

### 4-7. 이동
```powershell
Move-Item 원본 대상경로
```

![이동](assets/move.png)

### 4-8. 이름변경
```powershell
Rename-Item 기존이름 새이름
```

![이름변경](assets/rename.png)

### 4-9. 삭제
```powershell
Remove-Item 파일명
```

![삭제](assets/remove.png)

### 4-10. 파일 내용 확인
```powershell
Get-Content 파일명
```
`cat 파일명`

![파일내용확인](assets/cat.png)

### 4-11. 빈 파일 생성
```powershell
New-Item -ItemType File 파일명
```

![빈파일 생성](assets/bin.png)

---

## 5. 권한 실습

### 5-1. 권한 확인
```powershell
icacls
```

![권한 확인](assets/chmod.png)

### 5-2. 권한 변경
```powershell
/grant:r
```

![권한 변경](assets/grant1.png)
![권한 변경](assets/grant2.png)

---

## 6. Docker 설치 및 점검

### 6-1. 버전확인
```bash
docker --version
```

![버전확인](assets/dockerver.png)

### 6-2. 동작여부확인
```bash
docker info
```

![동작여부확인](assets/dockerinfo.png)

---

## 7. Docker 기본 운영 명령

### 7-1. hello-world 실행
```bash
docker run hello-world
```

![hello-world 생성](assets/dockerhello.png)

### 7-2. 이미지 및 컨테이너 목록 확인
```bash
docker images
docker ps -a
```

![이미지 및 목록 확인](assets/dockerimg.png)

### 7-3. ubuntu 컨테이너 실행 및 진입
```bash
docker run -it ubuntu bash
```

![ubuntu 컨테이너 실행 및 진입](assets/dockerbash.png)

### 7-4. 컨테이너 진입 후 간단 명령
```bash
ls
echo exitcur
```

![컨테이너 진입 후 간단 명령](assets/dockerls.png)

### 7-5. 포트매핑 실행명령
```bash
docker run -d --name my-nginx-container -p 8080:80
```

![포트매핑 실행명령](assets/dockermapping.png)

---

## 8. 포트 매핑 접속증거

### 8-1. 호스트 포트 접속
```bash
curl http://localhost:8080
```

![호스트 포트 접속](assets/dockercurl.png)

---

## 9. Docker 볼륨 영속성 검증

### 9-1. 볼륨 생성 및 마운트
```bash
docker volume create my-nginx-volume
docker run -d --name my-nginx-container -p 8082:80 -v my-nginx-volume:/usr/share/nginx/html nginx:alpine
```

![볼륨생성과 볼륨마운트](assets/dockervolumemake.png)

### 9-2. 컨테이너 삭제 후 데이터 유지 확인
```bash
docker stop my-nginx-container
docker rm my-nginx-container
docker volume ls
docker run -d --name my-nginx-new -p 8082:80 -v my-nginx-volume:/usr/share/nginx/html nginx:alpine
docker exec my-nginx-new cat /usr/share/nginx/html/index.html
```

- `docker stop my-nginx-container` : 컨테이너 중지
- `docker rm my-nginx-container` : 컨테이너 삭제
- `docker volume ls` : 볼륨 확인
- `docker run -d --name my-nginx-new -p 8082:80 -v my-nginx-volume:/usr/share/nginx/html nginx:alpine` : 같은 볼륨으로 새 컨테이너 생성
- `docker exec my-nginx-new cat /usr/share/nginx/html/index.html` : 파일이 그대로 있는지 확인

![데이터 유지 실행결과](assets/dockervolume.png)

---

## 10. Git 설정 및 GitHub 연동

```bash
git config --global user.name
git config --global user.email
git config --global init.defaultBranch main
git add .
git commit -m "commit message"
git push
```

![git 연동 확인](assets/gitlist.png)
