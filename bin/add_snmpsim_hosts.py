#!/usr/bin/env python
import argparse
import os
import sys
from zabbix.api import ZabbixAPI
from pyzabbix.api import ZabbixAPIException
import snmpsim_rules
import zabbix_cli
import glob


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
    DISCOVERY_GROUP_ID = "5" #TODO make this configurable

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
    try:
        rules.apply_all_rules()
    except ZabbixAPIException as err:
        print(err)
    params = rules.get_params()

    # check for .json file
    # TODO add support of rewriting defaults by adding .json files with the same name

    try:
        print("Going to create host \"{}\" with templates \"{}\" attached".format(
            params['host'], params['templates']))
        zapi.do_request('host.create', params)
    except ZabbixAPIException as err:
        if "Host with the same name" in err[0]:
            print("Host with the same name \"{}\" already exists. Skipping".format(
                params['host']))
        else:
            print(err[0])


def create_single_host(host, h_interface):
    """This creates single host"""

    print("Found file {}...".format(host))
    create_host(host, h_interface)


def scan_dir_with_snmpsim_files(dirname):
    """This finds all snmpsim snapshots in the directory"""

    hosts = []
    for file in glob.glob(dirname+'/*'+args.filter_str+"*.snmpwalk"):
        hosts.append(file)
    for file in glob.glob(dirname+'/*'+args.filter_str+"*.snmprec"):
        hosts.append(file)

    return hosts


def scan_snmpsim_root_dir(datadir):
    """This scans snmpsim data dir recursively"""
    os.chdir(datadir)
    hosts = []
    for root, _, _ in os.walk('.'):
        hosts.extend(scan_dir_with_snmpsim_files(root))
    hosts.sort()
    if len(hosts) == 0:
        sys.exit("No hosts found in the directory '{}' with filter: {}".format(
            datadir, args.filter_str))
    for host in hosts:
        create_single_host(host, h_interface)


zabbix_parser = zabbix_cli.zabbix_default_args()
parser = argparse.ArgumentParser(parents=[zabbix_parser], add_help=False)
parser.add_argument('--filter', '-f', dest='filter_str',
                    help="imports only files in directory that contain chars in the filenames.",
                    required=False, type=str, default='')
parser.add_argument(dest='arg1', nargs=1,
                    help='provide snmpsim data directory name', metavar='path')
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
    print(err[0])
else:
    h_interface = prepare_interface(
        args.snmpsim_ip, args.snmpsim_dns, args.snmpsim_port)

    path = args.arg1[0]
    if os.path.isdir(path):
        scan_snmpsim_root_dir(path)
    else:
        sys.exit("{0} is not a valid directory".format(path))

    zapi.do_request('user.logout')
