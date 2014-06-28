# Copy random files from source to destination

This script was originally developed to randomly copy a bunch of music files to a pendrive.

The default options takes this into consideration:

  * ".mp3" extension filter
  * no file number or total size limit


## Usage:

fillrandom [-h] [-d] [-e **EXTENSION**] [-n **NUMBER**] [-s **SIZE**] source destination


### positional arguments:

Argument    | Description
:-----------|:---------------------
source      | source directory
destination | destination directory


### optional arguments:

Argument                                     | Description
:--------------------------------------------|:-------------------------------
-h, --help                                   | show this help message and exit
-d, --debug                                  | enable debug output
-e **EXTENSION**, --extension **EXTENSION**  | file extension filter (defaults to ".mp3")
-n **NUMBER**, --number **NUMBER**           | limit the number of files to copy
-r, --random                                 | insert random id on the destination file name
-s **SIZE**, --size **SIZE**                 | limit the total size (in MB) to copy


## Licensing:

Licensed under ISC license:

	Copyright (c) 2013 Andre Sencioles Vitorio Oliveira <andre@bcp.net.br>
	
	Permission to use, copy, modify, and distribute this software for any
	purpose with or without fee is hereby granted, provided that the above
	copyright notice and this permission notice appear in all copies.
	
	THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
	WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
	MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
	ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
	WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
	ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
	OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
