from clients.ssh import get_ssh_client
from config.argsparser import namespace

if __name__ == "__main__":    
    ssh = get_ssh_client(namespace.host, namespace.user, namespace.private_key)

    ssh.close()
