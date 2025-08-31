# RUN: /usr/bin/python3 %s

# Test that, if error output is reported,
# we get all the remaining lines, not just one.

import sys

sys.stderr.write("stderr1\n")
# CHECKERR: stderr1

sys.stdout.write("fine so far\n")
# CHECK: fine so far

sys.stdout.write("something failed\n")
# That was unexpected, and it would trigger more output on stderr.

sys.stderr.write("stderr2\n")
# CHECKERR: stderr2
sys.stderr.write("stderr3\n")
sys.stderr.write("stderr4\n")
sys.stderr.write("stderr5\n")

sys.stdout.write("now stdout is broken\n")
# CHECK: things should be cool
