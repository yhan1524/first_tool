# CAPTURE_CHECKLIST.md

제출 전에 아래 항목을 캡처했는지 확인하세요.

## 필수 캡처
- [ ] 프로젝트 폴더 구조가 보이는 화면
- [ ] `Dockerfile` 내용이 보이는 화면
- [ ] `index.html` 내용이 보이는 화면
- [ ] `docker build -t my-nginx-app .` 실행 결과
- [ ] `docker run -d --name my-nginx-container -p 8080:80 my-nginx-app` 실행 결과
- [ ] `docker ps` 실행 결과
- [ ] 브라우저에서 `http://localhost:8080` 접속 결과
- [ ] `docker images` 실행 결과

## 요구사항에 따라 추가하면 좋은 캡처
- [ ] bind mount 실행 명령 및 결과
- [ ] volume 생성 명령 및 결과
- [ ] `docker volume ls` 실행 결과
- [ ] GitHub 저장소 업로드 완료 화면
- [ ] 커밋 내역 화면

## 제출 전 최종 점검
- [ ] 파일명 오탈자 없음
- [ ] README.md 포함 여부 확인
- [ ] 명령어가 실제로 동작하는지 재확인
- [ ] 캡처 이미지가 흐리지 않은지 확인
- [ ] 압축 파일 안에 필요한 파일이 모두 포함되어 있는지 확인
