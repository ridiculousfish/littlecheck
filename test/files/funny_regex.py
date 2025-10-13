#!/usr/bin/python3
import sys

print(r"0\{4\}")

# This is the regex \d{4
# Followed by a literal }
# We reject this, it's ambiguous.
# CHECK: {{\d{4}}}
