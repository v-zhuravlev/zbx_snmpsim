def create_host(zapi):

    params = {
        "host": "apache-agent",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "apache",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        "tags": [
            {
                "tag": "Apache docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template App Apache by Zabbix agent"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)