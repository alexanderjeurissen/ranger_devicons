RANGER_DIR=$(if $(XDG_CONFIG_HOME),$(XDG_CONFIG_HOME),$(HOME)/.config)/ranger
PLUGIN_DIR=$(RANGER_DIR)/plugins
RC_FILE=$(RANGER_DIR)/rc.conf

install:
	install -d $(PLUGIN_DIR)
	install -b devicons.py $(PLUGIN_DIR)/devicons.py
	install -b devicons_linemode.py $(PLUGIN_DIR)/devicons_linemode.py
	grep -q 'default_linemode devicons' $(RC_FILE) || echo '# a plugin that adds file glyphs / icon support to Ranger:' >> $(RC_FILE)
	grep -q 'default_linemode devicons' $(RC_FILE) || echo '# https://github.com/alexanderjeurissen/ranger_devicons' >> $(RC_FILE)
	grep -q 'default_linemode devicons' $(RC_FILE) || echo 'default_linemode devicons' >> $(RC_FILE)

uninstall:
	$(RM) $(PLUGIN_DIR)/devicons.py
	$(RM) $(PLUGIN_DIR)/devicons_linemode.py
