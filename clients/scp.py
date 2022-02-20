from scp import SCPClient

def get_scp_client(ssh_client):
    return SCPClient(ssh_client.get_transport())