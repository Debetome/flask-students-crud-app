FROM python:3.11-alpine

WORKDIR /app

COPY . ./

RUN pip3 install -r requirements.txt

ENV HOST='0.0.0.0'
ENV PORT=8000
ENV PRODUCTION=1

CMD ["python3", "app.py"]