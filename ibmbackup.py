from time import sleep

from config.argsparser import namespace
from clients.ssh import get_ssh_client
from utils.checksum import checksum

if __name__ == "__main__":
    print(namespace)
    ssh = get_ssh_client(namespace.host, namespace.user, namespace.private_key)

    # Checks if remote script exists and is the same as local script
    checksum(ssh, namespace.exec_path)

    main_in, main_out, main_err = ssh.exec_command(
        namespace.exec_path + " " + " ".join(namespace.library))

    while(not main_out.channel.exit_status_ready()):
        sleep(1)

    ssh.close()
    del ssh
