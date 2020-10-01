FROM richarvey/nginx-php-fpm:latest

EXPOSE 8080


RUN set -eux && \
    addgroup -S -g 1995 zabbix && \
    adduser -S \
            -D -G zabbix -G root \
            -u 1997 \
            -h /var/lib/zabbix/ \
        zabbix && \
    mkdir -p /etc/zabbix && \
    mkdir -p /etc/zabbix/zabbix_agentd.d && \
    mkdir -p /var/lib/zabbix && \
    mkdir -p /var/lib/zabbix/enc && \
    mkdir -p /var/lib/zabbix/modules && \
    apk add --no-cache --clean-protected \
            tini \
            bash \
            coreutils \
            iputils \
            pcre \
            libcurl \
            libldap && \
    rm -rf /var/cache/apk/*


RUN apk update
RUN apk add zabbix-agent
COPY www.conf /usr/local/etc/php-fpm.d/www.conf
COPY nginx.conf /etc/nginx/sites-enabled/fpm.conf
COPY zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf
COPY zabbix_agent_supervisor.conf   /etc/supervisor/conf.d/zagent.conf
CMD ["/start.sh"]