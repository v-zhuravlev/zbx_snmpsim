FROM alpine:3.7
RUN apk add --no-cache net-snmp-tools net-snmp

EXPOSE 161/udp
COPY bootstrap.sh bootstrap.sh
#COPY snmpd.conf /etc/snmp/snmpd.conf
ENTRYPOINT ["/bootstrap.sh"]