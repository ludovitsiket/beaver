import sys
import subprocess


def find_samba_shares(addr):
    shares = []
    machine = subprocess.call(["sudo", "smbclient", "-L", addr])
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


def mount_samba(addr):
    print('Mount ' + addr)
    return


def check_viruses():
    result = subprocess.call("clamscan -r")
    return result


def main_function():
    address = ''
    samba_machine = find_samba_shares(address)
    for item in samba_machine:
        connect_samba(item)
        mount_samba(item)
        viruses = check_viruses()
        print(viruses)


main_function()

