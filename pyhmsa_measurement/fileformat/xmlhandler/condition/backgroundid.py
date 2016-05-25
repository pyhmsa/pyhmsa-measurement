"""
XML handler for background id condition
"""

# Standard library modules.

# Third party modules.
from pyhmsa.fileformat.xmlhandler.condition.condition import _ConditionXMLHandler

# Local modules.
from pyhmsa_measurement.spec.condition.backgroundid import BackgroundID

# Globals and constants variables.

class BackgroundIDXMLHandler(_ConditionXMLHandler):

    def __init__(self, version):
        super().__init__(BackgroundID, version)
