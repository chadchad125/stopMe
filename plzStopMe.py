import psutil
import win32api
import time
import schedule

PROCNAMES = ["LeagueClient.exe", "RiotClientServices.exe"]
messages = ["No", "Dude, no", "Shit dude, Stop it!", "..."]
count = 0

def StopMeDammit():
    global count
    # Loops through not allowed list
    for PROCNAME in PROCNAMES:
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME:
                proc.kill()
                if(count < len(messages)):
                    win32api.MessageBox(0, messages[count], 'Stop it!')
                    count += 1

def ResetCount():
    global count
    count = 0

schedule.every(5).seconds.do(StopMeDammit)
schedule.every().hour.do(ResetCount)

while True:
    schedule.run_pending()
    time.sleep(1)
        
