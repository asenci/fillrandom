# Copy random files from source to destination
This script was originally developed to randomly copy a bunch of music files to a pendrive.

The default options takes this into consideration:

  * ".mp3" extension filter
  * no file number or total size limit

## positional arguments:
source      | source directory
destination | destination directory

## optional arguments:
-h, --help                                   | show this help message and exit
-d, --debug                                  | enable debug output
-e **EXTENSION**, --extension **EXTENSION**  | file extension filter (defaults to ".mp3")
-n **NUMBER**, --number **NUMBER**           | limit the number of files to copy
-s **SIZE**, --size **SIZE**                 | limit the total size (in MB) to copy
