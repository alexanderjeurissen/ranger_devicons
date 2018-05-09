from distutils.core import setup
import os

# pylint: disable=import-error,no-name-in-module,ungrouped-imports
if os.environ.get('SETUPTOOLS_USE'):
  from setuptools import setup
  from setuptools.command.install_lib import install_lib
else:
  from distutils.core import setup
  from distutils.command.install_lib import install_lib
# pylint: enable=import-error,no-name-in-module,ungrouped-imports


def main():
  setup(
    name = 'ranger_devicons',
    packages = ['ranger_devicons'],
    version = '1.0',
    description = 'Plugin for the Ranger file manager, that provides a linemode for file glyph/icon rendering',
    author = 'Alexander Jeurissen',
    author_email = 'alexander@jeurissen.email',
    url = 'https://github.com/alexanderjeurissen/ranger_devicons',
    download_url = 'https://github.com/alexanderjeurissen/ranger_devicons/archive/1.0.tar.gz',
    keywords = ['ranger', 'devicons', 'nerd-fonts', 'file-icons'],
    classifiers = [],
  )


if __name__ == '__main__':
  main()
