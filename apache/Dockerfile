FROM httpd:2.4
# RUN apk --no-cache add zabbix-agent
RUN apt-get update && apt-get install wget -y
RUN wget https://repo.zabbix.com/zabbix/4.2/debian/pool/main/z/zabbix-release/zabbix-release_4.2-2+buster_all.deb && dpkg -i zabbix-release_4.2-2+buster_all.deb
RUN apt-get update && apt-get install -y \
 zabbix-agent \
 supervisor
# RUN mkdir /var/run/zabbix && chmod a+w /var/run/zabbix
# RUN apt-get install procps -y

EXPOSE 8080
COPY httpd.conf /usr/local/apache2/conf/httpd.conf
COPY supervisor.conf /etc/supervisor/conf.d/
COPY zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]