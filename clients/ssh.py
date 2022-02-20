
import os
import sys 
from distutils.log import error
from paramiko.ssh_exception import AuthenticationException
from getpass import getpass
from paramiko import SSHClient, RSAKey, AutoAddPolicy


def get_ssh_client(host, username, key_path):
    ssh = SSHClient()
    password = None
    key = None

    ssh.set_missing_host_key_policy(AutoAddPolicy)

    if(username is None):
        username = input("Username ({}): ".format(os.getlogin()))

        if(username == ""):
            username = os.getlogin()

    if(key_path is None):
        password = getpass("Password: ")
    else:
        key = RSAKey.from_private_key_file(key_path)
    
    try:
        if (key is None):
            ssh.connect(hostname=host, username=username, password=password)

            return ssh
        else:
            ssh.connect(hostname=host, username=username, pkey=key)

            return ssh
    except AuthenticationException:
        error("Login failed")
        del ssh
        sys.exit(1)
