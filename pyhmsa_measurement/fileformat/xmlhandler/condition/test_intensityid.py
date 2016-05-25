#!/usr/bin/env python
""" """

# Standard library modules.
import unittest
import logging
import xml.etree.ElementTree as etree

# Third party modules.

# Local modules.
from pyhmsa_measurement.fileformat.xmlhandler.condition.intensityid import \
    IntensityIDXMLHandler
from pyhmsa_measurement.spec.condition.intensityid import IntensityID

# Globals and constants variables.
from pyhmsa_measurement.spec.condition.intensityid import \
    INTENSITY_TYPE_NET, INTENSITY_MEASURE_HEIGHT

class TestIntensityIDXMLHandler(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.h = IntensityIDXMLHandler(1.0)

        self.obj = IntensityID(INTENSITY_TYPE_NET, INTENSITY_MEASURE_HEIGHT)

        source = u'<IntensityID><Measure>Height</Measure><Type>Net</Type></IntensityID>'
        self.element = etree.fromstring(source.encode('utf-8'))

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testcan_parse(self):
        self.assertTrue(self.h.can_parse(self.element))

    def testparse(self):
        obj = self.h.parse(self.element)
        self.assertEqual(INTENSITY_TYPE_NET, obj.type)
        self.assertEqual(INTENSITY_MEASURE_HEIGHT, obj.measure)

    def testcan_convert(self):
        self.assertTrue(self.h.can_convert(self.obj))

    def testconvert(self):
        element = self.h.convert(self.obj)
        self.assertEqual(IntensityID.TEMPLATE, element.tag)
        self.assertEqual('Height', element.find('Measure').text)
        self.assertEqual('Net', element.find('Type').text)

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
