# File icons for the Ranger file manager

This plugin introduces a new linemode that prefixes file names with a file icon

![image](https://raw.githubusercontent.com/alexanderjeurissen/ranger_devicons/master/screenshot.png)

## Prerequisites
This plugin uses glyphs from a patched NERDfont. So in order for this plugin to work you need to
install a NERDfont and set it as the default font for your terminal.

I personally use the Source Code Pro patched NERDfont(this is also the font displayed in the
screenshot), this and other NERDfonts and the install instructions for these fonts can be found in
the following repository: https://github.com/ryanoasis/nerd-fonts

## Install instructions
Ranger has added support for loading directories in the plugins folder to `master` which makes it easier to install and keep plugins updated.
To install, just clone the repo into the plugins folder:
```bash
git clone https://github.com/alexanderjeurissen/ranger_devicons ~/.config/ranger/plugins/ranger_devicons
```

Then execute the following `echo "default_linemode devicons" >> $HOME/.config/ranger/rc.conf` (or wherever your `rc.conf` is located).
