"""
Measurement condition
"""

# Standard library modules.

# Third party modules.
from pyhmsa.spec.condition.condition import _Condition
from pyhmsa.util.parameter import EnumAttribute

# Local modules.

# Globals and constants variables.

class _Measurement(_Condition):
    
    TEMPLATE = 'Measurement'
    
    def __init__(self):
        _Condition.__init__(self)

class MeasurementPeak(_Measurement):
    
    CLASS = 'Peak'

class MeasurementBackground(_Measurement):
    
    CLASS = 'Background'

class MeasurementNet(_Measurement):
    
    CLASS = 'net'
    
    background = EnumAttribute(['Linear', 'Exponential'], 
                               required=False,
                               xmlname='Background',
                               doc='Background interpolation method')
