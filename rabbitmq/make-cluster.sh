#!/bin/bash

hostname=`hostname`
RABBITMQ_NODENAME=${RABBITMQ_NODENAME:-rabbit}

if [ -z "$JOIN_CLUSTER" -o "$JOIN_CLUSTER" = "$hostname" ]; then
    rabbitmq-server
else
    rabbitmq-server -detached
    rabbitmqctl stop_app
    rabbitmqctl join_cluster --ram $RABBITMQ_NODENAME@$JOIN_CLUSTER
    rabbitmqctl start_app

    for cmd in ${!ZBX_CMD*}; do 
        eval ${!cmd} 
    done

    tail -f /var/log/rabbitmq/log/*
fi
