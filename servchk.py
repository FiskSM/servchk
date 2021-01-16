#!/usr/bin/python3

import argparse
import datetime

parser = argparse.ArgumentParser(description="Manages and checks DHCP, DNS and FTP services running on the server")

parser.add_argument('-c', '--check', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-ss', '--start-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-st', '--stop-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-ci', '--check-interval', type=int)

pargs = parser.parse_args()
#print(pargs)
print(pargs.check)
