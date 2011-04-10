import os, sys
import logging
from logging.handlers import SysLogHandler 
from logging import StreamHandler
import plistlib

DEFAULT_PROVPROF_DIR = os.path.expanduser('~/Library/MobileDevice/Provisioning Profiles')

logger = logging.getLogger("%s[%s]" % (os.path.basename(sys.argv[0]),
    os.getpid(), ))

def isProvFile(filePath):
    return filePath.endswith('.mobileprovision')

def plistStringFromProvFile(path):
    beginToken = '<?xml'
    endToken = '</plist>'
    f = open(path)
    data = f.read()
    begin = data.index(beginToken)
    end = data.rindex(endToken) + len(endToken) 
    return data[begin:end]

def list(dir=DEFAULT_PROVPROF_DIR):
    for f in os.listdir(dir):
        if isProvFile(f):
            print f

def path(name, path=DEFAULT_PROVPROF_DIR):
    for f in os.listdir(path):
        if isProvFile(f):
            filePath = os.path.join(path, f)
            plistString = plistStringFromProvFile(filePath)
            plist = plistlib.readPlistFromString(plistString)
            if plist['Name'] == name:
                print filePath
           
COMMANDS = ('list', 'path')

def usage(command=None):
    print """
usage: provtool <subcommand>

Available subcommands are:
    list    List installed Provisiong Profiles.
    path    Get the path of a Provisioning Profile by name.
"""

def main():
    if len(sys.argv) == 1:
        usage()
        exit(1)
   
    command = sys.argv[1]
    if command not in COMMANDS:
        usage()
    elif command == 'list':
        list()
    elif command == 'path':
        if len(sys.argv) < 2:
            usage(command)
            exit(1)
        else:
            path(sys.argv[2])

if __name__ == "__main__":
    main()
