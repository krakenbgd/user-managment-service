FROM python:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /

ADD requirements.txt run_server.sh /
RUN pip install --no-cache-dir -r requirements.txt

ADD app /app

ENV PG_DB_HOST ${PG_DB_HOST}
ENV PG_DB_USERNAME ${PG_DB_USERNAME}
ENV PG_DB_PASSWORD ${PG_DB_PASSWORD}
ENV PG_DB_NAME ${PG_DB_NAME}

RUN useradd -r -u 1001 -m -s /bin/false app

RUN chown -R app:root /app run_server.sh requirements.txt && \
    chmod -R g=u /app run_server.sh requirements.txt

USER app

EXPOSE 8080
