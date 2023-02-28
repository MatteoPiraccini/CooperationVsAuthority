import matplotlib.pyplot as plt

import numpy as np

from matplotlib import colors

from matplotlib.ticker import PercentFormatter

def draw_data(data):
    
    """

    Create the 0-generation

    Parameters:

    -----------------------------
	
    data: an array with the frequencies of strategies in each simulation
    
    -----------------------------

    Returns a tupla with a 3D array with data about the 0-generation, the matrix of reputation and an array that store the amount of every types of individual
	
    """
    
    rows = np.ceil(len(data)/3)

    fig, axs = plt.subplots(rows , 3, sharey=True, tight_layout=True)

    # We can set the number of bins with the *bins* keyword argument.
    
    for N_simulation in range(len(data)):
        
        axs[N_simulation].hist(data[N_simulation], bins=len(data[N_simulation]))# istogrammi o stem?
        
   plt.show()  
        