#!/bin/bash

host=mysql-server-master

for i in {30..0}; do
		if echo 'SELECT 1' | mysql -uroot -p$MYSQL_ROOT_PASSWORD &> /dev/null; then
				break
		fi
		echo 'Local MySQL in progress...'
		sleep 1
done

for i in {30..0}; do
		if echo 'SELECT 1' | mysql -h $host -uroot -p$MYSQL_ROOT_PASSWORD &> /dev/null; then
				break
		fi
		echo 'Remote MySQL in progress...'
		sleep 1
done

if [ -z "$(mysql -uroot -p$MYSQL_ROOT_PASSWORD -e 'show slave status\G' 2>/dev/null)" ]; then
    echo "Start replication..."
    master=$(mysql -h$host -uroot -p$MYSQL_ROOT_PASSWORD -e 'show master status\G' 2>/dev/null)
    master_file=$(echo "$master" | awk /File:/{'print $2'})
    master_pos=$(echo "$master" | awk /Position:/{'print $2'})
    mysql -uroot -p$MYSQL_ROOT_PASSWORD -e 'stop slave' 2>/dev/null
    mysql -uroot -p$MYSQL_ROOT_PASSWORD -e "CHANGE MASTER TO MASTER_HOST='$host', MASTER_USER='root', MASTER_PASSWORD='$MYSQL_ROOT_PASSWORD', MASTER_LOG_FILE='$master_file', MASTER_LOG_POS=$master_pos" 2>/dev/null
    mysql -uroot -p$MYSQL_ROOT_PASSWORD -e 'start slave' 2>/dev/null
else
	echo "The replication is started."
fi
