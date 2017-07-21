RANGER_DIR=$(if $(XDG_CONFIG_HOME),$(XDG_CONFIG_HOME),$(HOME)/.config)/ranger
PLUGIN_DIR=$(RANGER_DIR)/plugins
RC_FILE=$(RANGER_DIR)/rc.conf
DEVICONS_IN_RC="default_linemode devicons"

install:
	install -d $(PLUGIN_DIR)
	install -b devicons.py $(RANGER_DIR)/devicons.py
	install -b devicons_linemode.py $(PLUGIN_DIR)/devicons_linemode.py
	grep -q $(DEVICONS_IN_RC) $(RC_FILE) || echo $(DEVICONS_IN_RC) >> $(RC_FILE)

uninstall:
	$(RM) $(RANGER_DIR)/devicons.py
	$(RM) $(PLUGIN_DIR)/devicons_linemode.py
