"""
XML handler for detectors
"""

# Standard library modules.

# Third party modules.
from pyhmsa.fileformat.xmlhandler.xmlhandler import _XMLHandler

# Local modules.
from pyhmsa_measurement.spec.condition.measurement import \
    MeasurementPeak, MeasurementBackground, MeasurementNet

# Globals and constants variables.

class MeasurementPeakXMLHandler(_XMLHandler):

    def can_parse(self, element):
        return element.tag == 'Measurement' and element.get('Class') == 'Peak'

    def parse(self, element):
        return self._parse_parameter(element, MeasurementPeak)

    def can_convert(self, obj):
        return type(obj) is MeasurementPeak

    def convert(self, obj):
        return self._convert_parameter(obj, 'Measurement', {'Class': 'Peak'})

class MeasurementBackgroundXMLHandler(_XMLHandler):

    def can_parse(self, element):
        return element.tag == 'Measurement' and element.get('Class') == 'Background'

    def parse(self, element):
        return self._parse_parameter(element, MeasurementBackground)

    def can_convert(self, obj):
        return type(obj) is MeasurementBackground

    def convert(self, obj):
        return self._convert_parameter(obj, 'Measurement', {'Class': 'Background'})

class MeasurementNetXMLHandler(_XMLHandler):

    def can_parse(self, element):
        return element.tag == 'Measurement' and element.get('Class') == 'Net'

    def parse(self, element):
        return self._parse_parameter(element, MeasurementNet)

    def can_convert(self, obj):
        return type(obj) is MeasurementNet

    def convert(self, obj):
        return self._convert_parameter(obj, 'Measurement', {'Class': 'Net'})