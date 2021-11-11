import getopt
import sys

if __name__ == '__main__':
    print(sys.argv)
    argList = sys.argv[0].split('/')
    print(argList)
    del argList[-1]
    print(argList)
    rootPath = '/'.join(argList)
    print(rootPath)
