# RUN: /usr/bin/python3 %s
import sys
sys.stdout.write("\x1B[33mFOO\n")
# CHECK: banana
