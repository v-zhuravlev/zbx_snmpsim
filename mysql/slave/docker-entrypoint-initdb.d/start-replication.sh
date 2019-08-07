#!/bin/bash

host1=mysql-server-master
host2=mysql-server-slave

for i in {30..0}; do
		if echo 'SELECT 1' | mysql -uroot -p$MYSQL_ROOT_PASSWORD &> /dev/null; then
				break
		fi
		echo 'Local MySQL in progress...'
		sleep 1
done

for i in {30..0}; do
		if echo 'SELECT 1' | mysql -h$host1 -uroot -p$MYSQL_ROOT_PASSWORD &> /dev/null; then
				break
		fi
		echo 'Remote MySQL in progress...'
		sleep 1
done

if [ -z "$(mysql -uroot -p$MYSQL_ROOT_PASSWORD -e 'show slave status\G' 2>/dev/null)" ]; then
    echo "Start replication on the second server..."
    master=$(mysql -h$host1 -uroot -p$MYSQL_ROOT_PASSWORD -e 'show master status\G' 2>/dev/null)
    master_file=$(echo "$master" | awk /File:/{'print $2'})
    master_pos=$(echo "$master" | awk /Position:/{'print $2'})
    mysql -uroot -p$MYSQL_ROOT_PASSWORD -e 'stop slave' 2>/dev/null
    mysql -uroot -p$MYSQL_ROOT_PASSWORD -e "CHANGE MASTER TO MASTER_HOST='$host1', MASTER_USER='root', MASTER_PASSWORD='$MYSQL_ROOT_PASSWORD', MASTER_LOG_FILE='$master_file', MASTER_LOG_POS=$master_pos" 2>/dev/null
    mysql -uroot -p$MYSQL_ROOT_PASSWORD -e 'start slave' 2>/dev/null
else
	echo "The replication started on the second server."
fi

# master-master replication block
if [ -z "$(mysql -h$host1 -uroot -p$MYSQL_ROOT_PASSWORD -e 'show slave status\G' 2>/dev/null)" ]; then
    echo "Start replication on the first server..."
    master=$(mysql -uroot -p$MYSQL_ROOT_PASSWORD -e 'show master status\G' 2>/dev/null)
    master_file=$(echo "$master" | awk /File:/{'print $2'})
    master_pos=$(echo "$master" | awk /Position:/{'print $2'})
    mysql -h$host1 -uroot -p$MYSQL_ROOT_PASSWORD -e 'stop slave' 2>/dev/null
    mysql -h$host1 -uroot -p$MYSQL_ROOT_PASSWORD -e "CHANGE MASTER TO MASTER_HOST='$host2', MASTER_USER='root', MASTER_PASSWORD='$MYSQL_ROOT_PASSWORD', MASTER_LOG_FILE='$master_file', MASTER_LOG_POS=$master_pos" 2>/dev/null
    mysql -h$host1 -uroot -p$MYSQL_ROOT_PASSWORD -e 'start slave' 2>/dev/null
else
	echo "The replication started on the first server."
fi
