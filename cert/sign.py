__author__ = 'egr'

import argparse
import execute
import sys
import os.path

def main():
    parser = argparse.ArgumentParser(description='Signing file using certificate specified')
    parser.add_argument('-p', '--password', required=True, dest='password', help='Certificate password')
    parser.add_argument('-x', '--pfx', required=True, dest='pfx', help='Pfx certificate')
    parser.add_argument('-f', '--file', required=True, dest='target', help='Target file to sign')
    parser.add_argument('-s', '--timestamp', dest='timestamp', help='Target file to sign',
                      default='http://timestamp.verisign.com/scripts/timstamp.dll')
    parser.add_argument('-t', '--toolpath', dest='toolpath', help='Path to Windows SDK sign tools', default='')
    args = parser.parse_args()

    exc = execute.Execute()

    exc.runProc([os.path.join(args.toolpath, 'signtool.exe'), 'sign', '/f', args.pfx, '/p', args.password, '/t', args.timestamp, '/v',
                 args.target])

    return 0

if __name__ == '__main__':
    sys.exit(main())