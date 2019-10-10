FROM rabbitmq:3.7-management-alpine

COPY rabbitmq.conf /etc/rabbitmq/
COPY make-cluster.sh /usr/local/bin/

RUN chmod u+rw /etc/rabbitmq/rabbitmq.conf \
    && chmod a+x /usr/local/bin/make-cluster.sh

EXPOSE 5672 15672 25672 4369 9100 9101 9102 9103 9104 9105
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["make-cluster.sh"]
