from __future__ import print_function
import sys
import random
import docker

client = docker.from_env()


def createD(name1, name2):

    d1 = client.containers.create(image="alpine",name=name1, command='sleep 10000', auto_remove=False)
    d2 = client.containers.create(image="alpine",name=name2, command='sleep 10000', auto_remove=False)
    return d1,d2
    #return client.containers.run("alpine", ["echo", "hello", "world"])

def myShell(container):
    command = input("interactive shell> ")
    print("type exit to quit the shell")
    check = "exit"
    container.start()
    while(command != check):
        log = container.exec_run(command,stderr=True, stdout=True)
        for line in log:
            print(line, end='')

def ping_hosts(cont1, cont2):
    pass

def inspect(cont1):
    pass

def networkType(cont1):
    pass

def start_host(cont1):
    pass

def stop_host(cont1):
    pass

def remove_host(cont1):
    pass
def running_host():
    pass

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
    cont1 = None
    cont2 = None
    banner()
    check_args()
    while True:
        menu = """\033[93m
             Enter an option (enter quit or 0 to exit)\n
             enter 1 for create a dokcer container with a choosen name \n
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
            #name1 = "Alamri_11"
            #name2 = "Almair_22"
            name1 = input("type a contanier name: ")
            name2 = input("type a contanier name: ")
            cont1, cont2 = createD(name1,name2)
            cont1Attr = cont1.attrs
            cont2Attr = cont2.attrs
            print("Container Id is:"+ str(cont1Attr["Id"]), "Container Name is: "+str(cont1Attr["Name"]))
            print("Container Id is:"+ str(cont2Attr["Id"]), "Container Name is: "+str(cont2Attr["Name"]))
        elif file == '2':
            myShell(cont1)
        elif file == '3':
            ping_host(cont1, cont2)
        elif file == '4':
            inspect(cont1)
        elif file == '5':
            networkType(cont1)
        elif file == '6':
            running_host()
        elif file == '7':
            start_host(cont1)
        elif file == '8':
            stop_host(cont1)
        elif file == '9':
            remove_host(cont1)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n\033[93m[!] ctrl+c detected from user, quitting.\n\n \033[0m')
