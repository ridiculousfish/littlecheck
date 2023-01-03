# RUN: /usr/bin/python3 %s

import sys

sys.stderr.write("ALPHA\n")
# CHECKERR: BETA

# Some superfluous output so we can test --after.
sys.stderr.write("GAMMA1\n")
sys.stderr.write("GAMMA2\n")
sys.stderr.write("GAMMA3\n")
sys.stderr.write("GAMMA4\n")
sys.stderr.write("GAMMA5\n")
sys.stderr.write("GAMMA6\n")
sys.stderr.write("GAMMA7\n")
sys.stderr.write("GAMMA8\n")
