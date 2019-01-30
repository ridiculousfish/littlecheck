LICH_PATH := littlecheck/

.PHONY: test
test:
	python -m unittest discover test
	python3 -m unittest discover test
