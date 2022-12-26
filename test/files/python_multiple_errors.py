# SPDX-FileCopyrightText: © 2020 ridiculousfish and littlecheck contributors
#
# SPDX-License-Identifier: CC0-1.0

# RUN: /usr/bin/python %s
import sys

sys.stdout.write("foo\n")
# CHECK: foo
sys.stdout.write("one\n")
# CHECK: eins
sys.stdout.write("two\n")
# CHECK: zwei
sys.stdout.write("bar\n")
# CHECK: bar
