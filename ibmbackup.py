from time import sleep

from config.argsparser import namespace
from clients.ssh import get_ssh_client
from utils.checksum import checksum

if __name__ == "__main__":
    ssh = get_ssh_client(namespace.host, namespace.user, namespace.private_key)

    # Checks if remote script exists and is the same as local script
    checksum(ssh, namespace.exec_path)

    ssh.close()
    del ssh
