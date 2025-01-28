# File icons for the Ranger file manager

This plugin introduces a new linemode that prefixes file names with a file icon

![image](screenshot.png)

## Prerequisites

This plugin uses glyphs from a patched NERDfont. So in order for this plugin to work you need to install a NERDfont and set it as the default font for your terminal.

I personally use the Source Code Pro patched NERDfont(this is also the font displayed in the screenshot), this and other NERDfonts and the install instructions for these fonts can be found in the [following repository](https://github.com/ryanoasis/nerd-fonts)

## Install instructions

Ranger has added support for loading directories in the plugins folder which makes it easier to install and keep plugins updated.

To install, just clone the repo into the plugins folder:

```bash
git clone https://github.com/alexanderjeurissen/ranger_devicons ~/.config/ranger/plugins/ranger_devicons
```

Then execute the following `echo "default_linemode devicons" >> $HOME/.config/ranger/rc.conf` (or wherever your `rc.conf` is located).

## Configuration

This plugin can be configured by setting environment variables (e.g. in your
`~/.profile`). Currently, only one option is available:

- `RANGER_DEVICONS_SEPARATOR` (default `" "`, i.e. a single space): The
  separator between icon and filename. Some terminals use the adjacent space to
  display a bigger icon, in which case this can be set to two spaces instead.

## Locale Support

This plugin supports I18n for directory name to icon mappings. Locale files are created for each language listed in `devicons.py`. The `devicon` function retrieves the locale file for the current locale and the English locale. It then looks up `file.relative_path` inside the current locale to determine the English directory mapping name (only if the current locale is not English). Finally, it looks up the English directory mapping name in the English locale to retrieve the icon.

### Adding New Locale Files

To add a new locale file, follow these steps:

1. Create a new file in the `locales` directory with the appropriate locale code (e.g., `locales/ja.yml` for Japanese).
2. Add directory mappings for the new locale. The mappings should map the directory names in the new locale to the English directory names.

Example:

```yaml
ja:
  directory_mappings:
    'デスクトップ': 'Desktop'
    'ドキュメント': 'Documents'
    'ダウンロード': 'Downloads'
    '音楽': 'Music'
    '画像': 'Pictures'
    '公開': 'Public'
    'テンプレート': 'Templates'
    'ビデオ': 'Videos'
```
