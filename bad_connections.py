# -*- coding: utf-8 -*-
from pythonping import ping
import platform
import colorama
import random
from colorama import Fore, Back, Style
colorama.init()
from sys import platform
import time
import os
from time import sleep

root = """
█▄▄ ▄▀█ █▀▄ █▀▀ █▀█ █▄░█ █▄░█ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄░█ █▀
█▄█ █▀█ █▄▀ █▄▄ █▄█ █░▀█ █░▀█ ██▄ █▄▄ ░█░ █ █▄█ █░▀█ ▄█"""
print(root)
print("""bad_connections true utility""")
print("""
команда для помощи help""")
user_pass = input("""[bad_connections] - """)
if user_pass == 'help':
    print("""1) all names in computer(txt) - check_user-pcc
2) os - check_os-pcc
3) ping - check_monitor-pcc
4) exit - exit!""")
    user_pass = input("""[bad_connections] - """)
if user_pass == 'check_user-pcc':
    os.system('net user > users.txt')
    time.sleep(1.3)
    print(Fore.GREEN + 'save is good')
    print(Style.RESET_ALL)
    input("press any key")
if user_pass == 'check_os-pcc':
    if platform == "linux" or platform == "linux2":
        print(Fore.YELLOW + "system platform linux")
    elif platform == "darwin":
        print(Fore.YELLOW + "system platform mac os")
    elif platform == "win32":
        print(Fore.YELLOW + "system platform windows")
    print(Style.RESET_ALL)
    input("press any key")
if user_pass == 'check_monitor-pcc':
    ping('8.8.8.8', verbose=True)
    input("press any key")
if user_pass == 'exit!':
    input("button")