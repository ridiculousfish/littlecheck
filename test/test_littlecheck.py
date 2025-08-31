import unittest
import io
import os.path

import littlecheck


class LittlecheckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Switch to test/files directory."""
        test_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(os.path.join(test_dir, "files"))
        os.environ["LANG"] = "C"

    def do_1_path_test(self, name, skip=False):
        """Run a single test. The name is the test name.
        The input file is the name with .py extension, the expected
        output of littlecheck is the name with .expected extension.
        """
        test_path = name + ".py" if not "." in name else name
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
            if skip:
                self.assertEqual(success, littlecheck.SKIP)
            else:
                self.assertEqual(success, expect_success)

    def test_py_ok(self):
        self.do_1_path_test("python_ok")

    def test_py_err1(self):
        self.do_1_path_test("python_err1")

    def test_py_middle_error(self):
        self.do_1_path_test("python_middle_error")

    def test_py_missing_output(self):
        self.do_1_path_test("python_missing_output")

    def test_py_multiple_error_output(self):
        self.do_1_path_test("python_multiple_error_annotation_lines")

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

    def test_skip(self):
        self.do_1_path_test("skip", skip=True)

    def test_require_succeeds(self):
        self.do_1_path_test("no_skip", skip=False)

    def test_space_replacement(self):
        test_path = "run_spaces.py"
        subs = {"%": "%", "s": test_path, "arg": "arg with spaces"}
        conf = littlecheck.Config()
        failures = []
        success = littlecheck.check_path(test_path, subs, conf, failures.append)
        self.assertEqual(success, True)
        self.assertEqual(len(failures), 0)

    def test_exe_found(self):
        # We only want to know that we don't get a CheckerError,
        # the actual error message here is platform-dependent.
        test_path = "exe_found.py"
        subs = {"%": "%", "s": test_path}
        conf = littlecheck.Config()
        failures = []
        success = littlecheck.check_path(test_path, subs, conf, failures.append)
        self.assertEqual(success, False)
        self.assertEqual(len(failures), 1)
        self.assertEqual(
            isinstance(failures[0], littlecheck.littlecheck.TestFailure), True
        )

    def test_exe_not_found(self):
        try:
            self.do_1_path_test("exe_not_found")
        except littlecheck.CheckerError:
            return
        raise Exception

    def test_sigkill(self):
        self.do_1_path_test("sigkill.sh")

    def test_sigint(self):
        self.do_1_path_test("sigint.sh")

    def test_int(self):
        self.do_1_path_test("int.sh")

    def test_sig2(self):
        self.do_1_path_test("sig2.sh")

    def test_exit_42(self):
        self.do_1_path_test("exit_42.sh")

    def test_exit_unexpected_0(self):
        self.do_1_path_test("exit_unexpected_0.sh")

    def test_exit_unexpected_multiple_expected(self):
        self.do_1_path_test("exit_unexpected_multiple_expected.sh")
