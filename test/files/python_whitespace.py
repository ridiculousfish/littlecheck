#!/usr/bin/python3
import sys

sys.stdout.write("    one\n")
# CHECK: {{^}}    one

sys.stdout.write("    two\n")
# CHECK: two

sys.stdout.write("three\n")
# CHECK:     three

sys.stdout.write("   four\n")
# CHECK: {{^}} four
