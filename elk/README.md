# Zabbix Elasticsearch cluster

Simple ES v.6|7 cluster simulator for testing metrics collection with Zabbix
Default login: elastic, default password: changeme.
Set the desired version number in the file .env. For example:
ELK_VERSION=6.7.0

## How to run

- Go to the [zbx_snmpsim](https://github.com/v-zhuravlev/zbx_snmpsim) root directory

- Build images of the latest versions (strongly recommended):

```bash
docker-compose -f docker-compose.es6.yml build --pull
or
docker-compose -f docker-compose.es7.yml build --pull
```

- Run ES:

```bash
docker-compose -f docker-compose.es6.yml up -d
or
docker-compose -f docker-compose.es7.yml up -d
```

- Run a complete Zabbix installation:

```bash
docker-compose -f docker-compose.zabbix.yml up -d
```

- Log in to the Zabbix frontend and import ES template `template_app_elasticsearch_http.xml`.

- Run the command to automatically add hosts to Zabbix:

```bash
python ./bin/create_hosts.py  --filter nginx data
```

Congratulations! Now you can test the ES monitoring in Zabbix.

If you encounter any problems starting the cluster, please see this page https://www.elastic.co/guide/en/elasticsearch/reference/6.5/docker.html
or this one https://www.elastic.co/guide/en/elasticsearch/reference/7.0/docker.html .
