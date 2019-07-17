import sys
import subprocess


def find_samba_shares():
    address = '192.168.1.12'
    shares = []
    machine = subprocess.call(["sudo", "smbclient", "-L", address])
    shares.append(machine)
    if shares is not True:
        print('No samba share found.')
        sys.exit()
    else:
        print(shares)
    return shares


def connect_samba(shares):
    connect = subprocess.call(["smbclient //", shares])
    return connect


def mount_samba():
    return


def check_viruses():
    return


samba_machine = find_samba_shares()
for item in samba_machine:
    connect_samba(item)
