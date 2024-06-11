FROM python:3.8-slim

WORKDIR /app

COPY app.py requirements.txt /app/
COPY model/ /app/model/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
