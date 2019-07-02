import os
import importlib
import glob
import sys
from pyzabbix.api import ZabbixAPIException


class HostsCreator:

    def __init__(self, path, zapi, filter_str):
        self.zapi = zapi
        self.path = path
        self.filter_str = filter_str

    def scan_dir_with_snmpsim_files(self, dirname):
        """This finds all hosts_*.py files in the directory"""

        hosts = []
        for file in glob.glob(dirname + '/*' + self.filter_str + "*.py"):
            if '__init__' not in file:
                hosts.append(file)

        return hosts

    def scan_snmpsim_root_dir(self):
        """This scans datadir recursively"""
        prev_dir = os.getcwd()
        os.chdir(self.path)
        hosts = []
        for root, _, _ in os.walk('.'):
            hosts.extend(self.scan_dir_with_snmpsim_files(root))
        hosts.sort()
        if len(hosts) == 0:
            print("No hosts found in the directory '{}' with filter: {}".format(
                self.path, self.filter_str))
        else:
            # this to import from data dir...
            sys.path.append('.')
            hosts = [
                '.'.join(
                    os.path.split(
                        os.path.normpath(
                            os.path.splitext(h)[0]))) for h in hosts]

            host_configs = {m for m in map(
                importlib.import_module, hosts) if hasattr(m, 'create_host')}

            for hc in host_configs:
                try:
                    print("Going to create host using config \"{}\"".format(
                         hc.__file__))
                    hc.create_host(self.zapi)
                except ZabbixAPIException as err:
                    print(err.data)
        os.chdir(prev_dir)
