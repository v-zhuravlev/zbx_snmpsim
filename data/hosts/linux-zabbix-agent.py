def create_host(zapi):

    params = {
        "host": "linux-zabbix-agent",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "linux-zabbix-agent",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        "tags": [
            {
                "tag": "Linux",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template OS Linux"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)