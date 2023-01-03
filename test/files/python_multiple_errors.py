# RUN: /usr/bin/python3 %s
import sys

sys.stdout.write("foo\n")
# CHECK: foo
sys.stdout.write("one\n")
# CHECK: eins
sys.stdout.write("two\n")
# CHECK: zwei
sys.stdout.write("bar\n")
# CHECK: bar
