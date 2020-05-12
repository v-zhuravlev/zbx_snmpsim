# Zabbix Etcd

Simple Etcd simulator for testing metrics collection with Zabbix

## How to run

Use docker-compose.etcd.yml  for running cluster etcd v3.4 with API v3

Use docker-compose.etcd2.yml  for running cluster etcd v3.2 with API v2

Both etcd clusters can work simultaneously.


- Go to the [zbx_snmpsim](https://github.com/v-zhuravlev/zbx_snmpsim) root directory

- Build images of the latest versions (strongly recommended):

```bash
docker-compose -f docker-compose.etcd.yml build --pull
```

- Run Nginx:

```bash
docker-compose -f docker-compose.etcd.yml up -d
```

- Run a complete Zabbix installation:

```bash
docker-compose -f docker-compose.zabbix.yml up -d
```

- Log in to the Zabbix frontend and import Etcd templates `template_app_etcd_http.xml`.

- Run the command to automatically add hosts to Zabbix:

```bash
python ./bin/create_hosts.py  --filter etcd data
```

Congratulations! Now you can test the Etcd monitoring in Zabbix.
