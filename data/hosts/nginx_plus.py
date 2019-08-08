def create_host(zapi):

    params = {
        "host": "nginx_plus",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "nginx",
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
            zapi.template.get(filter={"name": "Template App Nginx HTTP"}, output=['id'])[0],
            zapi.template.get(filter={"name": "Template App Nginx Plus HTTP"}, output=['id'])[0]
        ],
        "macros": [
            {
                "macro": "{$NGINX_STUB_STATUS_PORT}",
                "value": "8080"
            }
        ],
        "inventory_mode": 0
    }
    zapi.host.create(params)