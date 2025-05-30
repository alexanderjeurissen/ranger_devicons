import os
import sys

# Ensure the package root is on the path
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from ranger_devicons.devicons import devicon, dir_node_exact_matches, file_node_extensions

class DummyFile:
    def __init__(self, path, is_directory=False):
        self.relative_path = path
        self.is_directory = is_directory
        base = os.path.basename(path)
        self.extension = base.split('.')[-1] if '.' in base else ''


def test_devicon_known_directory():
    file = DummyFile('Downloads', is_directory=True)
    expected = dir_node_exact_matches['Downloads']
    assert devicon(file) == expected


def test_devicon_known_extension():
    file = DummyFile('script.py')
    expected = file_node_extensions['py']
    assert devicon(file) == expected
