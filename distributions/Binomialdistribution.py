import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) number of trials
    """

    def __init__(self, file_name='name'):

        Distribution.__init__(self, file_name)

        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)

    def calculate_mean(self):

        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """

        self.mean = self.p * self.n

        return self.mean



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """

        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))

        return self.stdev


    def extract_stats_from_data(self):

        """Function to calculate p, n, mean and standard deviation from the data
         set

        Args:
            None

        Returns:
            None
        """

        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)

    def plot_bar(self):
        """Function to output a bar chart of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        self.extract_stats_from_data()

        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.title('Number of successes (1) and failures (0) ')
        plt.xlabel('outcome')
        plt.ylabel('count')

        plt.show()

    def pmf(self, k):
        """Probability mass function calculator for the binomial distribution.

        Args:
          k (natural number): number of successes


        Returns:
            float: probability mass function output
        """

        if ((isinstance(k,int) == False) or (k < 0)):
            print ("k (the argumnet of pmf) needs to be a non-negative integer")
            exit()


        self.extract_stats_from_data()

        a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
        b = (self.p ** k) * (1 - self.p) ** (self.n - k)

        return a * b


    def plot_bar_pmf(self):

        """Function to plot the pmf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        x = []
        y = []

        self.extract_stats_from_data()

        # calculate the x values to visualize
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pmf(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability Mass Function')
        plt.xlabel('Number of successes (k)')
        plt.show()

        return 

    def __repr__(self):

        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial

        """

        self.extract_stats_from_data()

        return "Number of trials {}, success propability for each trial {} ".\
                format(self.n, round(self.p, 2))
