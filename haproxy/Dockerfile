FROM haproxy:2.0
RUN apt-get update -y && apt-get install -y wget
RUN wget https://repo.zabbix.com/zabbix/4.2/debian/pool/main/z/zabbix-release/zabbix-release_4.2-2+buster_all.deb && dpkg -i zabbix-release_4.2-2+buster_all.deb
RUN apt-get update -y && apt-get install -y zabbix-agent

COPY my_wrapper_script.sh my_wrapper_script.sh
CMD ./my_wrapper_script.sh
