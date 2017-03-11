RANGER_DIR=$(if $(XDG_CONFIG_HOME),$(XDG_CONFIG_HOME),$(HOME)/.config)/ranger
PLUGIN_DIR=$(RANGER_DIR)/plugins

install:
	install -d $(PLUGIN_DIR)
	install -b devicons.py $(RANGER_DIR)/devicons.py
	install -b devicons_linemode.py $(PLUGIN_DIR)/devicons_linemode.py

uninstall:
	$(RM) $(RANGER_DIR)/devicons.py
	$(RM) $(PLUGIN_DIR)/devicons_linemode.py
