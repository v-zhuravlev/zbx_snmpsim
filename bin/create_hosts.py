import argparse
import os
import sys
from pyzabbix.api import ZabbixAPI, ZabbixAPIException
from snmpsim_creator import SnmpsimCreator
from hosts_creator import HostsCreator
import zabbix_cli


if __name__ == "__main__":
    # zapi = ZabbixAPI(url='http://localhost/', user='Admin', password='zabbix')
    
    # fs = [os.path.splitext('hosts.' + f)[0] for f in os.listdir('./hosts') if f.endswith('.py')]
    # hosts = {m for m in map(
    #     importlib.import_module, fs) if hasattr(m, 'create_host')}
    # for h in hosts:
    #     try:
    #         h.create_host(zapi) 
    #     except ZabbixAPIException as err:
    #         print(err.data)

    # zapi.user.logout()

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
        print(err.data)

    else:
        path = args.arg1[0]
        if os.path.isdir(path):
            # snmpsim
            snmpsim_create = SnmpsimCreator(path, zapi, args.filter_str, args.snmpsim_ip, args.snmpsim_dns, args.snmpsim_port)
            snmpsim_create.scan_snmpsim_root_dir()
            
            hosts_create = HostsCreator(path, zapi, args.filter_str)
            hosts_create.scan_snmpsim_root_dir()
        else:
            sys.exit("{0} is not a valid directory".format(path))

        zapi.do_request('user.logout')
