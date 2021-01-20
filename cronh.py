import subprocess
import pathlib

def editCronTab(args):
    args = ' '.join(args)
    path = pathlib.Path(__file__).parent.absolute()

    with open('/tmp/crontmp', 'a+') as f:
        print(f'*/5 * * * * /usr/bin/python3 {path}/servchk.py -s {args}', file=f)
    subprocess.run(['sudo', 'crontab', '/tmp/crontmp'])
    subprocess.run(['rm', '/tmp/crontmp'])

def updateCronTab(args):
    try:
        subprocess.run(['crontab', '-l', '>', '/tmp/crontmp'])
    except:
        print("Crontab file not present, generating the file...\n")
        subprocess.run(['touch', '/tmp/crontmp'])

    editCronTab(args)

