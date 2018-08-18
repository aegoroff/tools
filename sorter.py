import logging
import argparse
import sys
import os
import shutil
from datetime import datetime

__author__ = 'egr'


def main():
    logging.basicConfig(format="%(asctime).19s %(levelname)s %(message)s ")
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description='Files sorter by dates')
    parser.add_argument('-b', '--path', dest='path', help='Files folder path')

    args = parser.parse_args()

    if not os.path.exists(args.path):
        logging.error('Unexist path %s ...', args.path)
        return

    mirror(args.path)


def mirror(path):
    content = os.listdir(path)
    for item in content:
        src = os.path.join(path, item)
        created = datetime.fromtimestamp(os.path.getctime(src))
        destination = os.path.join(path, '{}'.format(created.date()))
        if not os.path.exists(destination):
            os.mkdir(destination)
        shutil.move(src, os.path.join(destination, item))



if __name__ == '__main__':
    sys.exit(main())