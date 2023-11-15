FROM python:3.11.4-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]