#!/usr/bin/python3

import argparse
import subprocess

parser = argparse.ArgumentParser(description="Manages and checks DHCP, DNS and FTP services running on the server")

parser.add_argument('-c', '--check', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-s', '--start-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-r', '--restart-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-p', '--stop-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-i', '--check-interval', nargs'?', type=int, default=300)

pargs = parser.parse_args()

args = vars(pargs)
for k in list(args.keys()):
    if not args[k]:
        del args[k]

for v in args:
    print(v)

if 'check' in args:
    for v in args['check']:
        subprocess.run(['systemctl', 'status', v])

if 'start_service' in args:
    for v in args['start_service']:
        subprocess.run(['sudo', 'systemctl', 'start', v])

if 'restart_service' in args:
    for v in args['restart_service']:
        subprocess.run(['sudo', 'systemctl', 'restart', v])

if 'stop_service' in args:
    for v in args['stop_service']:
        subprocess.run(['sudo', 'systemctl', 'stop', v])




