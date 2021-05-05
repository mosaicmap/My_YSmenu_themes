#!/bin/python3
"""
Converts color in HTML format (#RRGGBB) (RGB24) to BGR15 in haxadecimal
format 0xXXXX (Binary: Abbbbbgggggrrrrr, where A=1)

Martin Pokorný, 2020
"""

import argparse
import os
import sys
import math
import logging

__version__ = '0.2 (2021-05-05)'
__author__ = 'Martin Pokorný'

logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    #level=logging.DEBUG,
                    format='{line:%(lineno)d} %(levelname)s: %(message)s')
log = logging.getLogger(os.path.basename(__file__))


def convert_html_rgb_to_bgr15(html_c: str):
    """
    Converts color in HTML format (#RRGGBB) (RGB24) to BGR15 in haxadecimal
    format 0xXXXX (Binary: Abbbbbgggggrrrrr, where A=1)

    :param html_c:  color in HTML format (#RRGGBB)
    :return:  BGR15 in haxadecimal format 0xXXXX
    
    >>> convert_html_rgb_to_bgr15("FF0088")
    '0xC41F'
    >>> convert_html_rgb_to_bgr15("#FF0088")
    '0xC41F'
    """
    html_c = html_c.lstrip("#")
    log.debug(f"{html_c}")

    # rgb 8 bit values to 5 bit values ...
    r = int(html_c[0:2], 16) >> 3
    g = int(html_c[2:4], 16) >> 3
    b = int(html_c[4:6], 16) >> 3
    log.debug(f"r:{r}, g:{g}, b:{b}")
    log.debug(f"r:{r:05b}, g:{g:05b}, b:{b:05b}")

    # Binary: Abbbbbgggggrrrrr, where A=1
    result = f"1{b:05b}{g:05b}{r:05b}"
    log.debug(f"bgr15: {result}")

    # 0xXXXX
    result = int(result, 2)
    result = f"0x{result:04X}"
    log.debug(f"result: {result}")

    return result


def define_and_parse_args():
    parser = argparse.ArgumentParser(
        description='Converts color in HTML format (#RRGGBB) (RGB24) to BGR15 \
                in haxadecimal format 0xXXXX (Binary: Abbbbbgggggrrrrr, where A=1)')
    parser.add_argument('-v', '--version', action='version',
                        version=__version__,
                        help='print program version and exit')
    parser.add_argument('color', action="store",
                        help='color in HTML format #RRGGBB or RRGGBB')
    args = parser.parse_args()
    return args


def handle_args(args):
    if args.color:
        try:
            html_c = args.color           
            bgr15_c = convert_html_rgb_to_bgr15(html_c)
            print(f"{html_c} -> {bgr15_c}")
        except Exception as ex:
            log.error("{}: {}".format(type(ex).__name__, ex))


def main():
    args = define_and_parse_args()
    handle_args(args)


def _test():
    import doctest  
    doctest.testmod()  


if __name__ == '__main__':
    #_test()
    main()
