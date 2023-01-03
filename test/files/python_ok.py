# RUN: /usr/bin/python3 %s

from __future__ import print_function

import sys

print("abc")
# CHECK: abc

print("%x" % (16 ** 3))
# CHECK: 1000

for i in range(3):
    print(i)
# CHECK: 0
# CHECK: 1
# CHECK: 2

print(str(3 ** 64))
# CHECK: {{\d+}}

if True:
    print("indented")
    # CHECK: indented
