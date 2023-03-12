import numpy as np

import simulation as sm

import analysis as an

import plot

#############################################
##TEST for simulation.py


def random_int(low_value, high_value, size, dtype):
    
    """
    This function is for generate fixed random number
    
    Parameters:

    -----------------------------
    low_value: int, inferior value (included)
        
    high_value: int, superior value (excluded)
        
    shape: int, shape of the values generated
        
    dtype: type of the generated values
    -----------------------------
    """

    np.random.seed(11)

    return np.random.randint(low_value, high_value, size, dtype)
	

def testing_interaction():
    
    """
    This function is for testing sm.interaction()
    """

    size_pop=20
    
    fake_indexes= np.random.choice(np.arange(size_pop), 12, False)

    strategy=np.array(random_int(-5,7,size_pop, dtype=np.byte))

    sources=np.array(random_int(0,4,size_pop, np.byte))

    image=np.array(random_int(-4,7, (size_pop,size_pop), np.byte))

    print(fake_indexes)

    print(sources,)
    
    print(image[:, fake_indexes[0]])
	
    sm.interaction( fake_indexes[0], fake_indexes[1], fake_indexes[-10:], strategy, sources, image, True, True, [])

    
    print(sources, 
          
          strategy[fake_indexes[0]],
          
          ' >=', 
          
          image[fake_indexes[0]][fake_indexes[1]], 
          
          image[:, fake_indexes[0]], 
          
          sep='\n')


def test_new_generation_one_offspring():
    
    """
    Testing new_generation if one individuals have sources and others not. 
    
    The result must be that the next generation is  composed only by its 
    
    offspring
    
    GIVEN: I have two arrays: strategy and sources
    WHEN: I perform the new_generation() function
    THEN: the new generation show the right offspring
    """

    fake_strategy=np.full(10, 0, np.byte)
    
    fake_sources=np.zeros(10, np.byte)
    
    fake_strategy[3] = 2
    
    fake_sources[3] = 1

    new_generation = sm.new_generation(fake_strategy, fake_sources)
    
    assert np.all(new_generation == np.full_like(fake_strategy, 2))

def test_new_generation_many_offspring():
    
    """
    Testing if new_generation give the correct results with a given array of 
    
    strategies and a given array with sources
    
    GIVEN: I have two arrays: strategy and sources
    WHEN: I perform the new_generation() function
    THEN: the new generation show the right offspring
    """

    fake_strategy= np.array( [-1, 3, -2, 0, 1, 1, 1, -2, 6, 3])
    
    fake_sources= np.array( [1, 0, 2, 0, 2, 5, 1, 3, 1, 0])
    
    new_generation = sm.new_generation(fake_strategy, fake_sources)
    
    assert np.all(new_generation == [-2, 1, 1, 1, 1, -2, -2, -1, 1, 6])

def test_new_generation_same():
    
    """
    Testing if new_generation return the same array if all individuals have the
    
    same sources
    
    GIVEN: I have two arrays: strategy and sources
    WHEN: I perform the new_generation() function
    THEN: the new generation show the right offspring
    """

    fake_strategy= np.array( [-1, 3, -2, 0, 1, 1, 1, -2, 6, 3])
    
    fake_sources= np.full_like(fake_strategy, 0)
    
    new_generation = sm.new_generation(fake_strategy, fake_sources)
    
    assert np.all(new_generation == fake_strategy)
    
def testing_mutation():
    
    a = np.zeros(1000)
    
    b = np.zeros(1000)
    
    a=sm.mutations(True, a)
    
    

         
def testing_life_cycle():
 
    """
    This function is for testing sm.lifecycle()
    """
    
    size=20
    
    fake_population=[sm.random_int(-5, 7, size, np.byte), np.array(sm.random_int(0, 7, size, np.byte), np.byte)]
    
    print(sm.life_cycle(fake_population, 3, False, True, 10))
    
def testing_simulation():
    
    fake_par=(20, 0, 2, False, False, 10 )
    
    populations=sm.init_simulation(fake_par[0])
    
    print(populations)

    data_list=(sm.evolution(fake_par[1], fake_par[2], populations, fake_par[3], fake_par[4], fake_par[5]))
    
    print(data_list)
    
    
    
#########################################################
## TEST for analysis.py
    
def testing_an_strategy():
    
    """
    This function is for testing analysis.py
    
    """
    
    fake_n_gen=3
    
    fake_size_pop=10
    
    fake_data= random_int(-5, 7, (fake_n_gen, 2, fake_size_pop), np.byte)
    
    print(fake_data)
    
    print(an.frequency_strategies(fake_data))
    
#########################################################
## TEST for plot.py
    
def testing_plot():
    
    """
    This function is for testing plot.draw_data.py
    
    """
    
    n_simulations=7
    
    fake_data=(np.random.uniform(0.0, 0.25, (n_simulations,12)))
    
    # ci vogliono i parametri
    
    ls=(2,3,4,True, False,2)
    
    parameters=()
    
    for i in range(n_simulations):
        
        parameters=(*parameters, ls)
    
    plot.draw_data(fake_data, parameters)
    

    
def testing_reorganize():
    
    """
    This function is for testing plot.reorganize_data()
    
    """
    
    fake_data=np.array([[0,1,2,3,4,5,6,-5,-4,-3,-2,-1] for i in range(10)])
    
    print(fake_data)
    
    print(plot.reorganize_data(fake_data))
    
    
###########################################################
## TEST for start.py


    
def not_a_mess_with_append():
    
    """
    This function is for testing the behavior of append and if it work under a
    
    certain way
    
    """
    
    size=5
    
    populations=np.zeros((1,2,size), np.byte)
    
    generation=0
    
    old_sources= np.empty(size, np.byte)
    
    new_population = np.array(np.vstack((np.ones(size, np.byte),np.zeros_like(old_sources))))
    
    print(populations, old_sources, new_population, sep='\n\n')
    
    populations[generation][1]=old_sources
    
    populations=np.append(populations, np.array([new_population], np.byte), axis=0)
    
    print('\n\n', populations, '\n\n\n')
    
    
    assert np.shape(populations) == (2,2,size)
    
    print(populations[1][0])
    
    print(populations[0][1])
    
          
def try_main():
    
    """
    This function is for testing the code in start.py
    
    """
    
    n_generation=[2, 1] # esclusa la 0

    n_interactions=[100, 190]

    tot_simulations=2

    populations=np.array(sm.init_simulation(), np.byte)
    
    assert np.shape(populations) == (1,2,100)

    data_list=[]

    for n_simulations in range(tot_simulations):
        
        data_list.append((sm.evolution(n_generation[n_simulations], n_interactions[n_simulations], populations))) ### deve fare tutto in colpo solo con diversi tipi di simulazione

    data=tuple(data_list)
    
    print(data)
    
def try_to_import():
    
    """
    This function is for testing if the data for the parameters are imported correctly
    
    """
    
    csv=np.genfromtxt('https://raw.githubusercontent.com/MatteoPiraccini/CooperationVsAuthority/main/Parameters.csv', delimiter=',', skip_header=1)
    
    print(csv)
    
    ls_parameters=[]
    
    # max parameters : 255, 255
    
    for n_simulation in range(len(csv)):
        
        tupla=(np.ubyte(csv[n_simulation][0]),
                                                
                                                np.ubyte(csv[n_simulation][1]),
                                                
                                                np.uintc(csv[n_simulation][2]),
                                                
                                                np.bool_(csv[n_simulation][3]),
                                                
                                                np.bool_(csv[n_simulation][4]),
                                                
                                                np.ubyte(csv[n_simulation][5]))
        
        ls_parameters.append(tupla)
    
    print(ls_parameters)
    
def test_export():
    
    """
    This function is for testing export of data
    
    """
    
    fake_data= np.ones((2,10))
    
    np.savetxt('Prova.csv', fake_data, delimiter=',',fmt='%10.5f')