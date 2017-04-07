# accept a timestamp
# read the current date
# pump out a qsub script named by the timestamp, for the current date

import datetime
import sys
import subprocess
import time

jobs = int(subprocess.check_output("showq | grep areagan | wc -l",shell=True))
print(jobs)

max_jobs = 150
jobs_remaining = max_jobs - jobs

loop_counter = 0

while jobs_remaining > 24:
    ctime = subprocess.check_output("date +%S.%M.%H.%d.%m.%y",shell=True).rstrip()

    f = open('currdate.txt','r')
    tmp = f.read().rstrip()
    f.close()

    date = datetime.datetime.strptime(tmp,'%Y-%m-%d')
    date += datetime.timedelta(days=1)

    if date > datetime.datetime(2014,07,14):
    # if date > datetime.datetime(2013,5,27):
        print('date past search range')
        break
    else:
        loop_counter += 1
        print("in the loop, time number {0}".format(loop_counter))
        f = open('currdate.txt','w')
        tmp = f.write(date.strftime('%Y-%m-%d'))
        f.close()

        script = '''DATE={0}
for HOUR in 0{{0..9}} {{10..23}}
do
  sleep 0.1
  echo "${{DATE}}-${{HOUR}}"
  export DATE
  export HOUR
  qsub -qshortq -V runHour.qsub
done

\\rm {1}.sh
'''.format(date.strftime('%Y-%m-%d'),ctime)

        # print('writing {}.sh'.format(ctime))
        f = open('{}.sh'.format(ctime),'w')
        f.write(script)
        f.close()
    
        qstatus = subprocess.check_output(". {}.sh".format(ctime),shell=True)
        # print(qstatus)
        jobs_remaining -= 24
        print("24 jobs submitted, {0} jobs remaining".format(jobs_remaining))








