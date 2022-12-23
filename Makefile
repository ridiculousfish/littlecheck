LICH_PATH := littlecheck/

.PHONY: test
test:
	LC_ALL=C python3 -m unittest discover test
