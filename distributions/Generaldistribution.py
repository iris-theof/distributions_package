class Distribution:

	def __init__(self, file_name='name'):

		""" Generic distribution class for calculating and
		visualizing a probability distribution.

		Attributes:
			mean (float) representing the mean value of the distribution
			stdev (float) representing the standard deviation of the distribution
			data_list (list of floats) a list of floats extracted from the data file
			"""

		self.data = []

		with open(file_name) as file:
			data_list = []
			line = file.readline()
			while line:
				data_list.append(int(line))
				line = file.readline()
		file.close()

		self.data = data_list
