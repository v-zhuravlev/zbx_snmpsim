# Zabbix snmpsim
[Work in progress]
This repo provides a quick way to test Zabbix SNMP templates with Zabbix and a snmpsim snapshots provided by snmpsim app.  



## Prepare simulation data
- Add file *.snmpwalk or *.snmprec to data dir. More on how to prepare simulation data is [here](http://snmplabs.com/snmpsim/building-simulation-data.html)

## Test with bundled Zabbix Server
- run docker-compose to start zabbix-server and snmpsim
`docker-compose.exe -f .\docker-compose.snmpsim.yml -f .\docker-compose.yml.zabbix up`
- Access Zabbix Frontend on http://localhost
- Add new host with SNMP interface and use DNS address `snmpsim` to connect, use port 161
- Add {$SNMP_COMMUNITY} macro with the same value as *.snmprec *.snmpwalk filename

## Test with already existing Zabbix Server
You can also just use snmpsim instance without bundled Zabbix Server and test with your own Zabbix that is up and running somewhere:
- Start snmpsim only: `docker-compose.exe -f .\docker-compose.snmpsim.yml up`
- Access Zabbix Frontend
- Add new host with SNMP interface and use IP address of the host you are running on, use port 161
- Add {$SNMP_COMMUNITY} macro with the same value as snmprec/snmpwalk filename

## Some automation
Use bundled python script `add_snmpsim_hosts.py` to mass create hosts and attach templates. (Requires py-zabbix, run `pip install py-zabbix` first)  
For example:
- `bin/add_snmpsim_hosts.py data` - to create hosts and attach templates for all *snmpwalk, *snmprec files found in the `data` dir.  
- `bin/add_snmpsim_hosts.py data/net.cisco.switch` - to create host `net.cisco.switch` and attach `Template Net Cisco IOS SNMPv2` to it.
- `bin/add_snmpsim_hosts.py data --filter juniper` - to create host that contains `juniper` in the filename and attach `Template Net Juniper SNMPv2` to them.
- `bin/add_snmpsim_hosts.py --api_url http://myzabbix.local/api_jsonrpc.php --username=myuser --password mypassword data --snmpsim-ip=192.168.3.4` to create snmpsim hosts on the other Zabbix Server.  

See `--help` for usage.

### How to redefine host settings on creation
Base templates depends on the filename. Some logic how template are choosen by default is defined here: `bin/snmpsim_rules.py#set_templates()`  

//TODO:  
You can rewrite any template settings by creating host.json file nearby host.snmpec file.  
For example:
```json
    {
        "templates":[
            "Template OS Linux",
            "Template ICMP Ping"
        ]
    }
```