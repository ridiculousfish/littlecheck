#!/bin/sh

# ignore checks that look commented

# # CHECK: don't check me

# echo commented inline check # CHECK: not checked either

# but allow inline checks, if the first character of the line is not #
echo ok # CHECK: ok

echo mismatch # CHECK: match
