import subprocess
import pathlib

def editCronTab(args):
    args = ' '.join(args)
    path = pathlib.Path(__file__).parent.absolute()

    with open('/tmp/crontmp', 'a+') as f:
        print(f'*/5 * * * * /usr/bin/python3 {path}/servchk.py -a {args}', file=f)
    subprocess.run(['sudo', 'crontab', '/tmp/crontmp'])
    subprocess.run(['rm', '/tmp/crontmp'])

def updateCronTab(args):
    subprocess.run(['sudo', 'crontab', '-l', '>', '/tmp/crontmp'])
    editCronTab(args)

