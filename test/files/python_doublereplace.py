#!/usr/bin/python
#
# This file causes SequenceMatcher to return a "replace" from the failing "0" line *including the next line*,
# even tho they are the same!

# I'm not *entirely* sure why this happens, but we have a workaround.
import sys

sys.stdout.write("Checking that --quiet quits early - if this is broken it hangs\n")
# CHECK: Checking that --quiet quits early - if this is broken it hangs
sys.stdout.write("0\n")
# CHECK: 0
sys.stdout.write("2\n")
# CHECK: 0
# These would be given as "does not match CHECK"
sys.stdout.write("0\n")
# CHECK: 0
sys.stdout.write("0\n")
# CHECK: 0
