"""Ranger plugin providing a linemode with devicons."""

import os
import ranger.api
from ranger.core.linemode import LinemodeBase
from .devicons import *

SEPARATOR = os.getenv('RANGER_DEVICONS_SEPARATOR', ' ')

@ranger.api.register_linemode
class DevIconsLinemode(LinemodeBase):
    """Linemode that prefixes file names with their devicon."""

    name = "devicons"
    uses_metadata = False

    def filetitle(self, file, metadata):
        """Return the file's title with the appropriate devicon."""
        return devicon(file) + SEPARATOR + file.relative_path
