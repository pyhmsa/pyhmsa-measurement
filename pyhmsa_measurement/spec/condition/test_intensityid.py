#!/usr/bin/env python
""" """

# Standard library modules.
import unittest
import logging
import pickle
# Third party modules.

# Local modules.
from pyhmsa_measurement.spec.condition.intensityid import IntensityID

# Globals and constants variables.
from pyhmsa_measurement.spec.condition.intensityid import \
    INTENSITY_TYPE_NET, INTENSITY_MEASURE_HEIGHT

class TestIntensityID(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.intensityid = IntensityID(INTENSITY_TYPE_NET, INTENSITY_MEASURE_HEIGHT)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testtype_(self):
        self.assertEqual(INTENSITY_TYPE_NET, self.intensityid.type)

        self.assertRaises(ValueError, self.intensityid.set_type, 'abc')
        self.assertRaises(ValueError, self.intensityid.set_type, None)

    def testmeasure(self):
        self.assertEqual(INTENSITY_MEASURE_HEIGHT, self.intensityid.measure)

        self.assertRaises(ValueError, self.intensityid.set_measure, 'abc')
        self.assertRaises(ValueError, self.intensityid.set_measure, None)

    def testpickle(self):
        s = pickle.dumps(self.intensityid)
        intensityid = pickle.loads(s)

        self.assertEqual(INTENSITY_TYPE_NET, intensityid.type)
        self.assertEqual(INTENSITY_MEASURE_HEIGHT, intensityid.measure)

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
