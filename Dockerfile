FROM python:3.8.20-alpine 

WORKDIR /app

COPY main.py /app/main.py
COPY templates /app/templates
COPY requirements.txt /app/requirements.txt

VOLUME [ "/app/data" ]

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]