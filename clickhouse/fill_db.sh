#!/bin/bash

echo "INSERT INTO test_db_zabbix.events_dist (company_id, product_id) VALUES (1, 111), (1, 122), (1, 133);" | curl 'http://ch1t:8123/' --data-binary @-
echo "INSERT INTO test_db_zabbix.events_dist (company_id, product_id) VALUES (2, 112), (2, 122), (2, 132);" | curl 'http://ch2:8123/' --data-binary @-
echo "INSERT INTO test_db_zabbix.events_dist (company_id, product_id) VALUES (3, 1111), (3, 1112), (3, 1113);" | curl 'http://ch3:8123/' --data-binary @-
echo "INSERT INTO test_db_zabbix.events_dist (company_id, product_id) VALUES (4, 11), (4, 12), (4, 13);" | curl 'http://ch4:8123/' --data-binary @-
