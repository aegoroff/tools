import logging
import argparse
import sys
import os
import shutil

__author__ = 'egr'


def main():
    logging.basicConfig(format=("%(asctime).19s %(levelname)s %(message)s "))
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description='APR lib build results distributive automation tool')
    parser.add_argument('-t', '--target', dest='target_path', help='Target base path', default='BIN')

    args = parser.parse_args()

    if not os.path.exists(args.target_path):
        logging.info('Unexist target %s create new one', args.target_path)
        os.makedirs(args.target_path)

    libdirs = ['apr', 'apr-util']
    arch = ['x86', 'x64']
    libs = ['apr-1.lib', 'aprutil-1.lib']
    configurations = ['Debug', 'Release']

    mapping = {}

    for d in libdirs:
        for a in arch:
            mapping[d + '-' + a] = os.path.join(d, a)

    copy_map = {}

    for src in mapping:
        for conf in configurations:
            src_dir = os.path.join(src, conf)
            target_dir = os.path.join(args.target_path, mapping[src], conf)
            if not os.path.exists(target_dir):
                logging.info('Unexist target %s create new one', target_dir)
                os.makedirs(target_dir)
            for lib in libs:
                src_fullpath = os.path.join(src_dir, lib)
                copy_map[src_fullpath] = target_dir

    for source_file in copy_map:
        if os.path.exists(source_file):
            logging.info('copy file: %s', source_file)
            shutil.copy(source_file, copy_map[source_file])

if __name__ == '__main__':
    sys.exit(main())
