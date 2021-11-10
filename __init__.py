import os
from ranger.api import register_linemode
from ranger.core import linemode
from .devicons import *


SEPARATOR = os.getenv('RANGER_DEVICONS_SEPARATOR', ' ')
PATCH_BUILTIN = (os.getenv('RANGER_DEVICONS_PATCH_BUILTIN', 'True').lower() in ('true', 'yes', '1'))


def patch_devicons(base, classname=None, attributes=None):
    """Patch a linemode class with file icons."""

    classname = classname or base.__name__
    attributes = attributes or {}

    def filetitle(self, file, metadata):
        """Prefix a file icon to the file title."""

        icon = devicon(file)
        return ''.join((
            icon,
            SEPARATOR,
            super(self.__class__, self).filetitle(file, metadata)
        ))

    return type(classname, (base,), {'filetitle': filetitle, **attributes})


# Identical to patched DefaultLinemode(name='filename')
DevIconsLinemode = register_linemode(patch_devicons(base=linemode.DefaultLinemode,
                                                    classname='DevIconsLinemode',
                                                    attributes={'name': 'devicons'}))


if PATCH_BUILTIN:
    name, member = None, None
    for name, member in vars(linemode).items():
        if name.endswith('Linemode'):
            try:
                if not issubclass(member, linemode.LinemodeBase):
                    continue
            except TypeError:
                continue
            else:
                # Patch ranger's builtin linemodes
                globals()[name] = register_linemode(patch_devicons(base=member))

    del name, member
