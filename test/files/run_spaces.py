#RUN: /usr/bin/python %s %arg

import sys

print(sys.argv[1:])
#CHECK: ['arg with spaces']


