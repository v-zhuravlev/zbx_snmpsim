#!/bin/bash

echo 'create database test_db_zabbix' | curl 'http://ch1:8123/' --data-binary @-
echo 'create database test_db_zabbix' | curl 'http://ch2:8123/' --data-binary @-
echo 'create database test_db_zabbix' | curl 'http://ch3:8123/' --data-binary @-
echo 'create database test_db_zabbix' | curl 'http://ch4:8123/' --data-binary @-

echo "CREATE TABLE IF NOT EXISTS test_db_zabbix.events_shard ON CLUSTER ua_cluster ( \
  event_date           Date DEFAULT toDate(now()),
  company_id           UInt32, \
  product_id           UInt32 \
) ENGINE=ReplicatedMergeTree( \
    '/clickhouse/tables/{shard}/events_shard', '{replica}', event_date, (company_id), 8192 );"  | curl 'http://ch1:8123/' --data-binary @-

echo "CREATE TABLE IF NOT EXISTS test_db_zabbix.events_dist \
ON CLUSTER ua_cluster AS test_db_zabbix.events_shard \
ENGINE = Distributed(ua_cluster, test_db_zabbix, events_shard, rand());"  | curl 'http://ch1:8123/' --data-binary @-


