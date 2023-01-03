# RUN: /usr/bin/python3 %s

import sys

print("First")
# CHECK: First

# CHECK: NotPrinted

print("Second")
# CHECK: Second
print("Third")
# CHECK: Third

print("1")
# CHECK: {{\d}}
print("2")
# CHECK: {{\d}}
print("3")
# CHECK: {{\d}}
print("4")
# CHECK: {{\d}}
print("5")
# CHECK: {{\d}}
print("6")
# CHECK: {{\d}}
print("6")
# CHECK: {{\d}}
print("foobar")
print("barbar")
# CHECK: {{barbar}}
print("6")
# CHECK: {{\d}}
print("6")
# CHECK: {{\d}}
print("6")
# CHECK: {{\d}}
print("6")
# CHECK: {{\d}}
print("6")
# CHECK: {{\d}}
print("6")
# CHECK: {{\d}}

print("Fourth")
