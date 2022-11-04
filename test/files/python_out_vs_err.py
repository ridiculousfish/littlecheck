# SPDX-FileCopyrightText: © 2019 ridiculousfish and littlecheck contributors
#
# SPDX-License-Identifier: CC0-1.0

# RUN: /usr/bin/python %s

# Test that error output is reported.
# Pretend that something fails and spews to stderr.
# Ensure littlecheck reports the error output, and doesn't just complain
# about broken stdout.

import sys

sys.stdout.write("fine so far\n")
# CHECK: fine so far

sys.stderr.write("something failed\n")
# That was unexpected.

sys.stdout.write("now stdout is broken\n")
# CHECK: things should be cool
