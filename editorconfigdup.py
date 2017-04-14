import argparse
import os
import sys

__author__ = 'egr'


def main():
    parser = argparse.ArgumentParser(description='Editorconfig duplication finder')
    parser.add_argument('-p', '--path', dest='path', help='path to editorconfig file')

    args = parser.parse_args()

    if args.path is None or not os.path.exists(args.path):
        print 'File not found'
        return

    ix = 0
    options_map = {}
    with open(args.path, "r") as f:
        line = f.readline()
        while line is not None and line.__len__() > 0:
            ix += 1
            parts = line.split('=')
            if parts.__len__() == 2:
                key = parts[0].strip()
                if key not in options_map:
                    options_map[key] = [str(ix)]
                else:
                    options_map[key].append(str(ix))
            line = f.readline()

    for pair in options_map:
        if options_map[pair].__len__() > 1:
            print pair + ': ' + ', '.join(options_map[pair])


if __name__ == '__main__':
    sys.exit(main())
