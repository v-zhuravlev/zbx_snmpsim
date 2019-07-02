def create_host(zapi):

    params = {
        "host": "postgres-zabbix-agent",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "postgres-zabbix-agent",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        # "tags": [
        #     {
        #         "tag": "PostgreSQL docker test",
        #         "value": ""
        #     }
        # ],
        "templates": [
            zapi.template.get(filter={"name": "Template Module ICMP Ping"}, output=['id'])[0]
        ],
        "macros": [
            {
                "macro": "{$SOME_POSTGRES_MACRO}",
                "value": "8080"
            }
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)