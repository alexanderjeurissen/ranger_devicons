# File icons for the Ranger file manager

This plugin introduces a new linemode that prefixes file names with a file icon

![image](screenshot.png)

## Prerequisites

This plugin uses glyphs from a patched NERDfont. So in order for this plugin to work you need to
install a NERDfont and set it as the default font for your terminal.

I personally use the Source Code Pro patched NERDfont(this is also the font displayed in the
screenshot), this and other NERDfonts and the install instructions for these fonts can be found in
the following repository: https://github.com/ryanoasis/nerd-fonts

## Install instructions

Ranger has added support for loading directories in the plugins folder which makes it easier to install and keep plugins updated.
To install, just clone the repo into the plugins folder:

```bash
git clone --depth=1 https://github.com/alexanderjeurissen/ranger_devicons ~/.config/ranger/plugins/ranger_devicons
```

## Configuration

This plugin can be configured by setting environment variables (e.g. in your
`~/.profile`).

- `RANGER_DEVICONS_SEPARATOR` (default `" "`, i.e. a single space): The
  separator between icon and filename. Some terminals use the adjacent space to
  display a bigger icon, in which case this can be set to two spaces instead.

- `RANGER_DEVICONS_PATCH_BUILTIN` (default `True`): Whether to patch Ranger's
  builtin linemodes, i.e., prefixes all builtin linemodes with file icons. You
  can set `RANGER_DEVICONS_PATCH_BUILTIN="False"` to disable this and execute the
  following command:

  ```bash
  echo "default_linemode devicons" >> "$HOME/.config/ranger/rc.conf"
  ```

  to use the devicons linemode (which is identical to the patched version of Ranger's
  default linemode).
