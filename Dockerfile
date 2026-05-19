FROM tiangolo/uwsgi-nginx-flask:python3.12

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY subject3_2/ /app/

ENV STATIC_PATH=/app/static
EXPOSE 80