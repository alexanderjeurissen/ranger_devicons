RANGER_DIR=$(if $(XDG_CONFIG_HOME),$(XDG_CONFIG_HOME),$(HOME)/.config)/ranger
PLUGIN_DIR=$(RANGER_DIR)/plugins
RC_FILE=$(RANGER_DIR)/rc.conf

install:
	install -d $(PLUGIN_DIR)
	install -b devicons.py $(PLUGIN_DIR)/devicons.py
	install -b __init__.py $(PLUGIN_DIR)/devicons_linemode.py
	grep -q 'default_linemode devicons' $(RC_FILE) || echo '# a plugin that adds file glyphs / icon support to Ranger:' >> $(RC_FILE)
	grep -q 'default_linemode devicons' $(RC_FILE) || echo '# https://github.com/alexanderjeurissen/ranger_devicons' >> $(RC_FILE)
	grep -q 'default_linemode devicons' $(RC_FILE) || echo 'default_linemode devicons' >> $(RC_FILE)

uninstall:
	sed -i.old -E '/^# a plugin that adds file glyphs/d' $(RC_FILE)
	sed -i.old -E '/^# https:\/\/github.com\/alexanderjeurissen\/ranger_devicons/d' $(RC_FILE)
	sed -i.old -E '/^default_linemode devicons/d' $(RC_FILE)
	$(RM) $(PLUGIN_DIR)/devicons.py
	$(RM) $(PLUGIN_DIR)/devicons_linemode.py
