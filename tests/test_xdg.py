import os
import sys
import importlib

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


def reload_devicons():
    from ranger_devicons import devicons
    importlib.reload(devicons)
    return devicons


def test_xdg_music_dir(monkeypatch):
    monkeypatch.setenv("XDG_MUSIC_DIR", "/home/user/Music")
    monkeypatch.setenv("XDG_UNKNOWN_DIR", "/home/user/Unknown")

    devicons = reload_devicons()

    assert devicons.dir_node_exact_matches.get("Music") == ""
    assert "Unknown" not in devicons.dir_node_exact_matches
