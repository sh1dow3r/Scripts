#!/usr/bin/python3
"""
take advantage of the number that show up in the second field when you do "ls -al" in /tmp directory.. 
For example if you want to send hello as a message for the receiver, you would create a "file1" 
and depending on the ASCII character number of the first letter you want to send, you will create that much soft links 
to the hard file and so on. For "H" it will create a file1 "1 being the first letter" and it will create 
a 72(The ACSII for the letter "H") soft links to that file and put it in dir1 "just to make less messy" 
after that it will create a second file called file2 "2 being the second letter" and it will create 
a 69 (The ACSII for the letter "E") and so on until it creates the full message which was "HELLO" 

After that, that, the receiver would scan the tmp  directory looks for how many symbolic links in there then 
make a list of the files of its symlink and convert the number of each file to an ASCII equivalent of the corresponding number.
"""

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


