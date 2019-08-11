# Zabbix PostgreSQL

Simple PostgreSQL cluster simulator for testing metrics collection with Zabbix

## How to run

- Go to the [zbx_snmpsim](https://github.com/v-zhuravlev/zbx_snmpsim) root directory

- Build images of the latest versions (strongly recommended):

```bash
docker-compose -f docker-compose.postgresql.yml build --pull
```

- Run the PostgreSQL cluster:

```bash
docker-compose -f docker-compose.postgresql.yml up -d
```

- Run a complete Zabbix installation:

```bash
docker-compose -f docker-compose.zabbix.yml up -d
```

- Log in to the Zabbix frontend and import the template `template_db_postgresql.xml`.

- Run the command to automatically add hosts to Zabbix:

```bash
python ./bin/create_hosts.py  --filter postgres data
```

Congratulations! Now you can test the PostgreSQL cluster monitoring in Zabbix.
