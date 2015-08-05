import logging
import argparse
import sys
import os
import shutil

__author__ = 'egr'


def main():
    logging.basicConfig(format=("%(asctime).19s %(levelname)s %(message)s "))
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description='Mirror copier')
    parser.add_argument('-b', '--base', dest='base_path', help='Base path')
    parser.add_argument('-s', '--source', dest='source_path', help='Source path')
    parser.add_argument('-t', '--target', dest='target_path', help='Source path')

    args = parser.parse_args()

    if not os.path.exists(args.base_path):
        logging.error('Unexist base %s ...', args.base_path)
        return

    if not os.path.exists(args.source_path):
        logging.error('Unexist source %s ', args.source_path)
        return

    if not os.path.exists(args.target_path):
        logging.error('Unexist target %s ', args.target_path)
        return

    files = os.listdir(args.base_path)
    for filename in files:
        src = os.path.join(args.source_path, filename)
        if os.path.exists(args.base_path):
            logging.info('found file: %s', src)
            shutil.copy(src, args.target_path)
        else:
            logging.info('file %s not found ', src)


if __name__ == '__main__':
    sys.exit(main())
