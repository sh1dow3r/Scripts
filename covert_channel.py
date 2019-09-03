#!/usr/bin/python3
import os
from pathlib import Path

#make a dirctory that has a n number of files
def makedir(path):
    cmd = "mkdir -p /tmp/"+path + " 2>/dev/null"
    os.system(cmd)
#make file
def makefile(fname):
    cmd = "echo -n > /tmp/"+fname+ " 2>/dev/null"
    os.system(cmd)

#make hard links  for given file 
def make_links(nLinks,i):
    si = str(i)
    for i in range(0, nLinks-1):
        cmd = "ln /tmp/file"+si+" /tmp/dir"+si+"/hard"+str(i)+" "+ "2>/dev/null"
        os.system(cmd)
#remove dir after reading
def removedir(path):
    print("removing dir in " + path)
    try:
        os.mkdir(path)
    except oserror:
        print("removing dir "+ path +" failed")
    else:
        print("successfully removed dir "+path)

def reader():
    cmd = "ls -l /tmp/file* | cut -d " " -f 3"
    lst = os.system(cmd)
    message = ""
    for i in lst:
        message = message+chr(i)
        print(message) #It should pring HELLO

def main():
    message = "HELLO"
    message_list = list(message)
    print(message_list)
    mlen = len(message_list)
    #n = 1
    #path = "/tmp/dir"+str(n)
    #print(path)
    for i in range(0, mlen):
        m = ord(message_list[i])
        m = int(m)
        makedir("dir"+str(i))
        makefile("file"+str(i))
        make_links(m,i)
        #n+=1
        
    #sleep(20)
    #removedir(path)
main()


