def create_host(zapi):

    params = {
        "host": "mysql-server-slave",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "mysql-zabbix-agent",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        "tags": [
            {
                "tag": "MySQL docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template DB MySQLv8"}, output=['id'])[0]
        ],
        "macros": [
            {
                "macro": "{$MYSQLSERVER}",
                "value": "mysql-server-slave"
            }
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)