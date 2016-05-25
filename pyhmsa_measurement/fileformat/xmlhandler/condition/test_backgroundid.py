#!/usr/bin/env python
""" """

# Standard library modules.
import unittest
import logging
import xml.etree.ElementTree as etree

# Third party modules.

# Local modules.
from pyhmsa_measurement.fileformat.xmlhandler.condition.backgroundid import \
    BackgroundIDXMLHandler
from pyhmsa_measurement.spec.condition.backgroundid import BackgroundID

# Globals and constants variables.
from pyhmsa_measurement.spec.condition.backgroundid import \
    BACKGROUND_INTERPOLATION_LINEAR

class TestBackgroundIDXMLHandler(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.h = BackgroundIDXMLHandler(1.0)

        self.obj = BackgroundID(BACKGROUND_INTERPOLATION_LINEAR)

        source = u'<BackgroundID><Interpolation>Linear</Interpolation></BackgroundID>'
        self.element = etree.fromstring(source.encode('utf-8'))

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testcan_parse(self):
        self.assertTrue(self.h.can_parse(self.element))

    def testparse(self):
        obj = self.h.parse(self.element)
        self.assertEqual(BACKGROUND_INTERPOLATION_LINEAR, obj.interpolation)

    def testcan_convert(self):
        self.assertTrue(self.h.can_convert(self.obj))

    def testconvert(self):
        element = self.h.convert(self.obj)
        self.assertEqual(BackgroundID.TEMPLATE, element.tag)
        self.assertEqual('Linear', element.find('Interpolation').text)

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
