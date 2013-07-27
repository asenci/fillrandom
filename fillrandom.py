#!/usr/bin/env python
"""Copy random files form source to the destination"""


def parseArgs():
    """Parse arguments from command line"""
    from argparse import ArgumentParser

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

    return parser.parse_args()


def run():
    import logging
    import os

    from random import SystemRandom
    from shutil import copy
    from sys import exit

    args = parseArgs()
    files_list = []
    random = SystemRandom()
    total_files = 0
    total_size = 0

    if not os.path.exists(args.source):
        exit('Invalid source: {}'.format(args.source))

    if not os.path.exists(args.destination):
        exit('Invalid destination: {}'.format(args.destination))

    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
        logging.debug('Debugging enabled.')
    else:
        logging.basicConfig(level=logging.INFO, format='%(message)s')

    logging.info('Scanning source...')
    for (dir_path, dir_names, file_names) in os.walk(args.source):
        if file_names:
            logging.debug('Scanning directory: {}'.format(dir_path))

        for file_name in file_names:
            if file_name.lower().endswith(args.extension):
                logging.debug('  Match, adding to list: {}'.format(file_name))
                files_list.append((
                    os.path.join(dir_path, file_name),
                    os.path.join(args.destination, file_name)
                ))

    logging.info('Copying files...')
    while True:
        next_file, dst_file = random.choice(files_list)
        next_size = os.stat(next_file).st_size / 1024.0 / 1024.0

        logging.debug('  {} ({:.2f} MB)'
                      .format(next_file, next_size))

        if args.size:
            if total_size + next_size > args.size:
                logging.debug('    Maximum size reached ({} MB).'
                              .format(args.size))
                break

        if args.number:
            if total_files == args.number:
                logging.debug('    Number of files reached ({} files).'
                              .format(args.number))
                break

        try:
            copy(next_file, dst_file)

        except IOError, e:
            # No space left
            logging.debug('    {}'.format(e.strerror))
            logging.debug('  Removing file: {}'.format(dst_file))
            os.unlink(dst_file)
            break

        except KeyboardInterrupt, e:
            # User interruption
            logging.debug('    Keyboard interruption.')
            logging.debug('  Removing file: {}'.format(dst_file))
            os.unlink(dst_file)
            break

        else:
            # Increment the number of copied files
            total_files += 1

            # Increment the total data size copied
            total_size += next_size

    logging.info('Copied {} files ({:.2f} MB)'.format(total_files, total_size))

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        pass
