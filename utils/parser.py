import os

import argparse

def remote_host(arg_val): 
    pong = os.system("ping {} 1 {} {}"
                    .format( ("-c", "-n")[os.name == 'nt'],
                            arg_val,
                            ("> /dev/null 2>&1", "> NUL")[os.name == "nt"]) )

    if pong == 0:
        return arg_val
    else:
        raise argparse.ArgumentTypeError("Cannot reach host: {}.".format(arg_val))

argsParser = argparse.ArgumentParser()
argsParser.add_argument("-u", "--unlock", 
                        help="Removes locks on remote resources before attempting to create a SAVF.",
                        action="store_true")
argsParser.add_argument("host", help="<Required>Remote IBMi host address.",
                        type=remote_host)
argsParser.add_argument("Libraries", help="<Required>Libraries to backup as SAVF.", nargs="*")

args = argsParser.parse_args()
print(args.Libraries)
