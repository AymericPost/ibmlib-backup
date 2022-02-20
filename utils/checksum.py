import sys
import os

def checksum(ssh, exec_path):
    ssh_in, ssh_out, ssh_err = ssh.exec_command(
        "sha256sum " + exec_path)
    exit_status = ssh_out.channel.recv_exit_status()

    # Exit status OK if remote script exists
    if(exit_status == 0):
        remote_sha256sum = ssh_out.readlines()[0].replace("\n", "").split("  ")[0]
        check_sha256sum = os.system(
            "echo '{}  ibm-remote/ibmbackup.sh' | sha256sum --check".format(remote_sha256sum))

        # Exit status OK if scripts are the same
        if(check_sha256sum == 0):
            del ssh_in, ssh_out, ssh_err
            return True
        else:
            ssh.close()
            del ssh_in, ssh_out, ssh_err, ssh

            sys.tracebacklimit = 0
            raise Exception("Remote file was modified.")
    else:
        ssh.close()
        del ssh_in, ssh_out, ssh_err, ssh

        sys.tracebacklimit = 0
        raise FileNotFoundError("File {} does not exist on remote host.".format(exec_path))
    