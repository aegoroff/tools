import logging
import argparse
import sys
import os
import shutil

__author__ = 'egr'

INCLUDE = 'include'
X86 = 'x86'
X64 = 'x64'


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
    arch_names = [X86, X64]
    libs = ['apr-1.lib', 'aprutil-1.lib']
    configurations = ['Debug', 'Release']

    mapping = {}

    for lib_dir in libdirs:
        copy_includes(args.target_path, lib_dir)
        for arch in arch_names:
            mapping[create_lib_arch_root_path(arch, lib_dir)] = os.path.join(lib_dir, arch)

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


def create_lib_arch_root_path(arch, lib_dir):
    # key like <libdir>-<arch> i.e. apr-x64 etc.
    return lib_dir + '-' + arch


def copy_includes(target_path, lib_dir):
    src_include_dir = os.path.join(lib_dir, INCLUDE)
    target_include_dir = os.path.join(target_path, lib_dir, INCLUDE)
    if not os.path.exists(target_include_dir):
        shutil.copytree(src_include_dir, target_include_dir)
        include_content = os.walk(target_include_dir)
        for (dirpath, dirs, files) in include_content:
            common_prefix = os.path.commonprefix([target_include_dir, dirpath])
            trail = dirpath.replace(common_prefix, '').strip('\\')
            for header in files:
                if not header.endswith('.h'):
                    not_header_file = os.path.join(dirpath, header)
                    os.remove(not_header_file)
                    if header.endswith('.hw'):
                        hame = os.path.splitext(header)[0]
                        x86_dir = create_lib_arch_root_path(X86, lib_dir)
                        made_from_template = os.path.join(x86_dir, hame + '.h')
                        if os.path.exists(made_from_template):
                            template_target = os.path.join(target_include_dir, trail)
                            logging.info('copy template from %s to %s', made_from_template, template_target)
                            shutil.copy(made_from_template, template_target)

if __name__ == '__main__':
    sys.exit(main())
