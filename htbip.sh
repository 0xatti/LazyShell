#!/bin/bash
#Gets IP of Hackthebox VPN
#Add to your path and give alias "htbip"
/sbin/ifconfig tun0 | grep "10.10." | awk '{print $2}'
