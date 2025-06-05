import os
import sys
import importlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from ranger_devicons.locales import fr
from ranger_devicons import devicons


def test_load_translations_and_translate(monkeypatch):
    monkeypatch.setenv('DEVICONS_LANG', 'fr')
    importlib.reload(devicons)

    translations = devicons.load_translations()
    assert translations == fr.translations

    assert devicons.translate_dir_name('Téléchargements') == 'Downloads'
    assert devicons.translate_dir_name('UnknownDir') == 'UnknownDir'


def test_load_translations_unknown(monkeypatch):
    monkeypatch.delenv('DEVICONS_LANG', raising=False)
    assert devicons.load_translations('unknown') == {}


def test_locale_used_when_env_unset(monkeypatch):
    """Translations fall back to the system locale when DEVICONS_LANG is unset."""
    monkeypatch.delenv('DEVICONS_LANG', raising=False)
    monkeypatch.setattr('locale.getdefaultlocale', lambda: ('fr_FR', 'UTF-8'))

    importlib.reload(devicons)

    assert devicons.dir_name_translations == fr.translations
    assert devicons.load_translations() == fr.translations
