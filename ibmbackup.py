from time import sleep

from config.argsparser import namespace
from clients.ssh import get_ssh_client
from clients.scp import get_scp_client
from utils.checksum import checksum

if __name__ == "__main__":
    ssh = get_ssh_client(namespace.host, namespace.user, namespace.private_key)
    scp = get_scp_client(ssh)

    # Checks if remote script exists and is the same as local script
    checksum(ssh, namespace.exec_path)

    main_in, main_out, main_err = ssh.exec_command(
        "bash " + namespace.exec_path + " " + " ".join(namespace.library))

    while(not main_out.channel.exit_status_ready()):
        sleep(1)

    for library in namespace.library:
        print("Downloading {}.FILE...".format(library))
        scp.get("/home/{}/{}.FILE".format(namespace.user, library), namespace.output)
        print("Done.")

        print("Removing distant file...")
        ssh.exec_command("rm /home/{}/{}.FILE".format(namespace.user, library))
        print("Done.")

    ssh.close()
    del ssh
