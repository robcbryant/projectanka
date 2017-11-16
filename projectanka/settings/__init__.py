""" Settings for projectanka """

from .settings import *
try:
    from .local_settings import *
except ImportError, exc:
    exc.args = tuple(
        ['%s (did you rename settings/local_settings.py?)' % exc.args[0]])
    raise exc
