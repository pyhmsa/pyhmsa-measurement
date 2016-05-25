"""
XML handler for intensity id condition
"""

# Standard library modules.

# Third party modules.
from pyhmsa.fileformat.xmlhandler.condition.condition import _ConditionXMLHandler

# Local modules.
from pyhmsa_measurement.spec.condition.intensityid import IntensityID

# Globals and constants variables.

class IntensityIDXMLHandler(_ConditionXMLHandler):

    def __init__(self, version):
        super().__init__(IntensityID, version)
