def create_host(zapi):

    params = {
        "host": "docker-engine",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "docker-engine",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        "tags": [
            {
                "tag": "Docker engine docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template App Docker"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)