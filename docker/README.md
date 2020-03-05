# Zabbix Docker engine monitoring

Simple Docker engine simulator for testing metrics collection with Zabbix

## How to run

- Go to the [zbx_snmpsim](https://github.com/v-zhuravlev/zbx_snmpsim/tree/docker) root directory

- Build images of the latest versions (strongly recommended):

```bash
docker-compose -f docker-compose.docker.yml build --pull
```

- Run Zabbix agent v2 with Docker plugin:

```bash
docker-compose -f docker-compose.docker.yml up -d
```

- Run a complete Zabbix installation:

```bash
docker-compose -f docker-compose.zabbix.yml up -d
```

- Log in to the Zabbix frontend and import templates `template_app_docker.xml`.

- Run the command to automatically add hosts to Zabbix:

```bash
python bin/create_hosts.py data --filter docker
```

Congratulations! Now you can test the Docker engine monitoring in Zabbix.
