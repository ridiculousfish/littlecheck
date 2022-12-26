# SPDX-FileCopyrightText: © 2019 ridiculousfish and littlecheck contributors
#
# SPDX-License-Identifier: CC0-1.0

# RUN: /usr/bin/python %s

import sys

sys.stderr.write("GAMMA1\n")
# CHECKERR: GAMMA1
sys.stderr.write("GAMMA2\n")
# CHECKERR: GAMMA2
sys.stderr.write("GAMMA3\n")
# CHECKERR: BETA
sys.stderr.write("GAMMA4\n")
# CHECKERR: GAMMA4
sys.stderr.write("GAMMA5\n")
# CHECKERR: GAMMA5
sys.stderr.write("GAMMA6\n")
# CHECKERR: GAMMA6
sys.stderr.write("GAMMA7\n")
# CHECKERR: GAMMA7
sys.stderr.write("GAMMA8\n")
# CHECKERR: GAMMA8
