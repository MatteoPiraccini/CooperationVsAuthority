import matplotlib.pyplot as plt

# to show only the grid for vertical axe

plt.rcParams["axes.grid"] =True

plt.rcParams["axes.grid.axis"] ="y"

import numpy as np


# frequencies of the strategies are stored in such way: 0 1 2 3 4 5 6 -5 -4 -3 -2 -1
# for the plot we need this way: -5 -4 -3 -2 -1 0 1 2 3 4 5 6

def reorganize_data(data):
    
    """

    Split and rearrange the array of frenquencies

    Parameters:

    -----------------------------
	
    data: array (N of simulations, 12), frequencies
    
    -----------------------------

    Returns an array (N of simulations, 12) rearrange
	
    """
    
    re_data = np.hsplit(data, np.array([7, 12]))
    
    re_data = np.hstack((re_data[1],re_data[0]))
    
    return re_data

def draw_data(data, par):
    
    """

    Generate a series of stem plot with the frequencies of strategies

    Parameters:

    -----------------------------
	
    data: array (N of simulations, 12), frequencies
    
    -----------------------------

	
    """
    
    # for a better readibility on the plot
    
    data = reorganize_data(data)
    
    # we need always a 2D array
    
    if np.shape(data) == (12,):
        
        data=[data]
        
    # on a row we want most three subplot
    
    rows = int(np.ceil(len(data)/5))

    fig, axs = plt.subplots((rows if rows<4 else 3) , 5, sharey=True, tight_layout=True)
    
    plt.xticks(np.arange(-4,7,2 ))
    
    plt.yticks(np.arange(0.0, 0.95, 0.05))
    
    string=''
    
    n_simulation=0
    
    # we always need a 2D axs
    
    if rows == 1:
    
        axs=[axs]
    
    for row in range(rows):
        
        if row > 3:
            
            break
        
        for column in range(5):
            
            if n_simulation > len(data)-1:
                
                break
        
            axs[row][column].stem(np.arange(-5,7), data[n_simulation], markerfmt=',', basefmt=None)
            
            if (par[n_simulation][3] & np.logical_not(par[n_simulation][4])):
                
                string='Punishment'
                
            if (par[n_simulation][4] & np.logical_not(par[n_simulation][3])):
                
                string='Reward'
                
            if (par[n_simulation][4] & par[n_simulation][3]):
                
                string='Punishment&Reward'
            
            axs[row][column].title.set_text('Pop.size= '+str(par[n_simulation][0])+' '+ string+ ' Controls= '+ str(par[n_simulation][5]))
            
            axs[row][column].set_xlabel('Strategy, k')
            
            axs[row][column].set_ylabel('Frequencies')
            
            n_simulation+=1
            
    plt.title(label='Results')
        
    plt.show()  
        