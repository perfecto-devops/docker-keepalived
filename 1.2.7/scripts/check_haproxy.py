#!/bin/bash
if [[ `curl -sL -w "%{http_code}\\n" -o /dev/null --connect-timeout 1 $1` -ne "200" ]]; then
        exit 1
fi
