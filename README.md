# 🐳 Dockerfiles for Python, Java & Node.js Applications

This project demonstrates how to create **Docker images for applications written in different programming languages**.

The goal is to understand how Dockerfiles are structured and how the process changes depending on the application runtime.

## 📌 Technologies Used

- 🐳 Docker
- 🐍 Python
- ☕ Java
- 🟢 Node.js
- 📦 Maven

## 📁 Project Structure

```text
Dockerfile/
│
├── Python-app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── Java-app/
│   ├── src/
│   │   └── main/
│   │       └── java/
│   │           └── Main.java
│   ├── pom.xml
│   └── Dockerfile
│
└── Node-app/
    ├── app.js
    ├── package.json
    └── Dockerfile
```

## 🐍 Python Application

The Python application uses the official Python image as its base image.

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Build the image

```bash
docker build -t python-app ./Python-app
```

### Run the container

```bash
docker run -d -p 5000:5000 --name python-container python-app
```

## ☕ Java Application

The Java application uses **Eclipse Temurin 21** with Maven to build the application.

```dockerfile
FROM maven:3.9-eclipse-temurin-21

WORKDIR /app

COPY pom.xml .
COPY src ./src

RUN mvn package

EXPOSE 5000

CMD ["java", "-cp", "target/classes", "Main"]
```

### Build the image

```bash
docker build -t java-app ./Java-app
```

### Run the container

```bash
docker run -d -p 5000:5000 --name java-container java-app
```

## 🟢 Node.js Application

The Node.js application uses the official Node.js image.

```dockerfile
FROM node:22

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

### Build the image

```bash
docker build -t node-app ./Node-app
```

### Run the container

```bash
docker run -d -p 3000:3000 --name node-container node-app
```

## 🔄 How Docker Works in This Project

The basic process is:

```text
Application Code
       ↓
   Dockerfile
       ↓
 docker build
       ↓
  Docker Image
       ↓
  docker run
       ↓
 Docker Container
       ↓
 Running Application
```

Although the Dockerfile structure is similar for each application, the **base image, dependency installation, build process, and start command** can be different depending on the programming language.

## 🛠️ Errors I Faced

While working on this project, I also faced a few errors during testing.

### Python dependency installation error

```text
ERROR: failed to build: failed to solve:
process "/bin/sh -c pip install -r requirements.txt"
did not complete successfully: exit code: 1
```

This helped me understand the importance of checking the dependencies listed in `requirements.txt`.

### Java class not found error

```text
Error: Could not find or load main class Main
Caused by: java.lang.ClassNotFoundException: Main
```

This was related to the Java project structure and the location of the compiled `.class` file.

### Application port error

```text
curl: (7) Failed to connect to localhost port 5000
```

This helped me understand that adding `EXPOSE` to a Dockerfile does not automatically make an application listen on that port. The application itself must listen on the port, and the port must be published using `docker run -p`.

## 🎯 What I Learned

Through this project, I learned:

- How to write a basic Dockerfile
- How to choose a suitable base image
- How `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, and `CMD` work
- How to install application dependencies inside an image
- How to build Docker images
- How to run containers
- How to map container ports to host ports
- How Dockerfiles differ between programming languages
- How to troubleshoot common Docker build and runtime errors

## 🚀 Future Improvements

Some improvements I can add to this project in the future:

- Multi-stage Docker builds
- Smaller and optimized images
- Docker Compose
- Docker image security scanning with Trivy
- CI/CD pipeline using Jenkins
- Push images to AWS ECR

## 👨‍💻 Author

**Uma Sharma**

This project was created as part of my hands-on learning with Docker, containerization, and DevOps.
