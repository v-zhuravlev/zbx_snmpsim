def create_agent_host(zapi):

    fpm_agent = {
        "host": "php-fpm_agent",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "",
                "dns": "fpm-agent",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        "tags": [
            {
                "tag": "PHP-FPM docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template App PHP-FPM by Zabbix agent"}, output=['id'])[0]
        ],
        "macros": [
            {
                "macro": "{$PHP_FPM.PORT}",
                "value": "8080"
            },
            # status is the page without redirect (since redirect is not supported by web.page.get)
            {
                "macro": "{$PHP_FPM.PROCESS_NAME}",
                "value": "php-fpm"
            }
        ],
        "inventory_mode": 0
    }


    fpm_http = {
        "host": "php-fpm_http",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 0,
                "ip": "127.0.0.1",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": zapi.hostgroup.get(filter={"name": "Discovered hosts"}, output=['id']),
        "tags": [
            {
                "tag": "PHP-FPM docker test",
                "value": ""
            }
        ],
        "templates": [
            zapi.template.get(filter={"name": "Template App PHP-FPM by HTTP"}, output=['id'])[0]
        ],
        "macros": [
            {
                "macro": "{$PHP_FPM.PORT}",
                "value": "8080"
            },
            {
                "macro": "{$PHP_FPM.HOST}",
                "value": "fpm-agent"
            }
        ],
        "inventory_mode": 0
    }
    zapi.host.create(fpm_agent)
    zapi.host.create(fpm_http)