# Zabbix Nginx

Simple Nginx simulator for testing metrics collection with Zabbix

## How to run

- Go to the [zbx_snmpsim](https://github.com/v-zhuravlev/zbx_snmpsim) root directory

- Build images of the latest versions (strongly recommended):

```bash
docker-compose -f docker-compose.nginx.yml build --pull
```

- Run Nginx:

```bash
docker-compose -f docker-compose.nginx.yml up -d
```

- Run a complete Zabbix installation:

```bash
docker-compose -f docker-compose.zabbix.yml up -d
```

- Log in to the Zabbix frontend and import Nginx templates `template_app_nginx*.xml`.

- Run the command to automatically add hosts to Zabbix:

```bash
python ./bin/create_hosts.py  --filter nginx data
```

Congratulations! Now you can test the Nginx monitoring in Zabbix.
