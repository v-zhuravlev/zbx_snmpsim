#!/usr/bin/env python
import os
import sys
import glob

from pyzabbix.api import ZabbixAPIException
import snmpsim_rules


class SnmpsimCreator:

    def __init__(self, path, zapi, filter_str, snmpsim_ip, snmpsim_dns, snmpsim_port):
        self.zapi = zapi
        self.path = path
        self.filter_str = filter_str
        self.h_interface = self.prepare_interface(
            snmpsim_ip, snmpsim_dns, snmpsim_port)

    def prepare_interface(self, ip, dns, port):
        h_interface = {
            "type": 2,
            "main": 1,
            "useip": 0,
            "ip": "",
            "dns": "",
            "port": "161"
        }
        if (ip):
            h_interface['ip'] = ip
            h_interface['useip'] = 1
        elif (dns):
            h_interface['dns'] = dns
        if (port):
            h_interface['port'] = port
            # h_interface['useip'] = 0

        return h_interface

    def create_host(self, host):
        """This creates snmpsim host in Zabbix"""
        DISCOVERY_GROUP_ID = "5"  # TODO make this configurable

        # prepare params
        params = {
            "host": "",
            "interfaces": [
                self.h_interface
            ],
            "macros": [

            ],
            "groups": [
                {
                    "groupid": DISCOVERY_GROUP_ID  # Discovered hosts
                }
            ],
            "templates": [

            ]
        }
        # apply some rules to params
        rules = snmpsim_rules.SnmpsimRules(self.zapi, params, host)
        try:
            rules.apply_all_rules()
        except ZabbixAPIException as err:
            print(err.data)
        except snmpsim_rules.ZabbixNotFoundException as err:
            print(err.error)
        finally:
            params = rules.get_params()

            # check for .json file
            # TODO add support of rewriting defaults by adding .json files with the same name

            try:
                print("Going to create host \"{}\" with templates \"{}\" attached".format(
                    params['host'], params['templates']))
                self.zapi.do_request('host.create', params)
            except ZabbixAPIException as err:
                if "Host with the same name" in err.data:
                    print("Host with the same name \"{}\" already exists. Skipping".format(
                        params['host']))
                else:
                    print(err.data)

    def create_single_host(self, host):
        """This creates single host"""

        print("Found file {}...".format(host))
        self.create_host(host)

    def scan_dir_with_snmpsim_files(self, dirname):
        """This finds all snmpsim snapshots in the directory"""

        hosts = []
        for file in glob.glob(dirname + '/*' + self.filter_str + "*.snmpwalk"):
            hosts.append(file)
        for file in glob.glob(dirname + '/*' + self.filter_str + "*.snmprec"):
            hosts.append(file)

        return hosts

    def scan_snmpsim_root_dir(self):
        """This scans snmpsim data dir recursively"""
        prev_dir = os.getcwd()
        os.chdir(self.path)
        hosts = []
        for root, _, _ in os.walk('.'):
            hosts.extend(self.scan_dir_with_snmpsim_files(root))
        hosts.sort()
        if len(hosts) == 0:
            print("No snmpsim hosts found in the directory '{}' with filter: {}".format(
                self.path, self.filter_str))
        else:
            for host in hosts:
                self.create_single_host(host)
        os.chdir(prev_dir)
