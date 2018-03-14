import logging
import argparse
import sys
import os
import shutil

__author__ = 'egr'


def main():
    logging.basicConfig(format="%(asctime).19s %(levelname)s %(message)s ")
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description='Mirror copier')
    parser.add_argument('-b', '--base', dest='base_path', help='Base path')
    parser.add_argument('-s', '--source', dest='source_path', help='Source path')
    parser.add_argument('-t', '--target', dest='target_path', help='Target path')

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

    mirror(args.base_path, args.source_path, args.target_path)


def mirror(base_path, source_path, target_path):
    content = os.listdir(base_path)
    for item in content:
        src = os.path.join(source_path, item)
        if os.path.exists(src):
            if os.path.isdir(src):
                tgt = os.path.join(target_path, item)
                if not os.path.exists(tgt):
                    os.mkdir(tgt)
                mirror(os.path.join(base_path, item), src, tgt)
            else:
                shutil.copy(src, target_path)
                logging.info('copied to %s', os.path.join(target_path, item))
        else:
            logging.info('path %s not found in source', src)


if __name__ == '__main__':
    sys.exit(main())
