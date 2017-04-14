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
    duplicates = {}
    with open(args.path, "r") as f:
        line = f.readline()
        while line is not None and line.__len__() > 0:
            ix += 1
            parts = line.split('=')
            if parts.__len__() == 2:
                key = parts[0].strip()
                if key not in duplicates:
                    duplicates[key] = [str(ix)]
                else:
                    duplicates[key].append(str(ix))
            line = f.readline()

    for pair in duplicates:
        if duplicates[pair].__len__() > 1:
            print pair + ': ' + ', '.join(duplicates[pair])


if __name__ == '__main__':
    sys.exit(main())
