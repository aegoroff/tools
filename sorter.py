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
    parser.add_argument('-p', '--path', dest='path', help='Files folder path')

    args = parser.parse_args()

    if not os.path.exists(args.path):
        logging.error('Unexist path %s ...', args.path)
        return

    sort_files_within_path(args.path)


def sort_files_within_path(path):
    for root, dirs, files in os.walk(path):
        for item in files:
            src = os.path.join(path, item)
            created = datetime.fromtimestamp(os.path.getctime(src))
            destination = os.path.join(path, '{}'.format(created.date()))
            if not os.path.exists(destination):
                os.mkdir(destination)
            shutil.move(src, os.path.join(destination, item))
        break



if __name__ == '__main__':
    sys.exit(main())