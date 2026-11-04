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
해당 프로젝트는 나누어 저장해야 할 자료가 적기 때문에 디렉토리의 구성을 간결하게 진행하였다
- 'assets/' 출력할 실행 증거 이미지모음
- 'app/' index 파일

디렉토리 설계기준은 대략 아래와 같다

- 기능별 분리: 파일을 용도에 따라 나누기
- 재사용성 고려: 공통 자료는 따로 모아주기
- 유지보수성: 찾기 쉽고 수정하기 쉽게 
- 확장성 확보: 파일이 늘어나도 구조가 무너지지 않도록

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
- windows 에서는 확장자(.txt)로 파일 종류를 구분
- rinux 에서는 내용이나 실행방식, 이름으로 구분해 확장자 없이 사용가능

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

### 5-1-1. 권한 확인(windows)
```powershell
icacls
```

![권한 확인](assets/chmod.png)

### 5-1-2. 권한 변경
```powershell
/grant:r
```

![권한 변경](assets/grant1.png)
![권한 변경](assets/grant2.png)

---
### 5-1-1. 권한 확인(unix)
```
chmod 755 example.sh    //파일생성
ls -l example.sh        //권한확인
```

![권한 확인](assets/unixls.png)
- 파일종류(-)       // (-) 일반파일 (d) 디렉터리
- 소유자권한(rwx)   // 읽기·쓰기·실행
- 그룹권한(xr)      // 실행·읽기 
- 기타사용자권한(x)  // 실행

### 5-1-2. 권한 변경
```powershell
chmod [권한] [파일명]
```

![권한 변경](assets/unixchmod.png)

- [권한 상세설명](#14-rwx-permission-mapping)
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

### 6-3. 빌드 실행
```bash
docker build -t nginx-alpine .
```

![빌드실행](assets/dockerbild.png)

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
### Git 설정
```bash
git config --global user.name
git config --global user.email
git config --global init.defaultBranch main
```
### GitHub 원격 저장소 연결
```
git remote add origin https://github.com/username/repository.git
git remote -v
```
### 커밋 및 푸시
```
git add .
git commit -m "commit message"
git push -u origin main
```

![git 연동 확인](assets/gitlist.png)

## 11. 이미지와 컨테이너

### 이미지와 컨테이너의 차이
- **이미지(Image)**: 컨테이너를 만들기 위한 실행 템플릿
- **컨테이너(Container)**: 이미지를 실행한 실제 동작 인스턴스
- 이미지는 저장된 상태이고, 컨테이너는 실행 중인 상태

### 빌드 → 실행 → 변경 흐름
1. `Dockerfile` 컨테이너를 작성한다.
2. `docker build`로 이미지를 생성한다.
3. `docker run`으로 컨테이너를 실행한다.
4. 컨테이너 내부에서 파일을 변경하면, 그 변경은 기본적으로 해당 컨테이너에만 반영된다.<br>

생성이미지 (app.txt)
```
처음 내용입니다.
```

```
docker run -it --name test1 myapp:1.0
echo "컨테이너에서 바꾼 내용입니다." > /app/app.txt
cat /app/app.txt

```
출력결과
```
컨테이너에서 바꾼 내용입니다.
```
```
docker run -it --name test2 myapp:1.0
cat /app/app.txt

```
출력결과
```
처음 내용입니다.
```


5. 변경 내용을 보존하려면 다시 이미지로 빌드하거나 볼륨을 사용해야 한다.<br>

이미지로 빌드
```
docker build -t myapp:2.0 .
```
볼륨 사용
```
docker run -v $(pwd):/app myapp
```


### 이미지, 컨테이너, 볼륨 비교

| 요소 | 설명 | 특징 | 예시 |
|---|---|---|---|
| Docker Image | 앱 실행에 필요한 파일, 설정, 라이브러리를 담은 것 | 읽기 전용 | `myapp:latest` |
| Docker Container | 이미지를 실행해서 만든 실제 동작 환경 | 실행 중이며 변경 가능 | `docker run myapp` |
| Docker Volume | 데이터를 따로 저장하는 공간 | 컨테이너 삭제 후에도 유지됨 | DB 파일, 로그, 업로드 파일 |


---

## 12. Network Namespace and Port Forwarding

### 네트워크 네임스페이스
네트워크를 서로 분리된 공간으로 만드는 기능
네트워크 네임스페이스는 충돌 방지, 보안, 독립성 확보를 위해 필요하다
컨테이너는 호스트와 분리된 네트워크 네임스페이스를 사용하므로, 기본적으로 외부에서 바로 접근할 수 없다

### 호스트모드
- 컨테이너가 호스트의 네트워크를 그대로 공유한다
### 브리지모드
- 컨테이너가 호스트와 분리된 별도 네트워크를 사용한다
- 외부 접근엔 포트 포워딩이 필요

### 포트 포워딩
호스트의 포트와 컨테이너의 포트를 연결하여 외부 요청을 컨테이너 서비스로 전달하는 접속방법

### 예시 `-p`
```bash
docker run -p 8080:80 myimage
```

- 호스트의 `8080` 포트
- 컨테이너의 `80` 포트
- **내 PC의 8080번 포트로 들어온 요청을 컨테이너의 80번 포트로 보냄**
---

## 13. Absolute vs Relative Path

### 절대경로와 상대경로
- **절대경로**: 루트(`/`)부터 시작하는 고정 경로
- **상대경로**: 현재 작업 위치를 기준으로 하는 경로

### 사용 기준
- 정확한 위치를 항상 유지해야 하면 → **절대경로**
- 현재 위치 기준으로 유연하게 이동할 때 → **상대경로**
- 자동화 스크립트에서는 경로 해석 오류를 줄이기 위해 절대경로를 우선 사용한다
- 개발 중 빠르게 이동하며 작업할 때는 상대경로가 편리하다.

### 경로 예시
```bash
/home/user/project/data.txt   # 절대경로
./data.txt                    # 상대경로
../data.txt                   # 상대경로
```
### 현재 작업 디렉터리의 절대경로(${PWD})
```
echo "hello" > "${PWD}/result.txt"    //Bash
"hello" | Out-File "$($PWD.Path)\result.txt"   //powershell
---

## 14. rwx Permission Mapping

### 권한 비트 의미
- `r` = read(읽기)
- `w` = write(쓰기)
- `x` = execute(실행)

### 숫자 매핑
| 권한 | 값 |
|---|---:|
| r | 4 |
| w | 2 |
| x | 1 |

### 조합 예시
| 권한 | 숫자 | 의미 |
|---|---:|---|
| rwx | 7 | 읽기 / 쓰기 / 실행 |
| rw- | 6 | 읽기 / 쓰기 |
| r-x | 5 | 읽기 / 실행 |
| r-- | 4 | 읽기 |
| --- | 0 | 권한 없음 |

### `755` 예시
- 소유자: `7` = `rwx`
- 그룹: `5` = `r-x`
- 기타: `5` = `r-x`

```bash
chmod 755 script.sh
ls -l script.sh
```
자주 쓰는 권한
- 755: 실행파일, 스크립트, 디렉터리에 자주 사용
- 644: 일반문서, 설정 파일에 자주 사용

---

## 15. Port Conflict Troubleshooting
```
Error response from daemon: driver failed programming external connectivity on endpoint second-nginx (...): Bind for 0.0.0.0:8080 failed: port is already allocated
```
### 포트 충돌 진단 순서
1. 포트가 사용 중인지 확인한다.
2. 해당 포트를 점유한 프로세스를 찾는다.
3. 필요하면 프로세스를 종료한다.
4. 다시 실행해서 문제가 해결되었는지 확인한다.

### 포트 사용 확인
```bash
lsof -i :8080
```
Windows 환경에서 확인 
```
netstat -ano | findstr :8080    
```
### 예시 출력
```text
TCP    10.70.102.112:55552    10.60.30.12:8080       ESTABLISHED     1234
```
- PID : 1234
### 해당 PID가 어떤 프로세스인지 확인
```
ps -p 1234 -f
```
Windows 환경에서 확인 
```
tasklist /FI "PID eq 1234"
```


### 프로세스 종료
```bash
kill 1234
```

강제 종료가 필요할 경우:
```bash
kill -9 1234
```
Windows 환경에서 종료(/F: 강제종료)
```
taskkill /PID 1234 /F
```

### 재확인
```bash
lsof -i :8080
```
Windows 환경에서 확인 
```
netstat -ano | findstr :8080    
```

### 정리
- 확인 → 식별 → 종료 → 재확인 순서로 기록한다.
- 실제 실행 로그를 함께 첨부하면 신뢰도가 높아진다.

---

## 16. Bind Mount vs Docker Volume

### 비교 표
| 항목 | 바인드 마운트 | Docker 볼륨 |
|---|---|---|
| 연결 방식 | 호스트 경로를 직접 연결 | Docker가 관리하는 저장소 사용 |
| 장점 | 개발 중 즉시 반영됨 | 관리가 편하고 이식성이 좋음 |
| 단점 | 호스트 경로에 의존함 | 호스트에서 직접 보기 어려울 수 있음 |
| 적합한 경우 | 개발 / 디버깅 | 운영 / 데이터 보존 |

### 간단 설명
- **바인드 마운트**는 로컬 파일을 컨테이너에 바로 연결하는 방식이다.
- **Docker 볼륨**은 Docker가 데이터를 관리하므로 운영 환경에서 사용하기 좋다.

### 예시
```bash
# 바인드 마운트
docker run -v $(pwd)/data:/app/data myimage

# Docker 볼륨
docker run -v myvolume:/app/data myimage
```
- 개발환경: <br>
바인드 마운트 우선, 내 PC 소스코드를 컨테이너에 바로 반영하기 위함<br>
볼륨은 컨테이너를 지워도 데이터가 남아야 할 때 사용함<br>

- 운영환경: <br>
볼륨 우선, 호스트의 의존성을 줄이고 데이터의 안정적 저장·백업·이관이 쉬움 <br>
호스트의 특정 경로를 직접 써야할 때 바인드 마운트를 사용할 수 있음

---

## 17. Troubleshooting Case

### 17-1. 컨테이너 포트 접속 실패

- **문제 상황**: 브라우저에서 `http://localhost:8080` 접속이 되지 않는다.
- **가설**: 호스트의 `8080` 포트가 이미 사용 중이라 컨테이너가 포트 바인딩에 실패했을 것이다.
- **검증 명령어**:

```bash
lsof -i :8080
```

- **확인 포인트**: `8080` 포트를 사용 중인 프로세스가 있는지 확인한다.

---

### 17-2. 컨테이너가 실행되지 않음

- **문제 상황**: 컨테이너를 실행했지만 바로 종료된다.
- **가설**: 실행 명령어나 설정 오류로 인해 컨테이너가 정상적으로 시작되지 않았을 것이다.
- **검증 명령어**:

```bash
docker ps -a
docker logs <container_id>
```

- **확인 포인트**: 종료 상태인지, 로그에 에러 메시지가 있는지 확인한다.

---

### 17-3. 웹 페이지가 열리지 않음

- **문제 상황**: 컨테이너는 실행 중이지만 외부에서 접속이 되지 않는다.
- **가설**: 애플리케이션이 `0.0.0.0`이 아니라 `localhost`에만 바인딩되어 있을 것이다.
- **검증 명령어**:

```bash
docker exec -it <container_id> netstat -tuln
```

또는

```bash
docker logs <container_id>
```

- **확인 포인트**: 서버가 어떤 주소로 바인딩되어 있는지 확인한다.

---

### 17-4. 데이터베이스 연결 실패

- **문제 상황**: 애플리케이션이 DB에 연결되지 않는다.
- **가설**: DB 호스트명 또는 포트 설정이 잘못되어 연결에 실패했을 것이다.
- **검증 명령어**:

```bash
docker exec -it <container_id> ping <db_host>
```

또는

```bash
docker exec -it <container_id> nc -zv <db_host> 5432
```

- **확인 포인트**: DB 서버에 네트워크 접근이 가능한지 확인한다.

---

### 17-5. 빌드는 성공했지만 실행 시 에러 발생

- **문제 상황**: 이미지는 잘 빌드되었지만 실행하면 오류가 난다.
- **가설**: 환경변수나 설정 파일이 누락되어 실행에 필요한 값이 없을 것이다.
- **검증 명령어**:

```bash
docker inspect <container_id>
docker logs <container_id>
```

- **확인 포인트**: 필요한 환경변수가 설정되어 있는지, 로그에 설정 누락 메시지가 있는지 확인한다.
