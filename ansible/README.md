# Zabbix create hosts

zabbix_create_hosts.yml is a simple playbook for adding hosts to Zabbix.
The "inventory" file contains a description of the hosts. Groups and templates must exist.

To use it, run:  

```
ansible-playbook zabbix_create_hosts.yml -i inventory

```
