"""
Author: Ali Alamri
Date: 4/24/2019
Description: this program provide an easy use of docker managment and gives the functionality of create, run, ping, interactive shell, stop and remove contaiers through a menue

"""

from __future__ import print_function
import sys
import random
import docker
import threading
import subprocess as sub


def createD(name1, name2):
    """
    This function takes two name and creates and run two container with a hard coded ubuntu image with those names
    after that it stop the container. The reason we used "run" instead of "create" is I needed to assign the conteiner
    a name when it's running if I just create it, it will asign it a differnet name.
    param:
        name1: the name of the first container
        name2: the name of the second continer
    """
    cont1 = "docker run --name {} -itd ubuntu:latest".format(name1)
    stop_cont1 = "docker stop {}".format(name1)
    cont2 = "docker run --name {} -itd ubuntu:latest".format(name2)
    stop_cont2 = "docker stop {}".format(name2)
    sub.call(cont1, shell=True)
    sub.call(stop_cont1, shell=True)
    sub.call(cont2,shell=True)
    sub.call(stop_cont2, shell=True)

def myShell(container):
    """
    This function return back the interactive shell back to the user taken the name of the container you want enter as an paramter
    param:
        container: the container you want to get a shell on
    """
    shell = "docker exec -it {} /bin/bash".format(container)
    sub.call(shell,shell=True)

def ping_hosts(cont1, cont2):
    """
    This function takes both contianer names as paramter and attaches them to new generated netwrok then ping between them reutrn true if successfull and false
    param:
        cont1: first contaienr to perform the ping
        cont2: second container to recieve the ping
    """
    new_network="docker network create hunter2" #my network name is hunter2
    connect1="docker network connect hunter2 {}".format(cont1) #connecting the first container to hunter2 netwrok
    connect2="docker network connect hunter2 {}".format(cont2) #connecting the second container to hunter2 network
    update1="docker exec -ti {} apt update ".format(cont1) #incase ping binary does not exist
    update2="docker exec -ti {} apt update".format(cont2) #incase ping binary does not exist
    install_ping1="docker exec -ti {} apt install -y iputils-ping ".format(cont1)
    install_ping2="docker exec -ti {} apt install -y iputils-ping ".format(cont2)
    magic_ping="docker exec -it {} ping {}".formant(cont1,cont2)
    sub.call(new_network,shell=True)
    sub.call(connect1, shell=True)
    sub.call(connect2,shell=True)
    sub.call(update1,shell=True)
    sub.call(update2,shell=True)
    sub.call(install_ping1,shell=True)
    sub.call(install_ping2,shell=True)
    sub.call(magic_ping,shell=True)

def inspect(cont1):
    """
    This function inspect the container given in the paramter and returen back a giant jason file with all the information in the that contiers. Things like(ID, createdat, state, name, network setting, mount, etc.)
    param:
        cont1: the container to be incpect
    """
    cont = "docker inspect {}".format(cont1)
    #jason1 = sub.Popen(cont,shell=True,stdout=sub.PIPE).communtication()[0]
    sub.call(cont,shell=True)

def networkType(cont1):
    pass

def start_host(cont1):
    cont = "docker start {}".format(cont1)
    sub.call(cont,shell=True)

def stop_host(cont1):
    cont = "docker stop {}".format(cont1)
    sub.call(cont,shell=True)

def remove_host(cont1):
    cont = "docker rm {}".format(cont1)
    sub.call(cont,shell=True)

def running_host():
    cont = "docker ps -a"
    sub.call(cont,shell=True)


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
        how_to_use = "python3 vDoc.py"
        print('Use as:', how_to_use)
        sys.exit(1)

def main():
    cont1 = ""
    cont2 = ""
    banner()
    check_args()
    while True:
        menu = """\033[93m
             Enter an option (enter quit or 0 to exit)\n
             enter 1 for create a docker container with a choosen name \n
             enter 2 for establish an interactive shell access to each container \n
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
            #name1 = "Alamri_11"
            #name2 = "Almair_22"
            cont1 = input("type a contanier name: ")
            cont2 = input("type a contanier name: ")
            createD(cont1,cont2)
            #print("Container Id is:"+ str(cont1Attr["Id"]), "Container Name is: "+str(cont1Attr["Name"]))
            #print("Container Id is:"+ str(cont2Attr["Id"]), "Container Name is: "+str(cont2Attr["Name"]))
        elif file == '2':
            cont1 = input("Which container? [ex. name of the container] ")
            myShell(cont1)
        elif file == '3':
            ping_hosts(cont1, cont2)
        elif file == '4':
            cont1 = input("Which container? [ex. name of the container] ")
            inspect(cont1)
        elif file == '5':
            cont1 = input("Which container? [ex. name of the container] ")
            networkType(cont1)
        elif file == '6':
            running_host()
        elif file == '7':
            cont1 = input("Which container? [ex. name of the container] ")
            start_host(cont1)
        elif file == '8':
            cont1 = input("Which container? [ex. name of the container] ")
            stop_host(cont1)
        elif file == '9':
            cont1 = input("Which container? [ex. name of the container] ")
            remove_host(cont1)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n\033[93m[!] ctrl+c detected from user, quitting.\n\n \033[0m')
