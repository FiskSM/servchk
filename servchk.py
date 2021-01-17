#!/usr/bin/python3

import argparse
import subprocess
import cronh

def cleanArgs(args):
    for k in list(args.keys()):
        if not args[k]:
            del args[k]
    return args

parser = argparse.ArgumentParser(description="Manages and checks DHCP, DNS and FTP services running on the server")

parser.add_argument('-c', '--check', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-s', '--start-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-r', '--restart-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-p', '--stop-service', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-a', '--check-start', nargs='+', choices=['dhcp', 'ftp', 'dns'])
parser.add_argument('-i', '--check-interval', nargs='?', type=int, default=5)

pargs = parser.parse_args()

args = cleanArgs(vars(pargs))

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

if 'check_start' in args:
    for v in args['check_start']:
        st = subprocess.check_output(['systemctl', 'show', v, '--value', '-p', 'ActiveState'])
        if st.decode('utf8') != 'active':
            subprocess.run(['sudo', 'systemctl', 'start', v])

if 'check_interval' in args:
    editCronTab(args['check_interval'])



