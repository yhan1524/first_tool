# Dev Workstation Mission

Docker, terminal, and Git practice project using **NGINX** and a static HTML page.

## 1. Project Overview
This project demonstrates the following:
- Build a Docker image with a `Dockerfile`
- Run a container from the built image
- Map host port to container port
- Serve a custom `index.html` page with NGINX
- Practice bind mount and Docker volume usage
- Prepare evidence files for submission

## 2. Project Structure
```text
dev-workstation-mission/
├─ Dockerfile
├─ app/
│  └─ index.html
├─ commands.md
├─ README.md
├─ README_snippet.md
└─ CAPTURE_CHECKLIST.md
```

## 3. Dockerfile
```dockerfile
FROM nginx:alpine
COPY app/index.html /usr/share/nginx/html/index.html
EXPOSE 80
```

## 4. Build and Run

### Build image
```bash
docker build -t my-nginx-app .
```

### Run container
```bash
docker run -d --name my-nginx-container -p 8080:80 my-nginx-app
```

### Verify
```bash
docker ps
```

Then open:
- http://localhost:8080

## 5. Bind Mount Example
Use local file directly inside a container:
```bash
docker run -d --name my-nginx-bind -p 8081:80   -v ${PWD}/app/index.html:/usr/share/nginx/html/index.html:ro   nginx:alpine
```

## 6. Volume Example
Create and use a Docker volume:
```bash
docker volume create my-nginx-data

docker run -d --name my-nginx-volume -p 8082:80   -v my-nginx-data:/usr/share/nginx/html   nginx:alpine
```

## 7. Useful Commands
```bash
docker images
docker ps -a
docker volume ls
docker stop my-nginx-container
docker rm my-nginx-container
```

## 8. Submission Tips
- Include terminal screenshots for build and run commands
- Include browser screenshot showing the page result
- Include `docker ps` and `docker images` output
- Include bind mount / volume proof if required by the assignment
- Use `CAPTURE_CHECKLIST.md` before final submission

## 9. GitHub Upload Guide
```bash
git init
git add .
git commit -m "Add dev workstation mission files"
git branch -M main
git remote add origin <YOUR_REPOSITORY_URL>
git push -u origin main
```

Replace `<YOUR_REPOSITORY_URL>` with your actual repository URL.

## 10. Expected Result
A working NGINX container should serve the custom HTML page through:
- `http://localhost:8080`
