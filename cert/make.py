__author__ = 'egr'

import sys
import argparse
import execute
import os.path

def main():
    parser = argparse.ArgumentParser(description='Making test self signed test certificate')
    parser.add_argument('-p', '--password', required=True,  dest='password', help='Certificate password')
    parser.add_argument('-c', '--company', required=True, dest='company', help='Company name')
    parser.add_argument('-o', '--output', required=True, dest='output', help='Output file name')
    parser.add_argument('-t', '--toolpath', dest='toolpath', help='Path to Windows SDK certificate management tools',
                      default='')
    args = parser.parse_args()


    exc = execute.Execute()

    cerFile = '{0}.cer'.format(args.output)
    spcFile = '{0}.spc'.format(args.output)
    pvkFile = '{0}.pvk'.format(args.output)
    pfxFile = '{0}.pfx'.format(args.output)
    exc.runProc([os.path.join(args.toolpath, 'makecert.exe') , "-r", '-pe', '-sv', pvkFile, '-n', 'CN={0}'.format(args.company), cerFile])
    exc.runProc([os.path.join(args.toolpath, 'cert2spc.exe'), cerFile, spcFile])
    exc.runProc([os.path.join(args.toolpath, 'pvk2pfx.exe'), '-pvk', pvkFile, '-pi', args.password, '-spc', spcFile, '-pfx', pfxFile, '-po',
                 args.password])

    return 0

if __name__ == '__main__':
    sys.exit(main())