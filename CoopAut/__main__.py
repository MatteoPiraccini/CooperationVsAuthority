import numpy as np

import simulation as sm

import analysis as an

import plot

# https://numpy.org/doc/stable/user/basics.creation.html
# parameters format = size_population, #interactions(unico parametro per tutti), #generations(unico parametro per tutti), Punishment, Reward, #controls

# confrontare frequenze con popolazione fissa e le varie combo di controlli
#(punire, premiare, entrambi, variare il numero di controlli)
# poi provare con differenti quantità di popolazioni e interazioni
# togliere varaibili globali

def main():
    
    csv=np.genfromtxt('Parameters.csv', delimiter=',', skip_header=1, ndmin=2)
    
    # non si aggiorna, crea cartella e crea il file, che poi ripesca sempre
    
    print(csv)
    
    ls_parameters=[]
    
    print(len(csv)) #se metti una sola riga dopo ti dà gli elementi della riga
    
    # max parameters : 255, 255
    
    for n_simulation in range(len(csv)):
        
        row=(np.ubyte(csv[n_simulation][0]), #size of population
                                                
               np.ubyte(csv[n_simulation][1]), #N of interactions
                                                
               np.uintc(csv[n_simulation][2]), #N of generations
                                                
               np.bool_(csv[n_simulation][3]), #Punishment
                                                
               np.bool_(csv[n_simulation][4]), #Reward
                                                
               np.ubyte(csv[n_simulation][5])) #N of controls
        
        ls_parameters.append(row)
        
    par = tuple(ls_parameters)

    data_list=[]
    

    for n_simulation in range(len(par)):
        
        populations=np.array(sm.init_simulation(par[n_simulation][0]), np.byte) # cercare di eliminarlo
    
        data_list.append((sm.evolution(par[n_simulation][1], par[n_simulation][2], populations, par[n_simulation][3], par[n_simulation][4], par[n_simulation][5])))

    data=np.array(data_list)

    results=an.analize_simulations(data)


    plot.draw_data(results[0], par)
    
    
