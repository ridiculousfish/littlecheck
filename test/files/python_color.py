# RUN: /usr/bin/python %s
import sys
sys.stdout.write("\x1B[33mFOO\n")
# CHECK: banana
