import argparse
import cookielib
import json
import logging
import os
import sys
import urllib2

__author__ = 'egorov'

_FILE_ENCODING = 'UTF-8'
_APP_CONFIG_PATH = 'config.json'


def writefile(path, data, mode):
    if path == '':
        return
    f = open(path, mode)
    try:
        f.write(data)
    finally:
        f.close()


def read_json(path):
    f = open(path)
    try:
        result = json.load(f, encoding=_FILE_ENCODING)
    finally:
        f.close()
    return result


def download(p, target, base_path):
    directory = base_path + '/' + target
    if not os.path.exists(directory):
        os.makedirs(directory)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    try:
        resp = opener.open(p)
        remove_punctuation_map = dict((ord(char), None) for char in u'/:')
        fn = p.translate(remove_punctuation_map)[4:]
        td = directory + '/' + fn
        writefile(td, resp.read(), 'wb')
        logging.info('saved to %s', td)
    except urllib2.URLError as ex:
        logging.exception(ex)
    finally:
        opener.close()


def main():
    logging.basicConfig(format=("%(asctime).19s %(levelname)s %(message)s "))
    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser(description='Files downloader')
    parser.add_argument('-b', '--base', dest='base_path', help='Base path to results', default='result')
    parser.add_argument('-c', '--config', dest='config', help='Download config path', default=_APP_CONFIG_PATH)

    args = parser.parse_args()

    items = read_json(args.config)
    for item in items:
        for f in items[item]:
            logging.info(' Downloading %s ...', f)
            download(f, item, args.base_path)

if __name__ == '__main__':
    sys.exit(main())