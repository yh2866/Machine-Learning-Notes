import matplotlib.pyplot as plt
import numpy as np

def plotData(data):
    """
    plots the data points and gives the figure axes labels of
    population and profit.
    """

# ====================== YOUR CODE HERE ======================
# Instructions: Plot the training data into a figure using the
#               "figure" and "plot" commands. Set the axes labels using
#               the "xlabel" and "ylabel" commands. Assume the
#               population and revenue data have been passed in
#               as the x and y arguments of this function.
#
# Hint: You can use the 'rx' option with plot to have the markers
#       appear as red crosses. Furthermore, you can make the
#       markers larger by using plot(..., 'rx', 'MarkerSize', 10);

	data = np.loadtxt('data/ex1data1.txt', delimiter=',')

	X = np.c_[np.ones(data.shape[0]),data[:,0]]
	y = np.c_[data[:,1]]


	plt.scatter(X[:,1], y, s=30, c='r', marker='x', linewidths=1)
	plt.xlim(4,24)
	plt.xlabel('Population of City in 10,000s')
	plt.ylabel('Profit in $10,000s');
    #plt.figure()  # open a new figure window

# ============================================================
