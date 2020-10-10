import os
import time
import requests

red = '\033[31m'
blue = '\033[34m'
green = '\033[32m'
default = '\033[0m'

def install():
    os.system('cd')
    os.system('pkg install git python python2 wget curl php -y')
    os.system('clear')
    print(green+'tool installed :)')
    os.system('cd')

print(green+"""
 _____           _   __  __            _        _
|_   _|__   ___ | | |  \/  | __ _ _ __| | _____| |_
  | |/ _ \ / _ \| | | |\/| |/ _` | '__| |/ / _ \ __|
  | | (_) | (_) | | | |  | | (_| | |  |   <  __/ |_
  |_|\___/ \___/|_| |_|  |_|\__,_|_|  |_|\_\___|\__|
  """)
print(' ')
print(red+"""
{1} OSIF (open source information Facebook)

{2} nmap (network scanner)

{99} Exit

{999} Write Feedback or Requests tool

"""+default)
while True:
    usr = int(input('Your choice :'))

    if usr == 1:
        install()
        os.system('git clone https://github.com/CiKu370/OSIF')
        print("""usage :::
        $ cd OSIF
        $ pip2 install requests
        $ python2 osif.py""")
        break
    elif usr == 2:
        os.system('pkg install nmap')
        print("""usage :::
        nmap -help""")
        break
    elif usr == 999:
        p = input(red+'feedback :'+default)
        req = requests.post('https://friend3ds.000webhostapp.com/test/feedback.php', data={'msg':p})
    elif usr == 99:
        print(blue+'have a nice day :)'+default)
        break 
    

