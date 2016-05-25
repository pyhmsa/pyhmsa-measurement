#!/usr/bin/env python
""" """

# Standard library modules.
import unittest
import logging
import pickle

# Third party modules.

# Local modules.
from pyhmsa_measurement.spec.condition.backgroundid import BackgroundID

# Globals and constants variables.
from pyhmsa_measurement.spec.condition.backgroundid import \
    BACKGROUND_INTERPOLATION_LINEAR

class TestIntensityID(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.bckgid = BackgroundID(BACKGROUND_INTERPOLATION_LINEAR)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testinterpolation(self):
        self.assertEqual(BACKGROUND_INTERPOLATION_LINEAR, self.bckgid.interpolation)

        self.assertRaises(ValueError, self.bckgid.set_interpolation, 'abc')
        self.assertRaises(ValueError, self.bckgid.set_interpolation, None)

    def testpickle(self):
        s = pickle.dumps(self.bckgid)
        bckgid = pickle.loads(s)

        self.assertEqual(BACKGROUND_INTERPOLATION_LINEAR, bckgid.interpolation)

if __name__ == '__main__': #pragma: no cover
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
