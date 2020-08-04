FROM centos

RUN yum -y update && yum -y install wget libnsl

RUN wget https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
RUN yum -y install oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm

COPY zabbix_agent2 /usr/sbin/zabbix_agent2
COPY zabbix_agent.conf /etc/zabbix/zabbix_agentd.conf

CMD ["/usr/sbin/zabbix_agent2", "-c", "/etc/zabbix/zabbix_agentd.conf"]