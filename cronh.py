import subprocess
import pathlib

def editCronTab(args):
    args = ' '.join(args)
    curpath = getPath()

    with open('/tmp/crontmp', 'a+') as f:
        print(f'*/5 * * * * /usr/bin/python3 {curpath}/servchk.py -a {args}', file=f)
    subprocess.run(['sudo', 'crontab', '/tmp/crontmp'])
    subprocess.run(['rm', '/tmp/crontmp'])
    print('Entry added to crontab file')

def updateCronTab(args):
    cmdtry = subprocess.Popen(['sudo', 'crontab', '-l'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    with open('/tmp/crontmp', 'w') as f:
        print(cmdtry.stdout.read().decode(), file=f)

    editCronTab(args)

def getPath():
    curpath = pathlib.Path(__file__).parent.absolute()
    return curpath
