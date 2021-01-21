#!/usr/bin/python3

import argparse
import subprocess
from cronh import *
import json
from pathlib import Path

def cleanArgs(args):
    for k in list(args.keys()):
        if not args[k]:
            del args[k]
    return args

curpath = getPath()
services = json.load(open(f'{curpath}/services.json'))

parser = argparse.ArgumentParser(description="Manages and checks DHCP, DNS and FTP services running on the server")

parser.add_argument('-c', '--check', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-s', '--start-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-r', '--restart-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-p', '--stop-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-a', '--check-start', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-i', '--check-interval', nargs='+', choices=['dhcp', 'ftp', 'dns'])

pargs = parser.parse_args()
args = cleanArgs(vars(pargs))

if not args:
    parser.print_help()

if 'check' in args:
    for v in args['check']:
        try:
            subprocess.check_output(['systemctl', 'is-active', services[v]])
            print(f'{v} service is currently running. For more information run:')
            print(f'\tsystemctl status {services[v]}')
        except:
            print(f'{v} service is NOT running. It can be started with:')
            print(f'\tsystemctl start {services[v]}')

if 'start_service' in args:
    for v in args['start_service']:
        subprocess.run(['sudo', 'systemctl', 'start', services[v]])

if 'restart_service' in args:
    for v in args['restart_service']:
        subprocess.run(['sudo', 'systemctl', 'restart', services[v]])

if 'stop_service' in args:
    for v in args['stop_service']:
        subprocess.run(['sudo', 'systemctl', 'stop', services[v]])

if 'check_start' in args:
    for v in args['check_start']:
        try:
            subprocess.check_output(['systemctl', 'is-active', services[v]])
        except:
            subprocess.run(['sudo', 'systemctl', 'start', services[v]])

if 'check_interval' in args:
    updateCronTab(args['check_interval'])

