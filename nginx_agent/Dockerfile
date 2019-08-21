FROM nginx
RUN apt-get update -y && apt-get install -y wget
RUN wget https://repo.zabbix.com/zabbix/4.2/debian/pool/main/z/zabbix-release/zabbix-release_4.2-2+buster_all.deb && dpkg -i zabbix-release_4.2-2+buster_all.deb
RUN apt-get update -y && apt-get install -y zabbix-agent

COPY stub-status.conf /etc/nginx/conf.d/stub-status.conf
COPY zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf
COPY my_wrapper_script.sh my_wrapper_script.sh
CMD ./my_wrapper_script.sh
