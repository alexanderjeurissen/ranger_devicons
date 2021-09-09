import os
import ranger.api
from ranger.core import linemode
from .devicons import *

SEPARATOR = os.getenv('RANGER_DEVICONS_SEPARATOR', ' ')


@ranger.api.register_linemode
class DevIconsLinemode(linemode.LinemodeBase):
    name = "devicons"
    uses_metadata = False

    def filetitle(self, file, metadata):
        return SEPARATOR.join((devicon(file), file.relative_path))


def patch_devicons(cls):
    def filetitle(self, file, metadata):
        return SEPARATOR.join((devicon(file),
                               super(self.__class__, self).filetitle(file, metadata)))

    return type(cls.__name__, (cls,), {'filetitle': filetitle})


name, attr = None, None
for name, attr in vars(linemode).items():
    if name.endswith('Linemode'):
        try:
            if issubclass(attr, linemode.LinemodeBase):
                globals()[name] = ranger.api.register_linemode(patch_devicons(attr))
        except TypeError:
            pass

del name, attr
