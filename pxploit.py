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

def scanner(i,p):
    for x in p:
        try:
            s = socket.socket()
            s.connect((i, int(x)))
            s.settimeout(3)
            service = ""
            try:
                service = s.recv(1024).decode()
            except Exception as e:
                e = str(e)
                if "utf-8" in e:
                    service = s.recv(1024)
                else:
                    service = "Can't find service"
            print("\r┏━Port {} Open".format(x))
            print("┗━🢖 {}".format(service))
        except socket.error as e:
            print("\rport {}".format(x), end='\r')
            continue
    s.close()
    print("\nDONE!")
    sys.exit()


if __name__ == '__main__':
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
            print("[-] Something wrong!\n\t{}\n\nReport issue: https://github.com/DwiWardana/pxploit/issues\nEmail me: mrxy@parsect.com".format(e))
