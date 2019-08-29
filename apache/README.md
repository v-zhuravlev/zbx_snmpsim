# Zabbix Apache

Simple Apache simulator for testing metrics collection with Zabbix

## How to run

- Go to the [zbx_snmpsim](https://github.com/v-zhuravlev/zbx_snmpsim) root directory

- Build images of the latest versions (strongly recommended):

```bash
docker-compose -f docker-compose.apache.yml build --pull
```

- Run Apache server instance:

```bash
docker-compose -f docker-compose.apache.yml up -d
```

- Run a complete Zabbix installation:

```bash
docker-compose -f docker-compose.zabbix.yml up -d
```

- Log in to the Zabbix frontend and import templates `template_app_apache*.xml`.

- Run the command to automatically add hosts to Zabbix:

```bash
python ./bin/create_hosts.py  --filter apache data
```

Congratulations! Now you can test the Apache monitoring in Zabbix.