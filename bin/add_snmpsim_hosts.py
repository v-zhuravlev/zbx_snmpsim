#!/usr/bin/env python
import argparse
import os
import sys
from zabbix.api import ZabbixAPI
from pyzabbix.api import ZabbixAPIException
import snmpsim_rules
import zabbix_cli


def prepare_interface(ip, dns, port):
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
        #h_interface['useip'] = 0

    return h_interface


def create_host(path, h_interface):
    """This creates snmpsim host in Zabbix"""
    DISCOVERY_GROUP_ID = "5"

    # prepare params
    params = {
        "host": "",
        "interfaces": [
            h_interface
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
    rules = snmpsim_rules.SnmpsimRules(zapi, params, path)
    rules.apply_all_rules()
    params = rules.get_params()

    # check for .json file
    # TODO add support of rewriting defaults by adding .json files with the same name

    try:
        print "Going to create host \"{}\" with templates \"{}\" attached".format(
            params['host'], params['templates'])
        zapi.do_request('host.create', params)
    except ZabbixAPIException as err:
        if "Host with the same name" in err[0]:
            print "Host with the same name \"{}\" already exists. Skipping".format(
                params['host'])
        else:
            print (err[0])


def create_single_host(host, h_interface):
    """This creates single host"""

    print ("Found file {}...".format(host))
    create_host(host, h_interface)


def import_dir_with_snmpsim_files(dirname, h_interface):
    """This creates all hosts found in the directory"""
    import glob

    hosts = []
    for file in glob.glob(dirname+'/*'+args.filter_str+"*.snmpwalk"):
        hosts.append(file)
    for file in glob.glob(dirname+'/*'+args.filter_str+"*.snmprec"):
        hosts.append(file)
    if len(hosts) == 0:
        sys.exit("No hosts found in the directory '{}' with filter: {}".format(
            dirname, args.filter_str))
    hosts.sort()
    for host in hosts:
        create_single_host(host, h_interface)


zabbix_parser = zabbix_cli.zabbix_default_args()
parser = argparse.ArgumentParser(parents=[zabbix_parser], add_help=False)
parser.add_argument('--filter', '-f', dest='filter_str',
                    help="imports only files in directory that contain chars in the filenames.",
                    required=False, type=str, default='')
parser.add_argument(dest='arg1', nargs=1,
                    help='provide file or directory name', metavar='path')
parser.add_argument('--snmpsim-dns', dest="snmpsim_dns", default="snmpsim",
                    help="DNS address of the snmpsim server. Use 'snmpsim' if inside docker network",
                    metavar="snmpsim")
parser.add_argument('--snmpsim-ip', dest="snmpsim_ip",
                    help="IP address of the snmpsim server.",
                    metavar="IP")
parser.add_argument('--snmpsim-port', dest="snmpsim_port", default="161",
                    help="UDP port of the snmpsim server.",
                    metavar="161")
args = parser.parse_args()

try:
    zapi = ZabbixAPI(url=args.api_url,
                     user=args.username,
                     password=args.password)
except ZabbixAPIException as err:
    print (err[0])
else:
    h_interface = prepare_interface(
        args.snmpsim_ip, args.snmpsim_dns, args.snmpsim_port)

    path = args.arg1[0]
    if os.path.isdir(path):
        import_dir_with_snmpsim_files(path, h_interface)
    elif os.path.isfile(path):
        create_single_host(path, h_interface)
    else:
        sys.exit("{0} is not a valid filename or directory".format(path))

    zapi.do_request('user.logout')
