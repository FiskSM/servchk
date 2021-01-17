import subprocess

def editCronTab(interval):
    with open('/tmp/crontmp', 'a+') as f:
        print(f'*/{interval} * * * * /usr/bin/python3 servchk -a', file=f)
    subprocess.run(['crontab', '/tmp/crontmp'])
    subprocess.run(['rm', '/tmp/crontmp'])

def updateCronTab(interval):
    try:
        subprocess.run(['crontab', '-l', '>', '/tmp/crontmp'])
    except:
        print("Crontab file not present, generating the file...\n")
        subprocess.run(['touch', '/tmp/crontmp'])

    editCronTab(interval)

