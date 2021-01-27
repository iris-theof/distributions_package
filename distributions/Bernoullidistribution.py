import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Bernoulli(Distribution):
    """ Bernoulli distribution class for calculating and visualizing a Bernoulli distribution.

      Attributes:
      	mean (float) representing the mean value of the distribution
      	stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
	p (float) representing the probability of an event occuring

     """

    def __init__(self, file_name='name'):

        Distribution.__init__(self, file_name)

        self.p = 1.0 * sum(self.data) / len(self.data)

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

        """Function to calculate the standard deviation from p

          Args:
            None

          Returns:
            float: standard deviation of the data set

        """

        self.stdev = math.sqrt(self.p * (1 - self.p))

        return self.stdev

    def extract_stats_from_data(self):

        """Function to calculate p from the data set

        Args:
            None

        Returns:
            float: the p value

        """

        self.p = 1.0 * sum(self.data) / len(self.data)

        return self.p

    def pmf(self, k):

        """Probability mass function calculator for the Bernoulli distribution.

           Args:
               k (0 or 1): number of successes


           Returns:
               float: probability mass function output
        """

        if ((k == 1) or (k == 0)) == False:
            print(k)
            print ("k (the argumnet of pmf) needs to be either zero or one")
            exit()

        q = 1 - self.p

        return self.p**k*(q)**(1-k)

    def plot_bar(self):

        """Function to output a bar plot of the propability of success
           and failure

          Args:
              None

       	  Returns:
              None
        """

        plt.bar(x=['0', '1'], height=[(1 - self.p), self.p])
        plt.title('Propability of failure (0) and success (1)')
        plt.xlabel('Outcome')
        plt.ylabel('Propability')

        plt.show()

    def __repr__(self):

        """Function to output the parameters of the Bernoulli instance

        Args:
            None

        Returns:
            string: characteristics of the Bernoulli

        """

        return "Propability of success p {}, propability of failure q {}".\
        format(round(self.p,2), round((1-self.p),2))
