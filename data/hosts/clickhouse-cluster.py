def create_host(zapi):

    shard1_rep1 = {
        "host": "clickhouse_1_1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "ch1",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Templates/Databases"}, output=['id']),
        "tags": [
            {
                "tag": "Clickhouse docker test",
                "value": ""
            }
        ],
        "macros": [
            {
                "macro": "{$CLICKHOUSE.PASSWORD}",
                "value": "web"
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template DB ClickHouse by HTTP"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }
    shard1_rep2 = {
        "host": "clickhouse_1_2",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "ch2",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Templates/Databases"}, output=['id']),
        "tags": [
            {
                "tag": "Clickhouse docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template DB ClickHouse by HTTP"}, output=['id'])[0]
        ],

        "macros": [
            {
                "macro": "{$CLICKHOUSE.PASSWORD}",
                "value": "web"
            }
        ],
        "inventory_mode": 0
    }

    shard2_rep1 = {
        "host": "clickhouse_2_1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "ch3",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Templates/Databases"}, output=['id']),
        "tags": [
            {
                "tag": "Clickhouse docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template DB ClickHouse by HTTP"}, output=['id'])[0]
        ],
        "macros": [
            {
                "macro": "{$CLICKHOUSE.PASSWORD}",
                "value": "web"
            }
        ],
        "inventory_mode": 0
    }

    shard2_rep2 = {
        "host": "clickhouse_2_2",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "ch4",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Templates/Databases"}, output=['id']),
        "tags": [
            {
                "tag": "Clickhouse docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template DB ClickHouse by HTTP"}, output=['id'])[0]
        ],
        "macros": [
            {
                "macro": "{$CLICKHOUSE.PASSWORD}",
                "value": "web"
            }
        ],
        "inventory_mode": 0
    }

    zapi.host.create(shard1_rep1)
    zapi.host.create(shard1_rep2)
    zapi.host.create(shard2_rep1)
    zapi.host.create(shard2_rep2)