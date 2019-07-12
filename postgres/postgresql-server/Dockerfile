FROM postgres:9.6

ENV MAX_CONNECTIONS 500
ENV WAL_KEEP_SEGMENTS 256
ENV MAX_WAL_SENDERS 100

ENV REPLICATION_ROLE master
ENV REPLICATION_USER replication
ENV REPLICATION_PASSWORD ""

ENV MONITORING_USER monitor
ENV MONITORING_PASS "monitor"

ENV POSTGRES_MASTER_SERVICE_HOST localhost
ENV POSTGRES_MASTER_SERVICE_PORT 5432

COPY 10-config.sh /docker-entrypoint-initdb.d/
COPY 20-replication.sh /docker-entrypoint-initdb.d/

RUN sed -i 's/set -e/set -e -x\nPGDATA=$(eval echo "$PGDATA")/' /docker-entrypoint.sh