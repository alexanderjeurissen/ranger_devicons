import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

def reload_devicons(lang):
    os.environ['DEVICONS_LANG'] = lang
    from ranger_devicons import devicons
    importlib.reload(devicons)
    return devicons

class MockFile:
    def __init__(self, path, is_directory=False):
        self.relative_path = path
        self.is_directory = is_directory
        self.extension = os.path.splitext(path)[1][1:]


def test_devicon_py_file():
    devicons = reload_devicons('es')
    file = MockFile('example.py')
    assert devicons.devicon(file) == ''


def test_devicon_readme():
    devicons = reload_devicons('es')
    file = MockFile('README.md')
    assert devicons.devicon(file) == ''


def test_devicon_directory_match():
    devicons = reload_devicons('es')
    file = MockFile('Documents', is_directory=True)
    assert devicons.devicon(file) == ''


@pytest.mark.parametrize("lang,translated,english", [
    ("es", "Descargas", "Downloads"),
    ("fr", "Téléchargements", "Downloads"),
    ("de", "Schreibtisch", "Desktop"),
    ("it", "Scaricati", "Downloads"),
    ("pt_BR", "Imagens", "Pictures"),
    ("ja", "ダウンロード", "Downloads"),
    ("ru", "Загрузки", "Downloads"),
    ("zh_cn", "下载", "Downloads"),
])
def test_devicon_directory_translation(lang, translated, english):
    devicons = reload_devicons(lang)
    english_file = MockFile(english, is_directory=True)
    translated_file = MockFile(translated, is_directory=True)
    assert devicons.devicon(translated_file) == devicons.devicon(english_file)


def test_devicon_unknown():
    devicons = reload_devicons('es')
    file = MockFile('unknown.unknown')
    assert devicons.devicon(file) == ''

def test_unmapped_directory_returns_default(monkeypatch):
    monkeypatch.setenv('XDG_DOWNLOAD_DIR', '/tmp/downloads')
    devicons = reload_devicons('es')
    file = MockFile('RandomDir', is_directory=True)
    assert devicons.devicon(file) == ''


def test_uncommon_extension_returns_default(monkeypatch):
    monkeypatch.setenv('XDG_DOWNLOAD_DIR', '/tmp/downloads')
    devicons = reload_devicons('es')
    file = MockFile('file.xyz')
    assert devicons.devicon(file) == ''

@pytest.mark.parametrize(
    "name,expected",
    [
        ("data.json", ""),
        ("image.png", ""),
        ("archive.tar", ""),
        ("Makefile", ""),
        ("Dockerfile", ""),
        ("package.json", ""),
    ],
)
def test_devicon_various_examples(name, expected):
    devicons = reload_devicons('es')
    assert devicons.devicon(MockFile(name)) == expected


def test_devicon_capitalized_extension_returns_default(monkeypatch):
    monkeypatch.setenv('XDG_DOWNLOAD_DIR', '/tmp/downloads')
    devicons = reload_devicons('es')
    file = MockFile('example.PY')
    assert devicons.devicon(file) == ''


def test_devicon_xdg_trailing_slash(monkeypatch):
    monkeypatch.setenv('XDG_PICTURES_DIR', '/tmp/Pictures/')
    devicons = reload_devicons('es')
    file = MockFile('Pictures', is_directory=True)
    assert devicons.devicon(file) == ''
