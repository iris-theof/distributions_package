
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
1. Install the package using `pip install .` (from inside the directory that you have downloaded it)
2. From a python shell first import the corresponding modules, e.g. for Gaussian
   `from distributions import Gaussian`
3. To load the data file from which we will calculate different properties of a specific distribution use e.g.
   `gaussian_1=Gaussian("file_path")`
  * To plot the propability density function and the normed histogram of data:
   `gaussian_1.histogram_pdf()`
   ![PDF Gaussian](https://github.com/iris-theof/distributions_package/blob/master/PDF_Gaussian.png)
   * To plot a histogram of the data:
   `gaussian_1.plot_histogram()`
    ![Histogram Gaussian](https://github.com/iris-theof/distributions_package/blob/master/Histogram_Gaussian..png)
   * To calculate the parameters of the distribution:
   `gaussian_1` (in case of a gaussian it will show the mean and the standard deviation)
   * To calculate the mean
   `gaussian_1.mean`
   * To calculate the standard deviation
   `gaussian_1.stdev`
   * To calculate the Propability Density Function (PDF) at a certain point x (e.g. 40)
    `gaussian_1.pdf(40)`


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Feel free to use the code in this repository as you would like! 
The original code for the Gaussian and Binomial code distributions was taken from the PyPi package distributions. 

