#!/bin/env python3
import sys
import time

try:
    import requests
    import socket
    import pandas
except Exception as e:
    e = str(e).split("'")[1]
    print("No module named {a}\nTry run this syntax: pip install {a}".format(a=e))
    sys.exit(1)

def banner():
    print(
"""
Usage:
        -h => This message
        -u => Update database""")

def update():
    try:
        df = pandas.read_csv("https://raw.githubusercontent.com/offensive-security/exploitdb/master/files_exploits.csv")
        df.to_csv(".database/database.csv")
    except Exception as e:
        print(e)


def scanner(i,p):
    for x in p:
        try:
            s = socket.socket()
            s.connect((i, int(x)))
            if x != 3306:
                service = s.recv(1024).decode()
            else:
                service = s.recv(1024)
            print("\r┏━Port {} Open".format(x))
            print("┗━🢖 {}".format(service))
            s.settimeout(5)
        except socket.error as e:
            print("\rport {}".format(x), end='')
            continue


if __name__ == '__main__':
    helper = ['-u', '-h']
    try:
        if sys.argv[1] == "-u":
            update()
        else:
            banner()
        sys.exit(0)
    except Exception:
        pass
    try:
        print(
"""    ** **
   *******
   *******
 ** ***** **
**** *** ****
***** * *****
 ***********
***** * *****
**** *** ****
 ** ***** **
   *******
   *******
    ** **

By: MrXY ( mrxy@parsect.com )
================
PARSECT PXploit\n""")
        host = socket.gethostbyname(str(input("(ip/domain): ")))
        port = [x for x in range(1,65535)]
        scanner(host,port)
    except KeyboardInterrupt:
        print("\n[!] Exit (Ctrl+C)")
        sys.exit(0)
    except Exception as e:
        e = str(e)
        if "invalid literal" in e:
            print("[!] Your input is invalid!")
            sys.exit(1)
        else:
            print("[-] Something wrong!\n\t{}\n\nReport issue: https://github.com/DwiWardana/PXploit/issues\nEmail me: mrxy@parsect.com".format(e))
