FROM ubuntu:24.04

RUN apt update
RUN apt install -y python3-pip python-is-python3 build-essential git 
RUN apt install -y vim debhelper
RUN apt install -y iproute2
RUN python --version | grep 'Python 3.12'

COPY ./debian/roo-vectordb_0.1-0_amd64.deb .
RUN apt install -y ./roo-vectordb_0.1-0_amd64.deb

USER postgres
RUN service postgresql start && \
    psql -c "CREATE USER ann WITH ENCRYPTED PASSWORD 'ann'" && \
    psql -c "CREATE DATABASE ann" && \
    psql -c "ALTER USER ann WITH SUPERUSER" && \
    psql -c "GRANT ALL PRIVILEGES ON DATABASE ann TO ann" && \
    psql -d ann -c "GRANT ALL ON SCHEMA public TO ann" && \
    psql -c "ALTER USER ann SET maintenance_work_mem = '2GB'" && \
    psql -c "ALTER USER ann SET max_parallel_workers = 8" && \
    psql -c "ALTER USER ann SET max_parallel_maintenance_workers = 7" && \
    psql -c "ALTER SYSTEM SET shared_buffers = '512MB'"
RUN service postgresql start && \
    psql -d ann -c "CREATE EXTENSION roovectorcpu"

USER root
COPY entrypoint.sh ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
