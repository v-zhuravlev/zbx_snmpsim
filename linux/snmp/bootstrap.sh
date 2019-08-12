#!/bin/sh

set -u
# User params
USER_PARAMS=$@

# Internal params
RUN_CMD="snmpd -f ${USER_PARAMS} -Lo -I -p /run/snmpd.pid"


# Launch
$RUN_CMD

# Exit immidiately in case of any errors or when we have interactive terminal
if [[ $? != 0 ]] || test -t 0; then exit $?; fi
