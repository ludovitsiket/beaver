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
    return(subprocess.call(["smbclient //", shares]))


def mount_samba(addr):
    return(print('Mount ' + addr))


def check_viruses():
    return(subprocess.call("clamscan -r"))


def read_ip(some_file):
    i = 0
    with open(some_file, 'r') as f:
        value = f.readline()
        value = value.replace('\n', '')
        i += 1
    return value


def main_function():
    try:
        samba_machine = find_samba_shares(read_ip('ip.txt'))
    except FileNotFoundError as e:
        print(e)
        sys.exit()
    for item in samba_machine:
        connect_samba(item)
        mount_samba(item)
        viruses = check_viruses()
        print(viruses)


if __name__ == '__main__':
    main_function()
