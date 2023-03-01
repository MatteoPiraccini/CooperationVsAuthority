import matplotlib.pyplot as plt

plt.rcParams["axes.grid"] =True

plt.rcParams["axes.grid.axis"] ="y"

import numpy as np

from matplotlib import colors

def reorganize_data(data):
    
    print(np.shape(data))
    
    re_data = np.hsplit(data, np.array([7, 12]))
    
    re_data = np.hstack((re_data[1],re_data[0]))
    
    return re_data

def draw_data(data, parameters):
    
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
    
    rows = int(np.ceil(len(data)/3))

    fig, axs = plt.subplots(rows , 3, sharey=True, tight_layout=True)
    
    plt.xticks(np.arange(-4,7,2 ))
    
    plt.yticks(np.arange(0.0, 0.35, 0.05))
    
    string=''
    
    N_simulation=0
       
    for row in range(rows):
        
        for column in range(3):
            
            if N_simulation > len(data)-1:
                
                break
        
            axs[row][column].stem(np.arange(-5,7), data[N_simulation], markerfmt=',', basefmt=None)
            
            if (parameters[N_simulation][3] & np.logical_not(parameters[N_simulation][4])):
                
                string='Punishment'
                
            if (parameters[N_simulation][4] & np.logical_not(parameters[N_simulation][3])):
                
                string='Reward'
                
            if (parameters[N_simulation][4] & parameters[N_simulation][3]):
                
                string='Punishment&Reward'
            
            axs[row][column].title.set_text('Pop.size= '+str(parameters[N_simulation][0])+' '+ string+ ' Controls= '+ str(parameters[N_simulation][5]))
            
            axs[row][column].set_xlabel('Strategy, k')
            
            axs[row][column].set_ylabel('Frequencies')
            
            N_simulation+=1
            
    plt.title()
        
    plt.show()  
        