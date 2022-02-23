# IBM Series i Libraries Backup

A python script with Shell and CLLE scripts friends that makes SAVFs out of IBMi libraries then SCP them to your computer.

## Setup

### Pre-requisites

- [Python 3+](https://www.python.org/)
- Python 3+ PIP

Python PIP is installed with Python on Windows. Make sure to check the box during installation. You can re-start the installation executable to modify the installation and make sure PIP is installed.

Python 3+ and PIP are included in official Linux packages lists.

- Debian based Linux

```sudo apt-get install python3 python3-pip``` 

- Arch based Linux

```sudo pacman -S python3 python-pip```

### Installation

Download the script by getting the ZIP archive from the 'Code' drop-down menu or if you have git set up on your computer, you can `git clone` it using your favorite method (HTTPS, SSH, GH-CLI).

The default output directory for the script is not included. You can create a "out" directory in the project root directory to make the `--output` argument optional.

Open a terminal / CMD from the downloaded file.

#### (Optional - But very recommended) Creating a Python virtual enviroment

A python virtual environment allows you to install additionnal python libraries just for the script's use without installing them globaly.

Generate a virtual environment with :

- Windows

```python -m venv env```

- UNIX

```python3 -m venv env```


Once the 'env' environment is screated, you can activate it with :

- Windows

```env\Scripts\activate.bat```

- UNIX

```source env/bin/activate```

Once you are done using the script, you can deactivate the virtual environment with : `deactivate`

#### Installing extra Python libraries

If you have a virtual environment, use :

```pip install -r requirements.txt```

If you don't, UNIX users need to make sure they are using the right version of pip : `pip3`.

### Setting up IBMi

#### Adding a homedir to your User Profile

To make use of this script, you need to make sure the user profile you intend to use to make the backup from has a home directory.

To make your home directory the same as your user profile, enter:

```CHGUSRPRF USRPRF(AS06005) HOMEDIR(*USRPRF)```

If the directory for your username doesn't exist, you need to create it. Start a Shell session with `QSH` then type :

```mkdir /home/YourUserName```

Exit then retry the `CHGUSRPRF` command.

#### Transfering the shell script

You can use tools like ACSBundle or SCP to transfer the 'ibm-remote/ibmbackup.sh' script to IBMi's /usr/share, which is the default location for this script.

SCP example :

```scp ibm-remote/ibmbackup.sh USERNAME@IBMi:/QOpenSys/usr/share/```

#### Compiling the CLLE program

You can open your IDE you use for IBMi programming and paste the content into a new CLLE source member then compile it. The shell script that calls the CLLE program will use your *LIBL by default to run it.

## Usage

You can use `python ibmbackup.py -h` to display usage instructions :

```
usage: ibmbackup.py [-h] [--no-checksum] [-k PRIVATE_KEY] [-u USER] [-t TIME_OUT] [-e EXEC_PATH] [-c CLLE_PATH]
                    [-o OUTPUT]
                    host library [library ...]

positional arguments:
  host                  <Required> Remote IBMi host address.
  library               <Required> Libraries to backup as SAVF.

optional arguments:
  -h, --help            show this help message and exit
  --no-checksum         Deactivates checksum. Do it only if necessary
  -k PRIVATE_KEY, --private-key PRIVATE_KEY
                        Path to private OpenSSH key for credentialess login. The script will still prompt for user name if
                        not given by arguments.
  -u USER, --user USER  Provides user name for authentification.
  -e EXEC_PATH, --exec-path EXEC_PATH
                        Path to QSH script on remote IBMi. Target will be sujected to hash check.
                        Default='/usr/share/ibmbackup.sh'
  -c CLLE_PATH, --clle-path CLLE_PATH
                        CLLE binary creating SAVF on remote IBMi. Default='QGPL/QSHLIBBKUP'
  -o OUTPUT, --output OUTPUT
                        Path to output generated SAVF on localhost.
```

If you intend to get SAVFs of MYLIB and MYLIB2 library from myibmi.com as ACCADMIN:

```python ibmbackup.py ibmi.com MYLIB MYLIB2```

If you have set your IBMi and your computer to use a 'id_rsa' OpenSSH key, for the same command with no prompt at all :

```python ibmbackup.py -u ACCADMIN -k ~/.ssh/id_rsa ibmi.com MYLIB MYLIB2```
