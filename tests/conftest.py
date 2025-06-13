import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import Mock

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_file_object():
    """Create a mock file object that simulates ranger's file objects."""
    def _create_mock(path, is_directory=False, extension=None):
        mock = Mock()
        mock.path = path
        mock.is_directory = is_directory
        mock.relative_path = os.path.basename(path)
        
        if extension:
            mock.extension = extension
        elif not is_directory and '.' in os.path.basename(path):
            mock.extension = os.path.splitext(path)[1]
        else:
            mock.extension = ''
        
        return mock
    
    return _create_mock


@pytest.fixture
def mock_ranger_context():
    """Create a mock ranger context for testing linemode."""
    context = Mock()
    context.separator = ' '
    return context


@pytest.fixture
def sample_files(temp_dir):
    """Create sample files for testing."""
    files = {
        'test.py': 'print("Hello, World!")',
        'README.md': '# Test Project',
        '.gitignore': '*.pyc\n__pycache__/',
        'package.json': '{"name": "test"}',
        'Dockerfile': 'FROM python:3.9',
        'Makefile': 'test:\n\tpytest',
        'test.jpg': b'fake image data',
        'document.pdf': b'fake pdf data',
    }
    
    created_files = {}
    for filename, content in files.items():
        file_path = temp_dir / filename
        if isinstance(content, bytes):
            file_path.write_bytes(content)
        else:
            file_path.write_text(content)
        created_files[filename] = file_path
    
    return created_files


@pytest.fixture
def sample_directories(temp_dir):
    """Create sample directories for testing."""
    directories = [
        'Downloads',
        'Documents',
        'Pictures',
        'Music',
        'Videos',
        '.git',
        'node_modules',
        '__pycache__',
        'test_dir',
        'src',
    ]
    
    created_dirs = {}
    for dirname in directories:
        dir_path = temp_dir / dirname
        dir_path.mkdir()
        created_dirs[dirname] = dir_path
    
    return created_dirs


@pytest.fixture
def mock_environment(monkeypatch):
    """Fixture to safely mock environment variables."""
    def _set_env(**kwargs):
        for key, value in kwargs.items():
            if value is None:
                monkeypatch.delenv(key, raising=False)
            else:
                monkeypatch.setenv(key, value)
    
    return _set_env


@pytest.fixture
def mock_xdg_dirs(mock_environment):
    """Mock XDG user directories."""
    xdg_dirs = {
        'XDG_DOCUMENTS_DIR': '/home/user/Documents',
        'XDG_DOWNLOADS_DIR': '/home/user/Downloads',
        'XDG_TEMPLATES_DIR': '/home/user/Templates',
        'XDG_PUBLICSHARE_DIR': '/home/user/Public',
        'XDG_MUSIC_DIR': '/home/user/Music',
        'XDG_PICTURES_DIR': '/home/user/Pictures',
        'XDG_VIDEOS_DIR': '/home/user/Videos',
    }
    mock_environment(**xdg_dirs)
    return xdg_dirs


@pytest.fixture
def devicons_instance():
    """Create an instance of DevIconsLinemode for testing."""
    from __init__ import DevIconsLinemode
    return DevIconsLinemode()


@pytest.fixture(autouse=True)
def reset_imports():
    """Reset module imports between tests to ensure clean state."""
    modules_to_remove = [
        'devicons',
        'locales',
        'locales.de',
        'locales.es',
        'locales.fr',
        'locales.it',
        'locales.ja',
        'locales.pt_BR',
        'locales.ru',
        'locales.zh_cn',
    ]
    
    for module in modules_to_remove:
        if module in sys.modules:
            del sys.modules[module]
    
    yield


@pytest.fixture
def capture_logs():
    """Capture log messages during tests."""
    import logging
    from io import StringIO
    
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    handler.setLevel(logging.DEBUG)
    
    logger = logging.getLogger()
    original_level = logger.level
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    yield log_capture
    
    logger.removeHandler(handler)
    logger.setLevel(original_level)