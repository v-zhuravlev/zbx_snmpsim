def create_host(zapi):

    params = {
        "host": "linux-node_exporter",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "linux-node_exporter",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        "tags": [
            {
                "tag": "node_exporter",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template OS Linux by Prom"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)