def create_host(zapi):

    params = {
        "host": "postgres-master",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "zabbix-agent-postgresql",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        "tags": [
            {
                "tag": "PostgreSQL docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template DB PostgreSQL"}, output=['id'])[0]
        ],
        "macros": [
            {
                "macro": "{$PG.HOST}",
                "value": "postgres-master"
            }
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)