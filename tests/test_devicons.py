import os
import sys

import pytest

# Import the `devicons` module directly to avoid loading the `ranger` package
# which is not installed in the test environment.  The repository root is
# added to `sys.path` to allow importing the module as a top-level script.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import devicons

class MockFile:
    def __init__(self, path, is_directory=False):
        self.relative_path = path
        self.is_directory = is_directory
        self.extension = os.path.splitext(path)[1][1:]


def test_devicon_py_file():
    file = MockFile('example.py')
    assert devicons.devicon(file) == ''


def test_devicon_readme():
    file = MockFile('README.md')
    assert devicons.devicon(file) == ''


def test_devicon_directory_match():
    file = MockFile('Documents', is_directory=True)
    assert devicons.devicon(file) == ''


def test_devicon_unknown():
    file = MockFile('unknown.unknown')
    assert devicons.devicon(file) == ''
