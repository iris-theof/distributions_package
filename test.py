# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from distributions import Gaussian
from distributions import Binomial
from distributions import Bernoulli


class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian('numbers_gaussian.txt')

    def test_readdata(self):
        self.assertEqual(self.gaussian.data[0:7],
         [36, 37, 38, 38, 39, 39, 40], 'data not read in correctly')

    def test_meancalculation(self):
        self.assertEqual(round(self.gaussian.calculate_mean(),2),
         round(sum(self.gaussian.data) / float(len(self.gaussian.data)),2),\
         'calculated mean not as expected')


    def test_stdevcalculation(self):
        self.assertEqual(round(self.gaussian.calculate_stdev(), 2), 3.92,\
                         'sample standard deviation incorrect')
        self.assertEqual(round(self.gaussian.calculate_stdev(0), 2), 3.90,\
                         'population standard deviation incorrect')

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(40), 5), 0.03803,\
         'propability density function does not give expected result')

    def test_def(self):
        self.assertEqual(str(self.gaussian), "mean {}, variance {}".
                         format(45.5, 15.36),'parameters of the Gaussian\
                          not as expected')

class TestBinomialClass(unittest.TestCase):
    def setUp(self):
        self.binomial = Binomial('numbers_binomial.txt')

    def test_readdata(self):
        self.assertEqual(self.binomial.data,\
         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], 'data not read in correctly')

    def test_meancalculation(self):
        mean = self.binomial.calculate_mean()
        self.assertEqual(round(mean,2), 8.00, 'calculated mean not as expected')

    def test_stdevcalculation(self):
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(round(stdev, 2), 1.75,'calculated standard deviation\
                         not as expected')

    def test_pmf(self):
        self.assertEqual(round(self.binomial.pmf(5), 3), 0.054, 'propability \
        mass function does not give the expected result ')
        self.assertEqual(round(self.binomial.pmf(3), 3), 0.005)

    def test_def(self):
        self.assertEqual(str(self.binomial),
        """Number of trials {}, success propability for each trial {} """ .\
        format(13, 0.62),'Parameters of the Binomial not as expected')

class TestBernoulliClass(unittest.TestCase):
    def setUp(self):
         self.bernoulli = Bernoulli('numbers_binomial.txt')

    def test_readdata(self):
        self.assertEqual(self.bernoulli.data,\
         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0], 'data not read in correctly')

    def test_meancalculation(self):
        mean = self.bernoulli.calculate_mean()
        self.assertEqual(round(mean, 1), 0.6, 'calculated mean not as expected')

    def test_stdevcalculation(self):
        stdev = self.bernoulli.calculate_stdev()
        self.assertEqual(round(stdev, 2), 0.49,'calculated standard deviation \
        not as expected')

    def test_pmf(self):
        self.assertEqual(round(self.bernoulli.pmf(1), 3), 0.615,'propability\
         mass function not as expected')
        self.assertEqual(round(self.bernoulli.pmf(0), 3), 0.385,'propability\
         mass function not as expected')

    def test_def(self):
        self.assertEqual(str(self.bernoulli),
        "Propability of success p {}, propability of failure q {}" .\
        format(0.62, 0.38),'Parameters of the Bernoulli not as expected')

if __name__ == '__main__':
    unittest.main()
