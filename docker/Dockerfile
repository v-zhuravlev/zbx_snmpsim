FROM ubuntu

RUN apt-get update && apt-get install -y supervisor libcurl4 procps #fish

COPY supervisor.conf /etc/supervisor/conf.d/
COPY zabbix_agent2 /usr/sbin/zabbix_agent2
COPY zabbix_agent.conf /etc/zabbix/zabbix_agentd.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisor.conf"]