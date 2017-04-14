import sys
import argparse
import execute
import os.path

__author__ = 'egr'


def main():
    parser = argparse.ArgumentParser(description='Making test self signed test certificate')
    parser.add_argument('-p', '--password', required=True, dest='password', help='Certificate password')
    parser.add_argument('-c', '--company', required=True, dest='company', help='Company name')
    parser.add_argument('-o', '--output', required=True, dest='output', help='Output file name')
    parser.add_argument('-t', '--toolpath', dest='toolpath', help='Path to Windows SDK certificate management tools',
                        default='')
    args = parser.parse_args()

    exc = execute.Execute()

    cer_file = '{0}.cer'.format(args.output)
    spc_file = '{0}.spc'.format(args.output)
    pvk_file = '{0}.pvk'.format(args.output)
    pfx_file = '{0}.pfx'.format(args.output)
    exc.run_proc(
        [os.path.join(args.toolpath, 'makecert.exe'), "-r", '-pe', '-sv', pvk_file, '-n', 'CN={0}'.format(args.company),
         cer_file])
    exc.run_proc([os.path.join(args.toolpath, 'cert2spc.exe'), cer_file, spc_file])
    exc.run_proc(
        [os.path.join(args.toolpath, 'pvk2pfx.exe'), '-pvk', pvk_file, '-pi', args.password, '-spc', spc_file, '-pfx',
         pfx_file, '-po',
         args.password])

    return 0


if __name__ == '__main__':
    sys.exit(main())
