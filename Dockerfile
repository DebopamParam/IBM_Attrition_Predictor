FROM python:3.12.1-slim-bullseye

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt update -y && apt install awscli -y

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

EXPOSE 8080

CMD ["fastapi", "run", "backend/main.py", "--proxy-headers", "--port", "8080"]
