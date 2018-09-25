#!/usr/bin/python
import os
from pyzabbix.api import ZabbixAPIException

def get_hostname_from_path(path):
    return os.path.basename(os.path.splitext(path)[0])

def get_snmp_community_from_path(path):
    return os.path.splitext(path[2:].replace('\\','/'))[0]


class SnmpsimRules():
    def __init__(self, zapi, params, path):
        self.zapi = zapi
        self.path = path
        self.params = params

    def get_params(self):
        return self.params

    def apply_all_rules(self):
        self.set_host()
        self.set_templates()
        self.set_snmp_community()

    def set_host(self):
        self.params['host'] = get_hostname_from_path(self.path)

    #TODO: add support to subdirs
    def set_snmp_community(self):
        macro = {
                "macro": "{$SNMP_COMMUNITY}",
                "value": get_snmp_community_from_path(self.path)
                }
        self.params['macros'].append(macro)
            
    
    def set_templates(self):
        """
        Choose base template by basename
        """
        templates = {

            "os.linux":"Template OS Linux SNMPv2",
            "os.win":"Template OS Windows SNMPv2",
            "net.cisco":"Template Net Cisco IOS SNMPv2",
            "net.ubnt":"Template Net Ubiquiti AirOS SNMPv1",
            "net.mikrotik":"Template Net Mikrotik SNMPv2",
            "net.juniper":"Template Net Juniper SNMPv2",
            "net.brocade.fc":"Template Net Brocade FC SNMPv2",
            "net.arista":"Template Net Arista SNMPv2",
            "net.alcatel":"Template Net Alcatel Timetra TiMOS SNMPv2",
            "net.extreme":"Template Net Extreme EXOS SNMPv2",
            "net.huawei.vrp":"Template Net Huawei VRP SNMPv2",
            "net.dlink.des72":"Template Net D-Link DES 7200 SNMPv2",
            "net.dlink":"Template Net D-Link DES_DGS Switch SNMPv2",
            "net.qtech":"Template Net QTech QSW SNMPv2",
            "net.dell":"Template Net Dell Force S-Series SNMPv2",
            "net.mellanox":"Template Net Mellanox SNMPv2",
            "net.qlogic":"Template Net Intel_Qlogic Infiniband SNMPv2",
            "net.tplink":"Template Net TP-LINK SNMPv2",
            "net.foundry":"Template Net Brocade_Foundry Nonstackable SNMPv2",
            "net.brocade":"Template Net Brocade_Foundry Nonstackable SNMPv2",
            "net.brocade.stack":"Template Net Brocade_Foundry Stackable SNMPv2",
            "net.netgear":"Template Net Netgear Fastpath SNMPv2",
            "net.hp.comware":"Template Net HP Comware HH3C SNMPv2",
            "net.hp":"Template Net HP Enterprise Switch SNMPv2",
            "server.dell":"Template Server Dell iDRAC SNMPv2",
            "server.supermicro":"Template Server Supermicro Aten SNMPv2",
            "server.ibm":"Template Server IBM IMM SNMPv1",
            "server.hp":"Template Server HP iLO SNMPv2",
            "server.cisco":"Template Server Cisco UCS SNMPv2",

        }
        for search_string, template_name in templates.iteritems():

            if search_string in get_hostname_from_path(self.path):
                #print "Found match {} in {}".format(search_string, template)
                template_id = self.zapi.get_id('template', item=template_name)
                if template_id:
                    template = {
                        "name": template_name,
                        "templateid": template_id
                    }
                    self.params['templates'].append(template)
                else:
                    raise ZabbixAPIException("No such template found: {}".format(template_name))
                break
