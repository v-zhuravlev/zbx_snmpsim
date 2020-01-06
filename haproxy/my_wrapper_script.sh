#!/bin/bash

# turn on bash's job control
set -m

# Start the primary process and put it in the background
#./my_main_process &
haproxy -f /usr/local/etc/haproxy/haproxy.cfg &

# Start the helper process
#./my_helper_process
service zabbix-agent start
#/usr/sbin/zabbix_agentd -c /etc/zabbix/zabbix_agentd.conf

# the my_helper_process might need to know how to wait on the
# primary process to start before it does its work and returns


# now we bring the primary process back into the foreground
# and leave it there
fg %1
