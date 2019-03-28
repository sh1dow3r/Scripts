from ftplib import FTP

def main():
    USER="localhost"
    ftp = FTP(USER)
    login = ftp.log()

