from ftplib import FTP
import ftplib
import argparse
import os

def anonCheck(ftp_server):
    try:
            server=ftp_server
            user = "anonymous"
            cred = user+"@"+server
            ftp = FTP(server, user, cred)
            ftp.quit()
            return True
    except Exception as e:
            print("FTP anonymous is disabled; You're good")
            return False

def anonFix():
    command = "sed -i 's/anonymous_enable=YES/anonymous_enable=NO/' /etc/vsftpd/vsftpd.conf"
    os.system(command)

    check = "cat /etc/vsftpd/vsftpd.conf | grep anonymous_enable=NO"
    check = os.system(check)
    if check:
        print("fix is done!")
    

def print_fix():
    print("""# Allow anonymous FTP? (Disabled by default).
            Changing this line:
                anonymous_enable=YES
            to:
                anonymous_enable=NO"
        """)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose","-v", help="increase output verbosity",
                    action="store_true")
    parser.add_argument("--version", help=" Show version.",
                    action="store_true")
    parser.add_argument("-f","--fix", help="fix the ftp anonymous login",
                    action="store_true")
    parser.add_argument("-y", "--yes", help="does not prompt the user for confirming the fix",
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
