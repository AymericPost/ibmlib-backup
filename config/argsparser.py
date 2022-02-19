import argparse

from utils.argschecks import openssh_pk, remote_host

# Argument parser settings :

argsParser = argparse.ArgumentParser()
argsParser.add_argument("-U", "--unlock", 
                        help="Removes locks on remote resources before attempting to create a SAVF.",
                        action="store_true")

argsParser.add_argument("-k", "--private-key", type=openssh_pk, required=False,
                        help="Path to private OpenSSH key for credentialess login. The script will still prompt for user name if not given by arguments.")

argsParser.add_argument("-u", "--user", help="Provides user name for authentification.")

argsParser.add_argument("-t", "--time-out", type=int, default=30,
                        help="Maximum wait time in seconds for remote scripts to provide results. Default=30")

argsParser.add_argument("-e", "--exec-path", default="/usr/bin/ibmbackup.sh",
                        help="Path to QSH script on remote IBMi. Target will be sujected to hash check. Default='/usr/bin/ibmbackup.sh'")

argsParser.add_argument("host", type=remote_host,
                        help="<Required> Remote IBMi host address.")

argsParser.add_argument('library', nargs="+",
                        help="<Required> Libraries to backup as SAVF.")
