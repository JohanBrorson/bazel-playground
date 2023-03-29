import os
import sys
import unittest
import xmlrunner


def testrunner(testCase):
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(testCase)])
    junit_out = os.environ["TEST_UNDECLARED_OUTPUTS_DIR"]
    runner = xmlrunner.XMLTestRunner(output=junit_out, outsuffix="")
    result = runner.run(suite)
    sys.exit(not result.wasSuccessful())
