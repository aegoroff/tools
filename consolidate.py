import argparse
import json
import logging
import os
import sys
import shutil


__author__ = 'egorov'

_FILE_ENCODING = 'UTF-8'
_APP_CONFIG_PATH = 'consolidate.json'

'''
consolidate.json example:

{
    "folders": [
        "c:/f1",
        "c:/f2"
    ]
}

'''

def read_json(path):
    f = open(path)
    try:
        result = json.load(f, encoding=_FILE_ENCODING)
    finally:
        f.close()
    return result

def main():
    logging.basicConfig(format="%(asctime).19s %(levelname)s %(message)s ")
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description='Files consolidater')
    parser.add_argument('-t', '--target', dest='target_path', required=True, help='Target directory to copy all files')
    parser.add_argument('-c', '--config', dest='config', help='Config path', default=_APP_CONFIG_PATH)

    args = parser.parse_args()

    items = read_json(args.config)
    for folder in items['folders']:
        if not os.path.exists(folder):
            logging.warn('Unexist folder %s', folder)
            continue
        files = os.listdir(folder)
        for filename in files:
            src = os.path.join(folder, filename)
            shutil.copy(src, args.target_path)


if __name__ == '__main__':
    sys.exit(main())
