
### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Usage](#usage)
4. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

A package that provides ready functions to deal with Gaussian, Binomial and Bernoulli distributions. Including calculation of mean, standard deviation, parameteers, Probability Density Function, plotting options for a given set of data.

## File Descriptions <a name="files"></a>

Inside the distributions folder there are 3 '.py' files that correspond to each one of the distributions considered. The 'Genearldistribution.py' in the same folder contains a method to initialize and to read data files that correspond to any distribution. The test.py provides unit tests and the numbers_binomial.txt and numbers_gaussian.txt are example of data files with data that correspond to these distributions.

## Usage <a name="usage"></a>
 Install the package using `pip install .` (from inside the directory that you have downloaded it)
### For Gaussian distributions
1. From a python shell first import the necessary module for Gaussian (normal) distributions
   `from distributions import Gaussian`
2. To load the data file from which we will calculate different properties of a specific  distribution use e.g. `gaussian_1=Gaussian("file_path")`.
The format of the file should be a single column of numbers (see e.g. `"numbers_gaussian.txt"`). 
 3. 
   * To plot a histogram of the data:
   `gaussian_1.plot_histogram()`
    ![Histogram Gaussian](https://github.com/iris-theof/distributions_package/blob/master/Histogram_Gaussian..png)
  * To plot the Propability Density Function (PDF) and the normed histogram of data:
   `gaussian_1.histogram_pdf()`
   ![PDF Gaussian](https://github.com/iris-theof/distributions_package/blob/master/PDF_Gaussian.png)
   * To calculate the parameters of the distribution:
   `gaussian_1` (it will display the mean and the variance of the gaussian)
   * To calculate the mean:
   `gaussian_1.mean`
   * To calculate the standard deviation:
   `gaussian_1.stdev`
   * To calculate the PDF at a certain point x (e.g. 40)
    `gaussian_1.pdf(40)`
    
### For Binomial distributions
1. From a python shell first import the necessary module for Binomial distributions
   `from distributions import Binomial`
2. To load the data file from which we will calculate different properties of a specific distribution use e.g. `binomial_1=Binomial("file_path")`. The format of the file should be a single column of numbers that are either 0 or 1 (see e.g. `"numbers_binomial.txt"`). 
3. 
 * To plot the total number of successes (1) and failures (0) in a bar chart:
    `binomial_1.plot_bar()`
    ![Bar Plot Binomial](https://github.com/iris-theof/distributions_package/blob/master/Bar_plot_Binomial.png)
  * To plot the Propability Mass Function (PMF) for number of successes k:
  `binomial_1.plot_bar_pmf()` 
  ![PMF Binomial]( https://github.com/iris-theof/distributions_package/blob/master/PMF_Binomial.png)
  * To calculate the success propability of the distribution p:
  `binomial_1.p`
  * To calculate the number of trials n:
  `binomial_1.n`
  * To calculate the mean:
  `binomial_1.calculate_mean()`
  * To calculate the standard deviation:
  `binomial_1.calculate_stdev()`
  * To calculate the parameters of the distribution:
   `binomial_1` (it will display the numbers of trials n, and the success propability of each trial p)
  * To calculate the PMF at k which is the number of successes (e.g. for k=2)
  `binomial_1.pmf(2)`. One needs to be careful as k needs to be a positive integer.
 
 ### For Bernoulli distributions
 1. From a python shell first import the necessary module for Binomial distributions
   `from distributions import Bernoulli`
 2. To load the data file from which we will calculate different properties of a specific distribution use e.g. `bernoulli_1=Bernoulli("file_path")`. The format of the file should be a single column of numbers that are either 0 or 1 (see e.g. `"numbers_binomial.txt"`). Note that we use for our example and unit tests the same file as the one for the Binomial distribution, since it serves our purpose. 
 3.  
 * To plot the propability of success (1) and failure (0) in a bar chart:
 `bernoulli_1.plot_bar()` 
 ![Bar Plot Bernoulli](https://github.com/iris-theof/distributions_package/blob/master/Bar_plot_Bernoulli.png)
 * To calculate the success propability of the distribution p:
  `bernoulli_1.p`
  * To calculate the mean:
  `bernoulli_1.calculate_mean()`
  * To calculate the standard deviation:
  `bernoulli_1.calculate_stdev()`
  * To calculate the parameters of the distribution:
   `bernoulli_1` (it will display the success propability p and the failure propability q)
  * To calculate the PMF for k=1 (success) or k=0 (failure)
  `bernoulli_1.pmf(0)`. 

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Feel free to use the code in this repository as you would like! 
The original code for the Gaussian and Binomial code distributions was taken from the PyPi package distributions. 

