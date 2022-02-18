import os
import argparse

# Argument checking functions :

def remote_host(arg_val): 
    pong = os.system("ping {} 1 {} {}"
                    .format( ("-c", "-n")[os.name == 'nt'],
                            arg_val,
                            ("> /dev/null 2>&1", os.devnull)[os.name == "nt"]) )

    if pong == 0:
        return arg_val
    else:
        raise argparse.ArgumentTypeError("Cannot reach host: {}.".format(arg_val))

def openssh_pk(arg_val):
    if(os.path.isfile(arg_val)):
        with open(arg_val, "r") as file:
            first_line = file.readline()

            if(first_line.startswith("-----BEGIN OPENSSH PRIVATE KEY-----") ):
                return arg_val
            else:
                raise argparse.ArgumentTypeError("File {} is not an OpenSSH private key.".format(arg_val))
    else:
        raise argparse.ArgumentTypeError("File {} does not exist.".format(arg_val))


# Argument parser settings :

argsParser = argparse.ArgumentParser()
argsParser.add_argument("-U", "--unlock", 
                        help="Removes locks on remote resources before attempting to create a SAVF.",
                        action="store_true")

argsParser.add_argument("-k", "--private-key",
                        help="Private OpenSSH key for credentialess login. The script will still prompt for user name if not given by arguments.",
                        type=openssh_pk, required=False)

argsParser.add_argument("-u", "--user", help="Provides user for authentification.")

argsParser.add_argument("-t", "--time-out", type=int, default=30,
                        help="Maximum wait time in seconds for remote scripts to provide results.")

argsParser.add_argument("host", help="<Required> Remote IBMi host address.",
                        type=remote_host)

argsParser.add_argument('library', nargs="+",
                        help="<Required> Libraries to backup as SAVF.")

namespace = argsParser.parse_args()
