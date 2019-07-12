def create_host(zapi):

    params = {
        "host": "postgres-slave",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "zabbix-agent",
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
            zapi.template.get(filter={"name": "Template DB PgSQL"}, output=['id'])[0]
        ],
        "macros": [
            {
                "macro": "{$PG_HOST}",
                "value": "postgres-slave"
            }
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)