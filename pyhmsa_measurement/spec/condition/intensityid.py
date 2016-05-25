"""
Measurement condition
"""

# Standard library modules.

# Third party modules.
from pyhmsa.spec.condition.condition import _Condition
from pyhmsa.util.parameter import EnumAttribute

# Local modules.

# Globals and constants variables.

INTENSITY_TYPE_PEAK = 'Peak'
INTENSITY_TYPE_BACKGROUND = 'Background'
INTENSITY_TYPE_NET = 'Net'

_INTENSITY_TYPES = frozenset([INTENSITY_TYPE_PEAK,
                              INTENSITY_TYPE_BACKGROUND,
                              INTENSITY_TYPE_NET])

INTENSITY_MEASURE_AREA = 'Area'
INTENSITY_MEASURE_HEIGHT = 'Height'

_INTENSITY_MEASURES = frozenset([INTENSITY_MEASURE_AREA,
                                 INTENSITY_MEASURE_HEIGHT])

class IntensityID(_Condition):

    TEMPLATE = 'IntensityID'

    type = EnumAttribute(_INTENSITY_TYPES,
                         required=True,
                         xmlname='Type',
                         doc='Type of intensity')

    measure = EnumAttribute(_INTENSITY_MEASURES,
                            required=True,
                            xmlname='Measure',
                            doc='How intensity was measured')

    def __init__(self, type_, measure):
        _Condition.__init__(self)

        self.type = type_
        self.measure = measure

