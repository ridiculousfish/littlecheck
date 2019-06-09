# littlecheck - command line tool tester

littlecheck is a tool for testing command line tools. It is heavily inspired by the [lit](http://llvm.org/docs/CommandGuide/lit.html) and [FileCheck](https://www.llvm.org/docs/CommandGuide/FileCheck.html) combo. littlecheck is much simpler, and has no dependencies except Python (2.7 or 3).

littlecheck is aimed at programs which process a text file and produce output on stdout and/or stderr. A test file is processed by littlecheck, which reads special directives embedded in comments. The same file is processed by the tool under test, which ignores the comments. littlecheck then verifies the tool's output according to the directives.

# Basic Example

An example test for the Python interpreter:

```python
# RUN: /usr/bin/python %s

print("abc")
# CHECK: abc

print("%x"%(16**3))
# CHECK: 1000

for i in range(3):
    print(i)
# CHECK: 0
# CHECK: 1
# CHECK: 2
```

To run this:

    ./littlecheck/littlecheck.py test.py

littlecheck will parse out the special comments `# RUN` and `# CHECK`:

- `# RUN` specifies an arbitary shell command. `%s` is substituted with the path to the input file. 
- `# CHECK` specifies an expected output line. littlecheck verifies that the output of the shell command matches the sequence of `CHECK` lines.

# Advanced Usage

littlecheck supports regular expressions, using Python's re syntax. Regular expressions are embedded in CHECK lines enclosed in double curly braces.

```python
# RUN: /usr/bin/python %s
print("A big number: ", 2**64)
# CHECK: A big number: {{\d+L}}
```

littlecheck also captures both stdout and stderr:

```ruby
# RUN: /usr/bin/ruby %s
$stdout.puts "this goes to stdout"
$stderr.puts "this goes to stderr"

# CHECK: this goes to stdout
# CHECKERR: this goes to stderr
```

# Tests

Run `make test` to run the tests.

# Limitations

- littlecheck currently only supports `#` comments. Other commenting styles would be straightforward to add.
- littlecheck does not yet support the rich set of substitutions of `lit`, only `%s` and `%%`.
- littlecheck does not support the `CHECK` and `CHECK-NEXT` distinction. All lines are expected to be present, except that empty output lines are ignored.
- littlecheck permits leading whitespace on matching lines and does not yet support something like the `--strict-whitespace` option to FileCheck.

# License

littlecheck is released into the public domain. You may use it for any purpose without attribution, or under the [CC0](https://creativecommons.org/publicdomain/zero/1.0/) license if public domain is not available.
