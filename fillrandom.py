#!/usr/bin/env python
"""Copy random files form source to the destination"""
import logging
import os


def parseArgs():
    """Parse arguments from command line"""
    from argparse import ArgumentParser
    from sys import exit

    parser = ArgumentParser(
        description='Copy random files from source to destination')

    parser.add_argument('source',
                        help='source directory')
    parser.add_argument('destination',
                        help='destination directory')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='enable debug output')
    parser.add_argument('-e', '--extension', default='.mp3',
                        help='file extension filter (defaults to ".mp3")')
    parser.add_argument('-n', '--number', type=int,
                        help='limit the number of files to copy')
    parser.add_argument('-s', '--size', type=int,
                        help='limit the total size (in MB) to copy')

    args = parser.parse_args()

    if not os.path.exists(args.source):
        exit('Invalid source: {}'.format(args.source))

    if not os.path.exists(args.destination):
        exit('Invalid destination: {}'.format(args.destination))

    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
        logging.debug('Debugging enabled.')
    else:
        logging.basicConfig(level=logging.INFO, format='%(message)s')

    return args


def scan(directory, extension):
    """Scan directory and return a list of files with the desired extension"""
    files_list = []

    logging.info('Scanning source...')
    for (dir_path, dir_names, file_names) in os.walk(directory):
        if file_names:
            logging.debug('Scanning directory: {}'.format(dir_path))

        for file_name in file_names:
            if file_name.lower().endswith(extension):
                logging.debug('  Match, adding to list: {}'.format(file_name))
                files_list.append((dir_path, file_name))

    return files_list


def copy(files_list, destination, max_files=None, max_size=None):
    """Copy files from the list to the destination"""
    from random import SystemRandom
    from shutil import copy

    random = SystemRandom()
    total_files = 0
    total_size = 0

    logging.info('Copying files...')
    while True:
        source, file_name = random.choice(files_list)
        src_path = os.path.join(source, file_name)
        dst_path = os.path.join(destination, file_name)
        file_size = os.stat(src_path).st_size / 1024.0 / 1024.0

        logging.debug('  {} ({:.2f} MB)'
                      .format(file_name, file_size))

        if max_size:
            if total_size + file_size > max_size:
                logging.debug('    Maximum size reached ({} MB).'
                              .format(max_size))
                break

        if max_files:
            if total_files == max_files:
                logging.debug('    Number of files reached ({} files).'
                              .format(max_files))
                break

        try:
            copy(src_path, dst_path)

        except IOError, e:
            # No space left
            logging.debug('    {}'.format(e.strerror))
            logging.debug('  Removing file: {}'.format(dst_path))
            os.unlink(dst_path)
            break

        except KeyboardInterrupt:
            # User interruption
            logging.debug('    Keyboard interruption.')
            logging.debug('  Removing file: {}'.format(dst_path))
            os.unlink(dst_path)
            break

        else:
            # Increment the number of copied files
            total_files += 1

            # Increment the total data size copied
            total_size += file_size

    logging.info('Copied {} files ({:.2f} MB)'.format(total_files, total_size))


def run():
    args = parseArgs()
    files_list = scan(args.source, args.extension)

    limits = {}
    if args.number:
        limits['max_files'] = args.number
    if args.size:
        limits['max_size'] = args.size

    copy(files_list, args.destination, **limits)

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        pass
