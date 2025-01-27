#!/usr/bin/python
# coding=UTF-8
# These glyphs, and the mapping of file extensions to glyphs
# has been copied from the vimscript code that is present in
# https://github.com/ryanoasis/vim-devicons

import re
import os
import yaml

# Load locale files
def load_locale(locale):
    with open(f'locales/{locale}.yml', 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# Get the current locale
current_locale = os.getenv('LANG', 'en').split('.')[0]

# Load the current locale and English locale
current_locale_data = load_locale(current_locale)
english_locale_data = load_locale('en')

# Get the XDG_USER_DIRS directory names from environment variables
xdgs_dirs = {
    os.path.basename(os.getenv(key).rstrip('/')): icon
    for key, icon in (
        ('XDG_DOCUMENTS_DIR', ''),
        ('XDG_DOWNLOAD_DIR', ''),
        ('XDG_CONFIG_DIR', ''),
        ('XDG_MUSIC_DIR', ''),
        ('XDG_PICTURES_DIR', ''),
        ('XDG_PUBLICSHARE_DIR', ''),
        ('XDG_TEMPLATES_DIR', ''),
        ('XDG_VIDEOS_DIR', ''),
    )
    if os.getenv(key)
}


# all those glyphs will show as weird squares if you don't have the correct patched font
# My advice is to use NerdFonts which can be found here:
# https://github.com/ryanoasis/nerd-fonts
file_node_extensions = {
    '7z'       : '',
    'a'        : '',
    'ai'       : '',
    'apk'      : '',
    'asm'      : '',
    'asp'      : '',
    'aup'      : '',
    'avi'      : '',
    'awk'      : '',
    'bash'     : '',
    'bat'      : '',
    'bmp'      : '',
    'bz2'      : '',
    'c'        : '',
    'c++'      : '',
    'cab'      : '',
    'cbr'      : '',
    'cbz'      : '',
    'cc'       : '',
    'class'    : '',
    'clj'      : '',
    'cljc'     : '',
    'cljs'     : '',
    'cmake'    : '',
    'coffee'   : '',
    'conf'     : '',
    'cp'       : '',
    'cpio'     : '',
    'cpp'      : '',
    'cs'       : '󰌛',
    'csh'      : '',
    'css'      : '',
    'cue'      : '',
    'cvs'      : '',
    'cxx'      : '',
    'd'        : '',
    'dart'     : '',
    'db'       : '',
    'deb'      : '',
    'diff'     : '',
    'dll'      : '',
    'wps'      : '',
    'wpt'      : '',
    'doc'      : '',
    'docx'     : '',
    'docm'     : '',
    'dotx'     : '',
    'dotm'     : '',
    'dump'     : '',
    'edn'      : '',
    'eex'      : '',
    'efi'      : '',
    'ejs'      : '',
    'elf'      : '',
    'elm'      : '',
    'epub'     : '',
    'erl'      : '',
    'ex'       : '',
    'exe'      : '',
    'exs'      : '',
    'f#'       : '',
    'fifo'     : '󰟥',
    'fish'     : '',
    'flac'     : '',
    'flv'      : '',
    'fs'       : '',
    'fsi'      : '',
    'fsscript' : '',
    'fsx'      : '',
    'gem'      : '',
    'gemspec'  : '',
    'gif'      : '',
    'go'       : '',
    'gz'       : '',
    'gzip'     : '',
    'h'        : '',
    'haml'     : '',
    'hbs'      : '',
    'hh'       : '',
    'hpp'      : '',
    'hrl'      : '',
    'hs'       : '',
    'htaccess' : '',
    'htm'      : '',
    'html'     : '',
    'htpasswd' : '',
    'hxx'      : '',
    'ico'      : '',
    'img'      : '',
    'ini'      : '',
    'ipynb'    : '',
    'iso'      : '',
    'jar'      : '',
    'java'     : '',
    'jl'       : '',
    'jpeg'     : '',
    'jpg'      : '',
    'js'       : '',
    'json'     : '',
    'jsonc'    : '',
    'jsx'      : '',
    'key'      : '',
    'ksh'      : '',
    'leex'     : '',
    'less'     : '',
    'lha'      : '',
    'lhs'      : '',
    'log'      : '',
    'lua'      : '',
    'lz'       : '',
    'lzh'      : '',
    'lzma'     : '',
    'm4a'      : '',
    'm4v'      : '',
    'markdown' : '',
    'md'       : '',
    'mdx'      : '',
    'mjs'      : '',
    'mka'      : '',
    'mkv'      : '',
    'ml'       : 'λ',
    'mli'      : 'λ',
    'mov'      : '',
    'mp3'      : '',
    'mp4'      : '',
    'mpeg'     : '',
    'mpg'      : '',
    'msi'      : '',
    'mustache' : '',
    'nix'      : '',
    'o'        : '',
    'ogg'      : '',
    'opus'     : '',
    'part'     : '',
    'pdf'      : '',
    'php'      : '',
    'pl'       : '',
    'pm'       : '',
    'png'      : '',
    'pp'       : '',
    'dps'      : '',
    'dpt'      : '',
    'ppt'      : '',
    'pptx'     : '',
    'pptm'     : '',
    'pot'      : '',
    'potx'     : '',
    'potm'     : '',
    'pps'      : '',
    'ppsx'     : '',
    'ppsm'     : '',
    'ps1'      : '',
    'psb'      : '',
    'psd'      : '',
    'pub'      : '',
    'py'       : '',
    'pyc'      : '',
    'pyd'      : '',
    'pyo'      : '',
    'r'        : '󰟔',
    'rake'     : '',
    'rar'      : '',
    'rb'       : '',
    'rc'       : '',
    'rlib'     : '',
    'rmd'      : '',
    'rom'      : '',
    'rpm'      : '',
    'rproj'    : '󰗆',
    'rs'       : '',
    'rss'      : '',
    'rtf'      : '',
    's'        : '',
    'sass'     : '',
    'scala'    : '',
    'scss'     : '',
    'sh'       : '',
    'slim'     : '',
    'sln'      : '',
    'so'       : '',
    'sql'      : '',
    'styl'     : '',
    'suo'      : '',
    'svelte'   : '',
    'swift'    : '',
    't'        : '',
    'tar'      : '',
    'tex'      : '󰙩',
    'tgz'      : '',
    'toml'     : '',
    'torrent'  : '',
    'ts'       : '',
    'tsx'      : '',
    'twig'     : '',
    'vim'      : '',
    'vimrc'    : '',
    'vue'      : '󰡄',
    'wav'      : '',
    'webm'     : '',
    'webmanifest' : '',
    'webp'     : '',
    'xbps'     : '',
    'xcplayground' : '',
    'xhtml'    : '',
    'et'       : '󰈛',
    'ett'      : '󰈛',
    'xls'      : '󰈛',
    'xlt'      : '󰈛',
    'xlsx'     : '󰈛',
    'xlsm'     : '󰈛',
    'xlsb'     : '󰈛',
    'xltx'     : '󰈛',
    'xltm'     : '󰈛',
    'xla'      : '󰈛',
    'xlam'     : '󰈛',
    'xml'      : '',
    'xul'      : '',
    'xz'       : '',
    'yaml'     : '',
    'yml'      : '',
    'zip'      : '',
    'zsh'      : '',
}


# Python 2.x-3.4 don't support unpacking syntex `{**dict}`
# XDG_USER_DIRS
dir_node_exact_matches.update(xdgs_dirs)


file_node_exact_matches = {
    '.bash_aliases'                    : '',
    '.bash_history'                    : '',
    '.bash_logout'                     : '',
    '.bash_profile'                    : '',
    '.bashprofile'                     : '',
    '.bashrc'                          : '',
    '.dmrc'                            : '',
    '.DS_Store'                        : '',
    '.fasd'                            : '',
    '.fehbg'                           : '',
    '.gitattributes'                   : '',
    '.gitconfig'                       : '',
    '.gitignore'                       : '',
    '.gitlab-ci.yml'                   : '',
    '.gvimrc'                          : '',
    '.inputrc'                         : '',
    '.jack-settings'                   : '',
    '.mime.types'                      : '',
    '.ncmpcpp'                         : '',
    '.nvidia-settings-rc'              : '',
    '.pam_environment'                 : '',
    '.profile'                         : '',
    '.recently-used'                   : '',
    '.selected_editor'                 : '',
    '.vim'                             : '',
    '.viminfo'                         : '',
    '.vimrc'                           : '',
    '.Xauthority'                      : '',
    '.Xdefaults'                       : '',
    '.xinitrc'                         : '',
    '.xinputrc'                        : '',
    '.Xresources'                      : '',
    '.zshrc'                           : '',
    '_gvimrc'                          : '',
    '_vimrc'                           : '',
    'a.out'                            : '',
    'authorized_keys'                  : '',
    'bspwmrc'                          : '',
    'cmakelists.txt'                   : '',
    'config'                           : '',
    'config.ac'                        : '',
    'config.m4'                        : '',
    'config.mk'                        : '',
    'config.ru'                        : '',
    'configure'                        : '',
    'docker-compose.yml'               : '',
    'dockerfile'                       : '',
    'Dockerfile'                       : '',
    'dropbox'                          : '',
    'exact-match-case-sensitive-1.txt' : 'X1',
    'exact-match-case-sensitive-2'     : 'X2',
    'favicon.ico'                      : '',
    'gemfile'                          : '',
    'gruntfile.coffee'                 : '',
    'gruntfile.js'                     : '',
    'gruntfile.ls'                     : '',
    'gulpfile.coffee'                  : '',
    'gulpfile.js'                      : '',
    'gulpfile.ls'                      : '',
    'ini'                              : '',
    'known_hosts'                      : '',
    'ledger'                           : '',
    'license'                          : '',
    'LICENSE'                          : '',
    'LICENSE.md'                       : '',
    'LICENSE.txt'                      : '',
    'Makefile'                         : '',
    'makefile'                         : '',
    'Makefile.ac'                      : '',
    'Makefile.in'                      : '',
    'mimeapps.list'                    : '',
    'mix.lock'                         : '',
    'node_modules'                     : '',
    'package-lock.json'                : '',
    'package.json'                     : '',
    'playlists'                        : '',
    'procfile'                         : '',
    'Rakefile'                         : '',
    'rakefile'                         : '',
    'react.jsx'                        : '',
    'README'                           : '',
    'README.markdown'                  : '',
    'README.md'                        : '',
    'README.rst'                       : '',
    'README.txt'                       : '',
    'sxhkdrc'                          : '',
    'user-dirs.dirs'                   : '',
    'webpack.config.js'                : '',
}


def devicon(file):
    if file.is_directory:
        if current_locale != 'en':
            english_name = current_locale_data['directory_mappings'].get(file.relative_path)
            if english_name:
                return english_locale_data['directory_mappings'].get(english_name, '')
        return english_locale_data['directory_mappings'].get(file.relative_path, '')
    return file_node_exact_matches.get(os.path.basename(file.relative_path),
                                       file_node_extensions.get(file.extension, ''))
