import numpy as np

import simulation as sm

import analysis as an

import plot

# bisogna caricare un file csv con ogni riga contente i parametri della simulazione
# si avrà un array di parametri
# https://numpy.org/doc/stable/user/basics.creation.html
# parameters format = size_population, #interactions(unico parametro per tutti), #generations(unico parametro per tutti), Punishment, Reward, #controls
parameters=list() # contenitore dei parametri per ogni lista, fare una namedtupla

# confrontare frequenze con popolazione fissa e le varie combo di controlli
#(punire, premiare, entrambi, variare il numero di controlli)
# poi provare con differenti quantità di popolazioni e interazioni
# togliere varaibili globali

def main():
    
    csv=np.genfromtxt('https://raw.githubusercontent.com/MatteoPiraccini/CooperationVsAuthority/main/Parameters.csv', delimiter=',', skip_header=1)
    
    print(csv)
    
    ls_parameters=[]
    
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

    populations=np.array(sm.init_simulation(par[0]), np.byte) # cercare di eliminarlo

    assert np.shape(populations) == (1,2, par[0])

    data_list=[] #cercare di spostarla in simulation

    for n_simulations in range(len(par)):
    
        data_list.append((sm.evolution(par[1][n_simulations], par[2][n_simulations], populations)))

    data=np.array(data_list)

    results=an.analize_simulations(data)


    plot.draw_data(results[0], parameters)

