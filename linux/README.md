# Zabbix Linux

Test Linux metrics collection using Zabbix agent, `node_exporeter` and `snmpd`

## How to run

- Go to the [zbx_snmpsim](https://github.com/v-zhuravlev/zbx_snmpsim) root directory

- Build images of the latest versions (strongly recommended):

```bash
docker-compose -f docker-compose.linux.yml build --pull
```

- Run all agents:

```bash
docker-compose -f docker-compose.zabbix.yml up -d
```

- Run a complete Zabbix installation:

```bash
docker-compose -f docker-compose.zabbix.yml up -d
```

- Run the command to automatically add hosts to Zabbix:

```bash
python ./bin/create_hosts.py  --filter linux data
```

Congratulations! Now you can test the Linux templates in Zabbix.
