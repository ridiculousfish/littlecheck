# SPDX-FileCopyrightText: © 2020 ridiculousfish and littlecheck contributors
#
# SPDX-License-Identifier: CC0-1.0

# RUN: /usr/bin/python %s
import sys
sys.stdout.write("\x1B[33mFOO\n")
# CHECK: banana
