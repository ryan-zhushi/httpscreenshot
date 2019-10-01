#!/bin/bash

nginx
echo -e 'nameserver 114.114.114.114' > /etc/resolv.conf
python3 /opt/httpscreenshot/httpscreenshot.py