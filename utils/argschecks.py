import os
import argparse

# Argument checking functions :

def remote_host(arg_val): 
    pong = os.system("ping {} 1 {} > {}"
                    .format( ("-c", "-n")[os.name == 'nt'],
                            arg_val,
                            ("/dev/null 2>&1", os.devnull)[os.name == "nt"]) )

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

def is_directory(arg_val):
    if(os.path.isfile(arg_val)):
        raise argparse.ArgumentTypeError(arg_val + " is a file. Output must be a directory.")
    elif(os.path.isdir(arg_val)):
        return arg_val
    else:
        raise argparse.ArgumentTypeError("Directory {} does not exist.".format(arg_val))

def uppercase(arg_val):
    return arg_val
