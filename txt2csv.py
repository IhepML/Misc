# coding: utf-8

# Copyright (c) 2019 Gsllchb
#
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""A standalone CLI tool for converting the text files with the format like
following to standard CSV files.
************************************************************************
*    Row   * MC_hit_tu *  DT_layer *   DT_cell * MC_hit_ed *  DT_drift *
************************************************************************
*        4 *         1 *         0 *        26 * 0.4144734 * 0.8997096 *
*        4 *         1 *         0 *        27 * 1.8536646 * 0.2957060 *
...         ...         ...         ...         ...         ...
*    99992 *         1 *        10 *       154 * 1.6096700 * 0.7033778 *
************************************************************************
"""

__version__ = "0.1.0"


import argparse
import sys


ENCODING = "utf-8"


def run(*args) -> None:
    args = _parse_args(args)
    with open(args.input, encoding=ENCODING) as f:
        text = f.read()
    csv = convert(text)
    with open(args.output, mode="x", encoding=ENCODING) as f:
        f.write(csv)


def convert(text: str) -> str:
    text = text.replace(" ", "").replace("*\n*", "\n").replace("*", ",")
    lines = text.splitlines()
    del lines[-1]
    del lines[2]
    del lines[0]
    return "\n".join(lines)


def _parse_args(args) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "input",
        help="the path of input file"
    )
    parser.add_argument(
        "output",
        help="the path of output file"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
    )
    return parser.parse_args(args)


def main():
    run(*sys.argv[1:])


if __name__ == '__main__':
    main()
