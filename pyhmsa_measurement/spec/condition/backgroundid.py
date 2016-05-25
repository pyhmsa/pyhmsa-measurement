""""""

# Standard library modules.

# Third party modules.
from pyhmsa.spec.condition.condition import _Condition
from pyhmsa.util.parameter import EnumAttribute

# Local modules.

# Globals and constants variables.

BACKGROUND_INTERPOLATION_LINEAR = 'Linear'
BACKGROUND_INTERPOLATION_EXPONENTIAL = 'Exponential'

_BACKGROUND_INTERPOLATIONS = frozenset([BACKGROUND_INTERPOLATION_LINEAR,
                                        BACKGROUND_INTERPOLATION_EXPONENTIAL])

class BackgroundID(_Condition):

    TEMPLATE = 'BackgroundID'

    interpolation = EnumAttribute(_BACKGROUND_INTERPOLATIONS,
                                  required=True,
                                  xmlname='Interpolation',
                                  doc='Interpolation method')

    def __init__(self, interpolation):
        super().__init__()

        self.interpolation = interpolation
