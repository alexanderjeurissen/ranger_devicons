import os
from ranger.api import register_linemode
from ranger.core import linemode
from .devicons import *


# User configurations
SEPARATOR = os.getenv('RANGER_DEVICONS_SEPARATOR', ' ')
OVERRIDE_BUILTIN = (os.getenv('RANGER_DEVICONS_OVERRIDE_BUILTIN', 'True').lower() in ('true', 'yes', '1'))


# Make patched linemode class
def patch_devicons(base, classname=None, attributes=None):
    """Patch a linemode class with file icons."""

    classname = classname or base.__name__
    attributes = (attributes or {}).copy()

    def filetitle(self, file, metadata):
        """Prefix a file icon to the file title."""

        icon = devicon(file)
        return ''.join((
            icon,
            SEPARATOR,
            super(self.__class__, self).filetitle(file, metadata)
        ))

    # Python 2.x-3.4 don't support unpacking syntex `{**dict}`
    attributes['filetitle'] = filetitle

    return type(classname, (base,), attributes)  # make subclass


# Add `DevIconsLinemode` linemode class
# Identical to patched DefaultLinemode(name='filename') (i.e., `devicons-filename`)
DevIconsLinemode = register_linemode(patch_devicons(base=linemode.DefaultLinemode,
                                                    classname='DevIconsLinemode',
                                                    attributes={'name': 'devicons'}))


# Patch ranger's builtin linemodes with prefix `devicons-`
name, linemode_class, new_name, new_classname = None, None, None, None
for name, linemode_class in vars(linemode).items():
    if name.endswith('Linemode'):
        try:
            if not issubclass(linemode_class, linemode.LinemodeBase):
                continue
        except TypeError:
            continue
        else:
            # Patch ranger's builtin linemodes with prefix `devicons-`
            new_name = 'devicons-' + linemode_class.name          # e.g., fileinfo         -> devicons-fileinfo
            new_classname = 'DevIcons' + linemode_class.__name__  # e.g., FileInfoLinemode -> DevIconsFileInfoLinemode
            globals()[new_name] = register_linemode(patch_devicons(base=linemode_class,
                                                                  classname=new_classname,
                                                                  attributes={'name': new_name}))

            if OVERRIDE_BUILTIN: # Override ranger's builtin linemodes
                globals()[name] = register_linemode(patch_devicons(base=linemode_class))

del name, linemode_class, new_name, new_classname
