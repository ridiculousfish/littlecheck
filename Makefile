# SPDX-FileCopyrightText: © 2019 ridiculousfish and littlecheck contributors
#
# SPDX-License-Identifier: CC0-1.0

LICH_PATH := littlecheck/

.PHONY: test
test:
	LC_ALL=C python -m unittest discover test
	LC_ALL=C python3 -m unittest discover test
