def create_host(zapi):

    params = {
        "host": "nginx-agent",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "nginx-agent",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        "tags": [
            {
                "tag": "Nginx docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template App Nginx by Zabbix agent"}, output=['id'])[0]
        ],
        "macros": [
            {
                "macro": "{$NGINX.STUB_STATUS.PORT}",
                "value": "8080"
            },
            # status is the page without redirect (since redirect is not supported by web.page.get)
            {
                "macro": "{$NGINX.STUB_STATUS.PATH}",
                "value": "status"
            }
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)
