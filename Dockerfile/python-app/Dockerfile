FROM python:3.12

WORKDIR /app

ENV APP_ENV=production

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
