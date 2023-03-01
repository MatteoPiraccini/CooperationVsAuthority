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

n_generation=[2] # esclusa la 0

n_interactions=[125]

tot_simulations=1

populations=np.array(sm.init_simulation(), np.byte) # cercare di eliminarlo

assert np.shape(populations) == (1,2,100)

data_list=[] #cercare di spostarla in simulation

for n_simulations in range(tot_simulations):
    
    data_list.append((sm.evolution(n_generation[n_simulations], n_interactions[n_simulations], populations))) ### deve fare tutto in colpo solo con diversi tipi di simulazione

data=np.array(data_list)

an.analize_simulations(data)

# manca l'analisi

plot.draw_data(data, parameters)

# creare file csv con tutti i dati
