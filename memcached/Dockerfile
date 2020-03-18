FROM memcached:1.6.0
# FROM redis:4
USER root
RUN  apt-get update && apt-get install -y supervisor libcurl4 procps libpcre3
# RUN ln -s /lib/x86_64-linux-gnu/libpcre.so.3 /lib/x86_64-linux-gnu/libpcre.so.1
EXPOSE 11211 10050
COPY supervisor.conf /etc/supervisor/conf.d/
COPY zabbix_agent2 /usr/sbin/zabbix_agent2
COPY zabbix_agent.conf /etc/zabbix/zabbix_agentd.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisor.conf"]