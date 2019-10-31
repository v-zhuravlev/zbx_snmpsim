FROM redis:5
# FROM redis:4

RUN apt-get update && apt-get install -y supervisor libcurl4 procps fish

EXPOSE 6379
COPY supervisor.master.conf /etc/supervisor/conf.d/
COPY supervisor.replica.conf /etc/supervisor/conf.d/
COPY zabbix_agent2.bin /usr/sbin/zabbix_agent2
COPY zabbix_agent.conf /etc/zabbix/zabbix_agentd.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisor.master.conf"]