import sys
import subprocess


def find_samba_shares():
    shares = []
    machine = subprocess.call(["sudo", "smbstatus", "-p"])
    shares.append(machine)
    if shares is not True:
        print('No samba share found.')
        sys.exit()
    else:
        print(shares)
    return shares


def connect_samba():
    return


def mount_samba():
    return


def check_viruses():
    return


samba_machine = find_samba_shares()
for item in samba_machine:
    print('...')
