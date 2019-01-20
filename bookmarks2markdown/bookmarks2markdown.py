# Copyright 2019 Nikola Trubitsyn. All rights reserved.
# Use of this source code is governed by the Apache 2.0
# license that can be found in the LICENSE file.

import argparse

import lxml.html


def main(*args, **kwargs):
    in_file = open(kwargs['in'], 'r')
    markdown = convert(in_file.read())
    in_file.close()

    out_file = open(kwargs['out'], 'w+')
    out_file.write(markdown)
    out_file.close()


def convert(doc: str):
    output = []
    html = lxml.html.fromstring(doc)

    for element in html.iter():
        res = fsm(element)
        if res:
            output.append(res)

    return '\n'.join(output)


def fsm(element: lxml.html.etree.Element):
    if element.tag == 'h1':
        return f'# {element.text}'
    if element.tag == 'h3':
        return f'## {element.text}'
    if element.tag == 'a':
        return f'* [{element.text}]({element.attrib["href"]})'


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
    main(**vars(argparser().parse_args()))
