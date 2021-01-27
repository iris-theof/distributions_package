import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution
from .Binomialdistribution import Binomial

class Bernoulli(Distribution):
    """ Bernoulli distribution class for calculating and visualizing a Bernoulli distribution.

      Attributes:
      	mean (float) representing the mean value of the distribution
      	stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
	p (float) representing the probability of an event occuring

     """

    def __init__(self, prob=.5):

        self.p = prob
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self):
        """Function to calculate the mean

           Args:
                None

           Returns:
                float: mean of the data set

        """
        self.mean = self.p

        return self.mean

    def calculate_stdev(self):

        """Function to calculate the standard deviation from p.

          Args:
            None

          Returns:
            float: standard deviation of the data set

        """

        self.stdev = math.sqrt(self.p * (1 - self.p))

        return self.stdev

    def replace_stats_with_data(self):

        """Function to calculate p from the data set

        Args:
            None

        Returns:
            float: the p value

        """

        self.p = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p

    def pmf(self, k):

        """Probability mass function calculator for the Bernoulli distribution.

           Args:
               k (0 or 1): number of successes


           Returns:
               float: probability mass function output
        """

        q = 1 - self.p

        return self.p**k*(q)**(1-k)

    def plot_bar(self):

        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

          Args:
              None

       	  Returns:
              None
        """

        plt.bar(x=['0', '1'], height=[(1 - self.p), self.p])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')

        plt.show()

    def __add__(self, other):

        """Function to add together two Bernoulli distributions with equal p

        Args:
            other (Bernoulli): Bernoulli instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = 2
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()

        return result


    def __repr__(self):

        """Function to output the characteristics of the Bernoulli instance

        Args:
            None

        Returns:
            string: characteristics of the Bernoulli

        """

        return "mean {}, standard deviation {}, p {}".\
        format(self.mean, self.stdev, self.p)
