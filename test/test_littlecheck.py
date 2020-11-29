import unittest
import io
import os.path
import tempfile

import littlecheck


class LittlecheckTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """ Switch to test/files directory. """
        test_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(os.path.join(test_dir, "files"))

    def do_1_path_test(self, name):
        """ Run a single test. The name is the test name.
           The input file is the name with .py extension, the expected
           output of littlecheck is the name with .expected extension.
        """
        test_path = name + ".py"
        expected_output_path = name + ".expected"
        subs = {"%": "%", "s": test_path}
        conf = littlecheck.Config()
        failures = []
        success = littlecheck.check_path(test_path, subs, conf, failures.append)
        failures_message = "\n".join([f.message() for f in failures]).strip()
        with io.open(expected_output_path, "r", encoding="utf-8") as fd:
            expect_text = fd.read().strip()
            expect_success = not expect_text
            self.assertEqual(failures_message, expect_text)
            self.assertEqual(success, expect_success)

    def test_py_ok(self):
        self.do_1_path_test("python_ok")

    def test_py_err1(self):
        self.do_1_path_test("python_err1")

    def test_py_middle_error(self):
        self.do_1_path_test("python_middle_error")

    def test_py_missing_output(self):
        self.do_1_path_test("python_missing_output")

    def test_py_multiple_errour_output(self):
        self.do_1_path_test("python_multipe_error_annotation_lines")

    def test_py_extra_output(self):
        self.do_1_path_test("python_extra_output")

    def test_py_out_vs_err(self):
        self.do_1_path_test("python_out_vs_err")

    def test_py_path(self):
        self.do_1_path_test("python_path_cmd")

    def test_py_shebang(self):
        self.do_1_path_test("python_shebang")

    def test_py_color(self):
        self.do_1_path_test("python_color")

    def test_inline_check(self):
        self.do_1_path_test("inline-check")

    def test_py_whitespace(self):
        self.do_1_path_test("python_whitespace")

    def test_py_replace(self):
        self.do_1_path_test("python_doublereplace")
