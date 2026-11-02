# commands.md

## 1) Build image
```bash
docker build -t my-nginx-app .
```

## 2) Run container with port mapping
```bash
docker run -d --name my-nginx-container -p 8080:80 my-nginx-app
```

## 3) Check running container
```bash
docker ps
```

## 4) Open page in browser
- URL: http://localhost:8080

## 5) Stop and remove container
```bash
docker stop my-nginx-container
docker rm my-nginx-container
```

## 6) Bind mount example
```bash
docker run -d --name my-nginx-bind -p 8081:80   -v ${PWD}/app/index.html:/usr/share/nginx/html/index.html:ro   nginx:alpine
```

## 7) Volume example
```bash
docker volume create my-nginx-data

docker run -d --name my-nginx-volume -p 8082:80   -v my-nginx-data:/usr/share/nginx/html   nginx:alpine
```

## 8) Inspect images, containers, volumes
```bash
docker images
docker ps -a
docker volume ls
```
