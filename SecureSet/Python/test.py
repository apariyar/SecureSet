#!/usr/bin/python3
import datetime
import subprocess
vboxDict = {(1,8):"systems", (3,8): "systems", (0,8):"net", (2,8): "net", (0,13): "logs", (2,13):"logs", (1,13):"other", (3,13):"other", (4,8):"other", (4,13):"other"}

#app2run = '/usr/bin/VirtualBox'
app2run = "C:\\Users\\apari\\VirtualBox VMs\\Ubuntu 18.04 SYS400\\Ubuntu 18.04 SYS400.vbox"


def dh():
# get the date and hour at runtime
    dtz = datetime.datetime 
    time=dtz.today()  
    day = time.weekday()
    hour = time.hour
    return [day, hour]


def vbox(mylist):
    for key in vboxDict:
      if(key == mylist):
        return key

	
#   print("in vbox function')

def main():
    alist = dh()
    vm = vbox(alist)
   # print(vm)
    subprocess.Popen(app2run, shell = True)
    


if __name__ == "__main__":
    main()
    


