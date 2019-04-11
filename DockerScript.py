#!/usr/bin/python3

import argparse
import os
import docker 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose","-v", help="increase output verbosity",
                    action="store_true")
    parser.add_argument("--version", help=" Show version.",
                    action="store_true")
    parser.add_argument("-c <NumberOfDockerContainer>","--create", help="create a number of docker containers based the count giben")
    parser.add_argument("-i", "--interactive", help="Establish interactive shell access to each dokcer",
                    action="store_true")
    parser.add_argument("-n", help="show but not run the command to fix the ftp anonymous login",
                        action="store_true")
    parser.add_argument("ftp_ip", help="display a square of a given number")
    
         
    args = parser.parse_args()
    if args.verbose:
        print("verbose is turned on")
    
    if args.version:
        print("anonSaver v1.0")

    if args.fix:
        print("fixing")
        if args.yes:
            anonFix()
        else:
            answer = input("Are you sure you want to apply the fix? [y,n]")
            if answer == "yes" or answer == "y":
                anonFix()
            else:
                pass
    if args.n:
        print_fix()

    if args.ftp_ip:
        ip = args.ftp_ip
        anonCheck(ip)

# Get flags used
    



if __name__ == "__main__":
    main()
