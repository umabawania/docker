FROM maven:3.9-eclipse-temurin-21

WORKDIR /app

COPY . .

RUN mvn package

EXPOSE 5000

CMD ["java", "-cp", "target/classes", "Main"]
