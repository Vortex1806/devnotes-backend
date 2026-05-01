FROM python:3-alpine

WORKDIR /app

COPY app/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x app/app.py

CMD ["python", "app/app.py"]
