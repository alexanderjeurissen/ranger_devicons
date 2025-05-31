import os
import importlib.util
import pathlib
import pytest

spec = importlib.util.spec_from_file_location(
    "devicons",
    pathlib.Path(__file__).resolve().parents[1] / "devicons.py",
)
devicons = importlib.util.module_from_spec(spec)
spec.loader.exec_module(devicons)

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
