#!/usr/bin/python

###############################################################################
# This script is used for doing the plot of the demographic history of        #
# a random-mating population from a ms command. At the same time, the script  #
# allows to plot (in the same figure) the demographic history infered by the  #
# PSMC software.                                                              #
###############################################################################

import matplotlib.pyplot as plt

# Set the values of these global variables
#==============================================================================

# Bin size used to generate the imput of PSMC (default is 100)
BIN_SIZE = 100

# Mutation rate per base per generation
MUTATION_RATE = 2.5e-8

# Number of years per generation
GENERAITON_TIME = 6

# Size of the plot
X_MIN = 1e4
X_MAX = 1e7
Y_MIN = 0
Y_MAX = 5e4

# What plot to do
PLOT_MS = False
PLOT_PSMC_RESULTS = True
#==============================================================================

def psmc2fun(PSMC_RESULTS, s=BIN_SIZE, u=MUTATION_RATE):

    with open(PSMC_RESULTS, 'r') as a:
        result = a.read()

    # getting the time windows and the lambda values
    last_block = result.split('//\n')[-2]

    last_block = last_block.split('\n')

    time_windows = []
    estimated_lambdas = []
    for line in last_block:
        if line[:2]=='RS':
            time_windows.append(float(line.split('\t')[2]))
            estimated_lambdas.append(float(line.split('\t')[3]))


    # getting the estimations of theta for computing N0
    result = result.split('PA\t') # The 'PA' lines contain the values of the
                                  # estimated parameters
    result = result[-1].split('\n')[0]
    result = result.split(' ')
    theta = float(result[1])
    N0 = theta/(4*u)/s

    # Scalling times and sizes
    times = [GENERAITON_TIME * 2 * N0 * i for i in time_windows]
    sizes = [N0 * i for i in estimated_lambdas]

    return(times, sizes)

if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.add_subplot(111)

    if PLOT_MS:
        (real_times, real_sizes) = ms2fun(MS_COMMAND, MUTATION_RATE)
        ax.step(real_times, real_sizes, where='post', linestyle='-', color='k', label = "Real history")

    if PLOT_PSMC_RESULTS:
        (estimated_times, estimated_sizes) = psmc2fun(PSMC_RESULTS, BIN_SIZE, MUTATION_RATE)
        ax.step(estimated_times, estimated_sizes, where='post', color='r', label = "PSMC estimated history")

    ax.set_xlabel("Time in years (25 years/generation)")
    ax.set_ylabel("Effective size (x 10^4)")
    ax.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    ax.grid(True)
    ax.set_xlim(X_MIN, X_MAX)
    ax.set_ylim(Y_MIN, Y_MAX)
    ax.set_xscale('log')
    plt.legend(loc = 'best')

    plt.show()
