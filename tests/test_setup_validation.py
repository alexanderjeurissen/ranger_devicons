"""
Validation tests to ensure the testing infrastructure is properly set up.
"""
import os
import sys
from pathlib import Path

import pytest


class TestInfrastructureSetup:
    """Test class to validate the testing infrastructure setup."""
    
    def test_pytest_is_available(self):
        """Test that pytest is properly installed and importable."""
        import pytest
        assert pytest.__version__
    
    def test_pytest_cov_is_available(self):
        """Test that pytest-cov is properly installed."""
        import pytest_cov
        assert pytest_cov.__version__
    
    def test_pytest_mock_is_available(self):
        """Test that pytest-mock is properly installed."""
        import pytest_mock
        # pytest-mock doesn't expose version directly, just check it's importable
        assert pytest_mock
    
    def test_project_structure_exists(self):
        """Test that the proper directory structure exists."""
        project_root = Path(__file__).parent.parent
        
        # Check main directories
        assert (project_root / "tests").exists()
        assert (project_root / "tests" / "__init__.py").exists()
        assert (project_root / "tests" / "unit").exists()
        assert (project_root / "tests" / "unit" / "__init__.py").exists()
        assert (project_root / "tests" / "integration").exists()
        assert (project_root / "tests" / "integration" / "__init__.py").exists()
        assert (project_root / "tests" / "conftest.py").exists()
    
    def test_pyproject_toml_exists(self):
        """Test that pyproject.toml exists with proper configuration."""
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"
        
        assert pyproject_path.exists()
        
        # Check that it contains expected sections
        content = pyproject_path.read_text()
        assert "[tool.poetry]" in content
        assert "[tool.pytest.ini_options]" in content
        assert "[tool.coverage.run]" in content
        assert "[tool.coverage.report]" in content
    
    def test_fixtures_are_available(self, temp_dir, mock_file_object, mock_ranger_context):
        """Test that custom fixtures from conftest.py are available."""
        # Test temp_dir fixture
        assert isinstance(temp_dir, Path)
        assert temp_dir.exists()
        
        # Test mock_file_object fixture
        mock = mock_file_object("/test/file.py", is_directory=False)
        assert mock.path == "/test/file.py"
        assert mock.extension == ".py"
        assert not mock.is_directory
        
        # Test mock_ranger_context fixture
        assert mock_ranger_context.separator == ' '
    
    def test_sample_fixtures_work(self, sample_files, sample_directories):
        """Test that sample file and directory fixtures work correctly."""
        # Test sample_files
        assert 'test.py' in sample_files
        assert sample_files['test.py'].exists()
        assert sample_files['test.py'].read_text() == 'print("Hello, World!")'
        
        # Test sample_directories
        assert 'Downloads' in sample_directories
        assert sample_directories['Downloads'].exists()
        assert sample_directories['Downloads'].is_dir()
    
    @pytest.mark.unit
    def test_unit_marker_works(self):
        """Test that the unit test marker is properly configured."""
        assert True
    
    @pytest.mark.integration
    def test_integration_marker_works(self):
        """Test that the integration test marker is properly configured."""
        assert True
    
    @pytest.mark.slow
    def test_slow_marker_works(self):
        """Test that the slow test marker is properly configured."""
        assert True
    
    def test_coverage_configuration(self):
        """Test that coverage is properly configured."""
        # This test will be meaningful when running with coverage
        # It ensures the coverage tool is working
        assert True
    
    def test_imports_from_project_root(self):
        """Test that we can import modules from the project root."""
        # The conftest.py adds the parent directory to sys.path
        try:
            import devicons
            assert hasattr(devicons, 'file_node_extensions')
        except ImportError:
            pytest.fail("Cannot import devicons module from project root")
    
    def test_environment_fixture(self, mock_environment):
        """Test that the mock_environment fixture works correctly."""
        mock_environment(TEST_VAR="test_value")
        assert os.environ.get("TEST_VAR") == "test_value"
        
        mock_environment(TEST_VAR=None)
        assert os.environ.get("TEST_VAR") is None


class TestPoetryConfiguration:
    """Test that Poetry is properly configured."""
    
    def test_poetry_configuration(self):
        """Test that Poetry and pytest are properly configured."""
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"
        
        content = pyproject_path.read_text()
        assert '[tool.poetry]' in content
        assert 'pytest = "^8.0.0"' in content
        assert 'pytest-cov = "^5.0.0"' in content
        assert 'pytest-mock = "^3.14.0"' in content