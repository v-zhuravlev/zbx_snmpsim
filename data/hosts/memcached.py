def create_host(zapi):

    params = {
        "host": "memcached-host",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "memcached-host",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Templates/Applications"}, output=['id']),
        "tags": [
            {
                "tag": "memcached docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template App Memcached"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)