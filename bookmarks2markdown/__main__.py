# Copyright 2019 Nikola Trubitsyn. All rights reserved.
# Use of this source code is governed by the Apache 2.0
# license that can be found in the LICENSE file.

import argparse

from NetscapeBookmarksFileParser import *
from NetscapeBookmarksFileParser import parser


def main():
    args = vars(argparser().parse_args())

    with open(args['in'], 'r') as in_file:
        markdown = convert(in_file.read())

    with open(args['out'], 'w+') as out_file:
        out_file.write(markdown)


def convert(doc: str):
    output = []

    bookmarks = NetscapeBookmarksFile(doc).parse()

    output.append('# {}'.format(bookmarks.title))

    output += fsm(bookmarks.bookmarks)

    return '\n'.join(output)


def fsm(folder: BookmarkItem, level=2):
    output = []

    for i in folder.items:
        if isinstance(i, BookmarkFolder):
            output.append('{} {}'.format('#' * level, i.name))
            output += fsm(i, level + 1)
        else:  # i.e. BookmarkShortcut
            output.append('- [{}]({})'.format(i.name, i.href))

    return output

def argparser():
    parser = argparse.ArgumentParser(
        description='Convert bookmarks to Markdown',
        add_help=True
    )
    parser.add_argument(
        '--in',
        type=str,
        default='bookmarks.html',
        help='HTML bookmarks file (default: bookmarks.html)'
    )
    parser.add_argument(
        '--out',
        type=str,
        default='bookmarks.md',
        help='output file (default: bookmarks.md)'
    )
    return parser


if __name__ == '__main__':
    main()
