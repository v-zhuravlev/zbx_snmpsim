#!/bin/bash
set -e

if [ $REPLICATION_ROLE = "master" ]; then
    psql -U postgres -c "CREATE ROLE $REPLICATION_USER WITH REPLICATION PASSWORD '$REPLICATION_PASSWORD' LOGIN"
    psql -U postgres -c "CREATE ROLE $MONITORING_USER WITH LOGIN PASSWORD '$MONITORING_PASS' NOSUPERUSER NOINHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;"

elif [ $REPLICATION_ROLE = "slave" ]; then
    pg_ctl -D "$PGDATA" -m fast -w stop
    rm -r "$PGDATA"/*

    pg_basebackup \
         --write-recovery-conf \
         --pgdata="$PGDATA" \
         --xlog-method=fetch \
         --username=$REPLICATION_USER \
         --host=$POSTGRES_MASTER_SERVICE_HOST \
         --port=$POSTGRES_MASTER_SERVICE_PORT \
         --progress \
         --verbose

    pg_ctl -D "$PGDATA" \
         -o "-c listen_addresses=''" \
         -w start
fi

echo [*] $REPLICATION_ROLE instance configured!
