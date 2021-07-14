import time
import os
import psutil
import multiprocessing
import platform
import colorama
from colorama import *
colorama.init()
from pythonping import ping

root = """
█▄▄ ▄▀█ █▀▄ █▀▀ █▀█ █▄░█ █▄░█ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄░█ █▀
█▄█ █▀█ █▄▀ █▄▄ █▄█ █░▀█ █░▀█ ██▄ █▄▄ ░█░ █ █▄█ █░▀█ ▄█"""

#sys
system = platform.uname()
system1 = platform.platform()
processor = platform.processor()

#заряд батареи 
battery = psutil.sensors_battery()
percent = int(battery.percent)

def main():
	battery1 = print(f"battery: {percent}%")
	print(system)
	print(system1)
	print("processor > " + processor)
	input("press any key")


print(root)
print("Run a system check")
roinput = input("""[bad_connections] - """)
if roinput == 'check_system-pcc':
	main()

if roinput == 'help':
    print("""1) all names in computer(txt) - check_user-pcc
2) os - check_os-pcc
3) ping - check_monitor-pcc
4) check - check_system-pcc
4) exit - exit!""")
    roinput = input("""[bad_connections] - """)

if roinput == 'check_user-pcc':
    os.system('net user > users.txt')
    time.sleep(1.3)
    print(Fore.GREEN + 'save is good')
    print(Style.RESET_ALL)
    input("press any key")
if roinput == 'check_os-pcc':
    if platform == "linux" or platform == "linux2":
        print(Fore.YELLOW + "system platform linux")
    elif platform == "darwin":
        print(Fore.YELLOW + "system platform mac os")
    elif platform == "win32":
        print(Fore.YELLOW + "system platform windows")
    print(Style.RESET_ALL)
    input("press any key")
if roinput == 'check_monitor-pcc':
    ping('8.8.8.8', verbose=True)
    input("press any key")
if roinput == 'exit!':
    input("button")
