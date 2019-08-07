# Zabbix MySQL lab

This is a simple lab to test Zabbix MySQL templates in standalone and master + slave configurations.

To use it, run:  

```
cd zbx_snmpsim
docker-compose -f .docker-compose.zabbix.yml -f .docker-compose.mysql.yml up
```

Wait for Zabbix to startup, then import `Template DB MySQLv8.xml`.

In another shell:  

```
cd zbx_snmpsim
python .\bin\create_hosts.py  --filter mysql data
No snmpsim hosts found in the directory 'data' with filter: mysql
Going to create host using config ".\hosts\mysql-slave.py"
Going to create host using config ".\hosts\mysql.py"
```

In Zabbix, observe MySQL hosts created monitoring MySQL cluster.
