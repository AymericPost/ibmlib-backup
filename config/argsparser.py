import argparse
from email.policy import default

from utils.argschecks import openssh_pk, remote_host, is_directory, uppercase

# Argument parser settings :

argsParser = argparse.ArgumentParser()
# Deactivated until more R&D is done:
# argsParser.add_argument("-U", "--unlock",
#                         help="Removes locks on remote resources before attempting to create a SAVF.",
#                         action="store_true")

argsParser.add_argument("--no-checksum", action="store_true",
                        help="Deactivates checksum. Do it only if necessary")

argsParser.add_argument("-k", "--private-key", type=openssh_pk, required=False,
                        help="Path to private OpenSSH key for credentialess login. The script will still prompt for user name if not given by arguments.")

argsParser.add_argument("-u", "--user", help="Provides user name for authentification.")

argsParser.add_argument("-t", "--time-out", type=int, default=30,
                        help="Maximum wait time in seconds for remote scripts to provide results. Default=30")

argsParser.add_argument("-e", "--exec-path", default="/usr/share/ibmbackup.sh",
                        help="Path to QSH script on remote IBMi. Target will be sujected to hash check. Default='/usr/share/ibmbackup.sh'")

argsParser.add_argument("-c", "--clle-path", default="QSHLIBBKUP",
                        help="CLLE binary creating SAVF on remote IBMi. Default='QGPL/QSHLIBBKUP'")

argsParser.add_argument("-o", "--output", default="./out/", type=is_directory,
                        help="Path to output generated SAVF on localhost.")

argsParser.add_argument("host", type=remote_host,
                        help="<Required> Remote IBMi host address.")

argsParser.add_argument('library', nargs="+", type=uppercase,
                        help="<Required> Libraries to backup as SAVF.")

namespace = argsParser.parse_args()
