#!/usr/bin/python3

import argparse
import datetime
import subprocess

parser = argparse.ArgumentParser(description="Manages and checks DHCP, DNS and FTP services running on the server")

parser.add_argument('-c', '--check', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-ss', '--start-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-st', '--stop-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-ci', '--check-interval', type=int)

pargs = parser.parse_args()

for serv in pargs.check:
    subprocess.call(['sudo', 'systemctl', 'status' serv])
