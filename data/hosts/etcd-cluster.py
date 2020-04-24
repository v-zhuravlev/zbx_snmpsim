def create_host(zapi):

    etcd1 = {
        "host": "etcd1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "etcd1",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Templates/Applications"}, output=['id']),
        "tags": [
            {
                "tag": "etcd docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template App Etcd by HTTP"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }

    etcd2 = {
        "host": "etcd2",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "etcd2",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Templates/Applications"}, output=['id']),
        "tags": [
            {
                "tag": "etcd docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template App Etcd by HTTP"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }

    etcd3 = {
        "host": "etcd3",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "etcd3",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Templates/Applications"}, output=['id']),
        "tags": [
            {
                "tag": "etcd docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template App Etcd by HTTP"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }
    zapi.host.create(etcd1)
    zapi.host.create(etcd2)
    zapi.host.create(etcd3)