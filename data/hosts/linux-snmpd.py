def create_host(zapi):

    params = {
        "host": "linux-snmpd",
        "interfaces": [
            {
                "type": 2,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "linux-snmpd",
                "port": "161"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        "tags": [
            {
                "tag": "Linux",
                "value": ""
            },
            {
                "tag": "SNMP",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template OS Linux SNMPv2"}, output=['id'])[0]
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)