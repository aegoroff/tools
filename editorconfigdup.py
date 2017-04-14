import argparse
import sys

__author__ = 'egr'


def main():
    parser = argparse.ArgumentParser(description='Editorconfig duplication finder')
    parser.add_argument('-p', '--path', dest='path', help='path to editorconfig file')

    args = parser.parse_args()

    ix = 0
    duplicates = {}
    with open(args.path, "r") as f:
        line = f.readline()
        while line is not None and line.__len__() > 0:
            ix += 1
            parts = line.split('=')
            if parts.__len__() == 2:
                key = parts[0]
                if key not in duplicates:
                    duplicates[parts[0]] = [str(ix)]
                else:
                    duplicates[parts[0]].append(str(ix))
            line = f.readline()

    for pair in duplicates:
        if duplicates[pair].__len__() > 1:
            print pair + ': ' + ', '.join(duplicates[pair])


if __name__ == '__main__':
    sys.exit(main())
