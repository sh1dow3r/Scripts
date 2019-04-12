from __future__ import print_function
import sys
import time
import random

try:
    import requests
except ImportError:
    print('\n\033[93m[!] Requests library not found, please install before proceeding.\n\n \033[0m')
    sys.exit(1)

def banner():
    banner = """
       ____
__   _|  _ \  ___   ___
\ \ / / | | |/ _ \ / __|
 \ V /| |_| | (_) | (__
  \_/ |____/ \___/ \___|

        """
    print(banner)

def check_args():
    if len(sys.argv) != 1:
        print("Invalid number of arguments entered!")
        how_to_use = "python3 DockerAtEase.py"
        print('Use as:', how_to_use)
        sys.exit(1)

def main():
    banner()
    check_args()
    while True:
        menu = """\033[93m
             Enter an option or a file path (enter quit or q to exit)\n
             enter 1 for creating two dokcer with my last name \n
             enter 2 for eastablish an interactive shell access to each container \n
             enter 3 for ping between container \n
             enter 4 for inspect the parametes of the containers \n
             enter 5 for indicate the type of network connection you have\n
             enter 6 for inventory of running containers and resource use \n
             enter 7 for start the container\n
             enter 8 for stop the container\n
             enter 9 for remove the containter\n
             enter 0 for quit the program    \033[0m"""
        try:
            file = input(menu)
        except Exception:
            file = raw_input(menu)
        if file == 'quit' or file == '0':
            break
        if file == '1':
            print("hi1")
        elif file == '2':
            print("hi1")
        elif file == '3':
            print("hi1")
            # replace rails with other user if applicable
        elif file == '4':
            print("hi1")
        elif file == '5':
            print("hi1")
        elif file == '6':
            print("hi1")
        elif file == '7':
            print("hi1")
        elif file == '8':
            print("hi1")
        elif file == '9':
            print("hi1")



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n\033[93m[!] ctrl+c detected from user, quitting.\n\n \033[0m')
