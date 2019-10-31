def create_host(zapi):

    params = {
        "host": "redis-master",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "redis-master",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Templates/Databases"}, output=['id']),
        "tags": [
            {
                "tag": "Redis docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template DB Redis"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)