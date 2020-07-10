

FROM zabbix/zabbix-proxy-sqlite3:centos-5.0-latest
USER root
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV NLS_LANG American_America.UTF8
RUN yum -y install wget

RUN wget https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
RUN wget https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-odbc-19.6.0.0.0-1.x86_64.rpm
RUN yum -y install oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm
RUN yum -y install oracle-instantclient19.6-odbc-19.6.0.0.0-1.x86_64.rpm


RUN wget https://dev.mysql.com/get/Downloads/Connector-ODBC/8.0/mysql-connector-odbc-8.0.19-1.el7.x86_64.rpm
RUN yum -y install mysql-connector-odbc-8.0.19-1.el7.x86_64.rpm