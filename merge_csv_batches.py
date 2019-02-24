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

"""A script for merging CSV batches"""

import pandas as pd

OUTPUT_PATH = "data.zip"
COMPRESSION = "zip"

BATCH_PATH_FMT = "batch{index}.csv"
START_INDEX = 0
END_INDEX = 10
assert START_INDEX < END_INDEX


def main():
    path = BATCH_PATH_FMT.format(index=START_INDEX)
    data = pd.read_csv(path)
    for i in range(START_INDEX + 1, END_INDEX):
        path = BATCH_PATH_FMT.format(index=i)
        data = data.append(pd.read_csv(path), ignore_index=True)
    data.to_csv(OUTPUT_PATH, index=False, compression=COMPRESSION)


if __name__ == '__main__':
    main()
