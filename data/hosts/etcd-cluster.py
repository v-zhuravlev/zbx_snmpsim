def create_host(zapi):

    etcd_v34_1 = {
        "host": "etcd_v34 node 1",
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
            zapi.template.get(filter={"name": "Template App Etcd Cluster by HTTP"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }

    etcd_v34_2 = {
        "host": "etcd_v34 node 2",
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
            zapi.template.get(filter={"name": "Template App Etcd Cluster by HTTP"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }

    etcd_v34_3 = {
        "host": "etcd_v34 node 3",
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
            zapi.template.get(filter={"name": "Template App Etcd Cluster by HTTP"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }

    etcd_v32_1 = {
        "host": "etcd_v32 node 1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "etcd32_1",
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
            zapi.template.get(filter={"name": "Template App Etcd Cluster by HTTP"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }


    etcd_v32_2 = {
        "host": "etcd_v32 node 2",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "etcd32_2",
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
            zapi.template.get(filter={"name": "Template App Etcd Cluster by HTTP"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }

    etcd_v32_3 = {
        "host": "etcd_v32 node 3",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "etcd32_3",
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
            zapi.template.get(filter={"name": "Template App Etcd Cluster by HTTP"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }

    zapi.host.create(etcd_v32_1)
    zapi.host.create(etcd_v32_2)
    zapi.host.create(etcd_v32_3)

    zapi.host.create(etcd_v34_1)
    zapi.host.create(etcd_v34_2)
    zapi.host.create(etcd_v34_3)
