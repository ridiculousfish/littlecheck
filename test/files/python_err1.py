# RUN: /usr/bin/python %s

import sys

sys.stderr.write("ALPHA\n")
# CHECKERR: BETA

