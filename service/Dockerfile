FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt ./ 
COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]
