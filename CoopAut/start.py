import numpy as np

from sys import argv

import simulation as sm

import analysis as an

import plot       

# check if the values of parameters are accetable

def check_parameters(parameters):
     
     """
     
     Control if the values passed to the program are valid
     
     Parameters:

     -----------------------------
 	
     parameters: array (N of simulations, 12), all the parameters from the csv file
     
     -----------------------------
     
     """
     
     for i in range (len(parameters)):
         
         if (parameters[i][0] < 12) | (parameters[i][0] > 255):
             
             raise ValueError (" size_population is out of range")
             
         if (parameters[i][1] < 1) | (parameters[i][1] > 255):
             
             raise ValueError (" N_interactions is out of range")
             
         if (parameters[i][2] < 1) | (parameters[i][2] > 4294967294):
             
             raise ValueError (" N_generations is out of range")
             
         if (parameters[i][5] < 0) | (parameters[i][0] > parameters[i][0]):
             
             raise ValueError (" N_controls is out of range")
      
        
      
# the programe start from here

# arguments: path for the parameter file, seed for random number

path = argv[1]

                  
if path[-4:] != '.csv':
    
                  raise Exception ("The extension must be .csv")

seed = int(argv[2])

np.random.seed(seed)

csv = np.genfromtxt(path, delimiter=',', skip_header=1, ndmin=2)
    
check_parameters(csv)
    
ls_parameters = []
    
for n_simulation in range(len(csv)):
        
        row = (np.ubyte(csv[n_simulation][0]), # size of population
                                                
               np.ubyte(csv[n_simulation][1]), # N of interactions
                                                
               np.uintc(csv[n_simulation][2]), # N of generations
                                                
               np.bool_(csv[n_simulation][3]), # Punishment
                                                
               np.bool_(csv[n_simulation][4]), # Reward
                                                
               np.ubyte(csv[n_simulation][5])) # N of controls
        
        ls_parameters.append(row)
        
# to fix parameters
        
par = tuple(ls_parameters)
    


data_list = [] 

for n_simulation in range(len(par)):
        
        # 1°-dim: generation, 2°-dim: strategy/sources, 3°-dim: individual
        
        populations = np.array(sm.init_simulation(par[n_simulation][0]), np.byte) # cercare di eliminarlo
    
        data_list.append((sm.evolution(par[n_simulation][1], par[n_simulation][2], populations, par[n_simulation][3], par[n_simulation][4], par[n_simulation][5])))

data = np.array(data_list)

results = an.analize_simulations(data)

# save means into a file in the same directory

np.savetxt('Results.csv', np.column_stack((results[0],results[1])), delimiter=',',fmt='%10.5f')


plot.draw_data(results[0], par)
    
    

    
       
         
