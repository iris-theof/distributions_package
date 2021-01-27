# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from distributions import Gaussian


class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian('numbers_gaussian.txt')

    def test_readdata(self):
        self.assertEqual(self.gaussian.data[0:7],
         [36, 37, 38, 38, 39, 39, 40], 'data not read in correctly')

    def test_meancalculation(self):
        self.assertEqual(self.gaussian.calculate_mean(),
         sum(self.gaussian.data) / float(len(self.gaussian.data)), 'calculated \
         mean not as expected')


    def test_stdevcalculation(self):
        self.assertEqual(round(self.gaussian.calculate_stdev(), 2), 3.92,\
                         'sample standard deviation incorrect')
        self.assertEqual(round(self.gaussian.calculate_stdev(0), 2), 3.90,\
                         'population standard deviation incorrect')

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(40), 5), 0.03803,\
         'pdf function does not give expected result')

    def test_def(self):
        self.assertEqual(str(self.gaussian), "mean {}, standard deviation {}".
                         format(45.5,3.92))

if __name__ == '__main__':
    unittest.main()
