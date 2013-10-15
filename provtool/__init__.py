import os
import sys
import logging
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


def name(filePath):
    plistString = plistStringFromProvFile(filePath)
    plist = plistlib.readPlistFromString(plistString)
    return plist['Name']


def path(provName, path=DEFAULT_PROVPROF_DIR):
    for f in os.listdir(path):
        if isProvFile(f):
            filePath = os.path.join(path, f)
            if name(filePath) == provName:
                print filePath


def uuid(path):
    fullpath = os.path.expanduser(path)
    if not isProvFile(fullpath):
        err = '%s is not a Provisioning Profile' % (fullpath)
        #sys.stderr.write(err)
        raise ValueError(err)  # TODO: ValueError the right kind of exception?
        return
    plistString = plistStringFromProvFile(fullpath)
    plist = plistlib.readPlistFromString(plistString)
    print plist['UUID']


def list(dir=DEFAULT_PROVPROF_DIR):
    print "%s:" % dir
    for f in os.listdir(dir):
        if isProvFile(f):
            print "%s : '%s'" % (f, name(os.path.join(dir, f)))


COMMANDS = ('list', 'path', 'uuid')


def usage(command=None):
    print """
usage: provtool <subcommand>

Available subcommands are:
    list            List installed Provisioning Profiles.
    path <name>     Get the path(s) of Provisioning Profile by name.
    uuid <path>     Display the UDID of a Provisioning Profile by path.
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
    elif command == 'uuid':
        if len(sys.argv) < 2:
            usage(command)
            exit(1)
        else:
            uuid(sys.argv[2])


if __name__ == "__main__":
    main()
