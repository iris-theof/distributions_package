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

	        self.mean = p

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
               x (float): point for calculating the probability mass function


           Returns:
               float: probability mass function output
        """

        q = 1 - p

        return p**k*(q)**(1-k)

     def plot_bar(self):

        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

          Args:
              None

       	  Returns:
              None
        """

        plt.bar(x = ['0', '1'], height = [(1 - self.p) , self.p ])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')

     def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution

           Args:
               None

           Returns:
               list: x values for the pmf plot
               list: y values for the pmf plot

        """

        x = []
        y = []

        # calculate the x values to visualize
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()

        return x, y
