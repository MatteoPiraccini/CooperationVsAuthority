import matplotlib.pyplot as plt

plt.rcParams["axes.grid"] =True

plt.rcParams["axes.grid.axis"] ="y"

import numpy as np

def reorganize_data(data):
    
    re_data = np.hsplit(data, np.array([7, 12]))
    
    re_data = np.hstack((re_data[1],re_data[0]))
    
    return re_data

def draw_data(data, par):
    
    """

    Create the 0-generation

    Parameters:

    -----------------------------
	
    data: an array with the frequencies of strategies in each simulation
    
    -----------------------------

    Returns a tupla with a 3D array with data about the 0-generation, the matrix of reputation and an array that store the amount of every types of individual
	
    """
    
    # for a better readibility
    
    data=reorganize_data(data)
    
    if np.shape(data) == (12,):
        
        data=[data]
    
    rows = int(np.ceil(len(data)/3))

    fig, axs = plt.subplots(rows , 3, sharey=True, tight_layout=True)
    
    plt.xticks(np.arange(-4,7,2 ))
    
    plt.yticks(np.arange(0.0, 0.35, 0.05))
    
    string=''
    
    n_simulation=0
    
    if rows == 1:
    
        axs=[axs]
    
    for row in range(rows):
        
        for column in range(3):
            
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
        