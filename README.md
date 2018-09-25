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
Use bundled python script `add_snmpsim_hosts.py <snmpsim root data dir>` to mass create hosts and attach templates. (Requires py-zabbix, run `pip install py-zabbix` first)  
For example:
- `bin/add_snmpsim_hosts.py data` - to create hosts and attach templates for all *snmpwalk, *snmprec files found in the `data` dir.  
- `bin/add_snmpsim_hosts.py data --filter dlink` - to create host that contains `dlink` in the filename and attach `Template Net D-Link DES_DGS Switch SNMPv2` to them:
```
.\bin\add_snmpsim_hosts.py .\data\ --filter dlink
Found file .\data\net.dlink.DGS-3627G.snmpwalk...
Going to create host "net.dlink.DGS-3627G" with templates "[{'name': 'Template Net D-Link DES_DGS Switch SNMPv2', 'templateid': 10223}]" attached
Found file .\data\net.dlink.des3200.snmprec...
Going to create host "net.dlink.des3200" with templates "[{'name': 'Template Net D-Link DES_DGS Switch SNMPv2', 'templateid': 10223}]" attached
Found file .\data\net.dlink.dgs-3420-26sc.snmpwalk...
Going to create host "net.dlink.dgs-3420-26sc" with templates "[{'name': 'Template Net D-Link DES_DGS Switch SNMPv2', 'templateid': 10223}]" attached
```
- `bin/add_snmpsim_hosts.py --api_url http://myzabbix.local/api_jsonrpc.php --username=myuser --password mypassword data --snmpsim-ip=192.168.3.4` to create snmpsim hosts on the other Zabbix Server.  
Note that you need to provide *root* snmpsim directory that you mount into snmpsim, do not provide subdirs in the snmpsim data tree - otherwise {$SNMP_COMMUNITY} macro value would be wrong!  
See `--help` for usage.

### How to redefine host settings on creation
Work in progress!  
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