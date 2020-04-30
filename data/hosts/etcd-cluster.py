def create_host(zapi):

    etcd_v34 = {
        "host": "etcs cluster",
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



    etcd_v32 = {
        "host": "etcs v3.2 cluster",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "etcdv2_1",
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

 
    zapi.host.create(etcd_v32)
    zapi.host.create(etcd_v34)
