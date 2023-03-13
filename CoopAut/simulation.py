import numpy as np
 

def init_simulation(population_size):

    """

    Create the 0-generation with casual strategies and zero sources

    Parameters:

    -----------------------------
    
    population_size: int, indicate numerosity of the population
	
    -----------------------------

    Return an array with dimension (1,2,size_population), there will be store data
	
    """


    population=np.zeros((1,2,population_size), np.byte) 
	
    population[0][0] = np.array(random_int(-5, +7, (1, population_size), np.byte)) 

    return population

		
# this function is for separate stochastic part from the deterministic one of
# the simulation for testing

def random_int(low_value, high_value, shape, dtype=np.byte):
    
    """

    Generate an array of random int

    Parameters:

    -----------------------------
        
    low_value: int, inferior value (included)
        
    high_value: int, superior value (excluded)
        
    shape: int, shape of the values generated
        
    dtype: type of the generated values, by default is np.byte
    	
    -----------------------------

    Return an array with dimension (shape) with casual int values from
    
    [low_value, high_value)
    	
    """
    # to testing the same number
    
    #np.random.seed(1)
    
    return np.random.randint(low_value, high_value, shape, dtype)

   
def interaction(donator, recipient, onlookers, 
                
                strategy_array, sources_array, image_matrix, 
                
                punishment, reward, controls):
    
    """

    Simulation of a pair of individuals, donator-reipient, interact and donator 
    
    decide whether cooperate

    Parameters:

    -----------------------------
	
    donator: int, index that rappresent an individual from the population that 
    
    could cooperate

    recipient: int, index that rappresent an individual from the population that
    
    maybe receive

    onlookers: array (1,10), indexes of indivuals that observe the 
    
    interaction

    strategy_array: array (1, size of population), the strategies for 
    
    each individuals

    sources_array: array (1, size of population), the sources for each 
    
    individuals

    image_matrix: array (size of poplutation)**2, matrix of image scores
    
    punishment: bool, to indicate if punishment is on
    
    reward: bool, to indicate if punishment is on
    
    controls: array 1-D, indexes of the people controlled
    
    -----------------------------
    
    Return nothing.
    
    """
    # no sense controls without a consequence
    
    if np.logical_not(punishment | reward):
        
        controls = []
    
    # by default donator not cooperate
    
    bonus=-1
    
    # controls if donator cooperate

    if strategy_array[donator]<image_matrix[donator][recipient]:
		
        bonus=1

        sources_array[recipient]+=1
        
    #apply consequences of the choice of donator
    
    # the controls effects are here to simplify the code, no theorical reason
  
    if (np.any(controls==recipient) | np.any(controls==donator)):
        
        #the source cannot be a negative value
        
        if (punishment & (bonus == -1) &  sources_array[donator]>0):
            
            sources_array[donator]+=bonus
            
            image_matrix[:,donator]+=bonus
            
        if (reward & (bonus == 1)):
            
            sources_array[donator]+=bonus
            
            image_matrix[:,donator]+=bonus
    
    # if controls catch no one, the consequences are limitated only to a 
    
    #restricted group
       
    else:
        
        image_matrix[recipient][donator]+=bonus
        
        for x in range(len(onlookers)):

            image_matrix[onlookers[x]][donator]+=bonus
        


def new_generation(strategy, sources):
    
    
    """
    Creation of the next generation; each indivuals has an offspring
    
    based on its sources.
    
    Parameters:
        
    -----------------------------
        
    strategy: array (1, size of population), strategy of each individual
    
    sources: array (1, size of population), sources of each individual
    
    -----------------------------
    
    Return an array (1, size of population) of the strategies of the individual 
    
    of the new generation 
   
    """
    
    tot_sources=np.sum(sources)
    
    # if nothing change
    
    if tot_sources==0:
        
        return strategy
    
    # to count the total number of individuals
    
    tot_pop=len(strategy) 
    
    # to save time later by not using /
        
    inv_tot_sources=np.float16(1/tot_sources)
    
    #in this array will be store the strategies of the new generation
    
    new_strategy=np.full_like(strategy, -7)
    
    proportions = np.float16(sources*inv_tot_sources)
    
    offspring = np.float16(tot_pop*proportions)
    
    # integers and fractional parts of the proportions need a separate treatment
    # for the calculus of the offsprings
    
    frac_offspring = np.array(np.modf(offspring)[0], np.float16)
    
    int_offspring = np.array(np.modf(offspring)[1], np.byte)
    
    # where to add the computed offspring
    
    curr_index = 0
    
    for individual in range(tot_pop):
        
        if int_offspring[individual] == 0:
            
            continue
        
        appendix = np.full(int_offspring[individual], strategy[individual], np.byte)
               
        new_strategy [curr_index : curr_index+len(appendix)] = appendix
        
        curr_index += len(appendix)
        
    # add strategies based on the fractional part

    while curr_index < tot_pop:
        
        appendix= strategy[np.argmax(frac_offspring)]
        
        new_strategy[curr_index] =  appendix
        
        frac_offspring[np.argmax(frac_offspring)] = 0
        
        curr_index += 1
            
    return new_strategy
            
    
def life_cycle(population, N_interactions, punishment, reward, N_controls, mutation_off):
    
    
    """
    Implemantation of a life cycle of a generation with interactions and 
    
    the arise of the next generation based on sources with possibility of mutations
    
    Parameters:
    
    -----------------------------
    
    population: array (2, size of population), strategy (0-row) and sources (1-row) 

    of each individuals
    
    N_interactions: int, how many interactions are iterated
    
    punishment: bool, to indicate if punishment is on
        
    reward: bool, to indicate if punishment is on
    
    N_controls: int, number of individual to be controled for each interaction

    mutation_off: bool, if the mutations are presents
    
    -----------------------------
    
    Return two arrays (size of population), first with the sources of the 
    
    old generation, the other with strategies of the new one
    
    """
    
    strategy = population[0]
    
    population_size = len(population[0])

    # new image scores matrix for each generation
    
    image_matrix = np.zeros((population_size, population_size), np.byte)
    
    # new sources array for each generation
    
    sources = np.zeros_like(strategy, np.byte)
    
    # create an array with all indexes for the next choice functions
    
    population_indexes = np.arange(population_size)
    
    for x in range(N_interactions):
        
        #DRandO = Donator, Recipient and Onlookers
        
        DRandO = np.random.choice(population_indexes, 12, False)
        
        controls = np.random.choice(population_indexes, N_controls, False)
        
        interaction(DRandO[0], DRandO[1], DRandO[-10:], strategy, sources, image_matrix, punishment, reward, controls)
    
    # useful for further implentation
    
    old_sources=np.array(sources)
    
    new_population = new_generation(strategy, sources)
    
    np.random.shuffle(new_population)
    
    new_population = mutations(mutation_off, new_population)
    
    return old_sources, new_population


def mutations(off, population):
    """
    Implemantation of mutations in the strategy of the population
    
    Parameters:
    
    -----------------------------
    mutation_off: bool, if the mutations are presents

    population: array (size of population), the strategy of the population without 

    mutation
    
    -----------------------------
    
    Return the same array if there is no mutations, otherwise the array of the 

    mutated population
    
    """
    
    if off == True:
        
        return population
    
    strategy = np.arange(-5,7,1, np.byte )
    
    p_mutations = np.array(np.random.randint(0, 1000, len(population)))
    
    mutated = np.nonzero(p_mutations == 0)[0]
    
    if mutated == []:
        
        return population
    
    for i in mutated:
        
        st = strategy [strategy != population[i]]
        
        population[i] = np.random.choice(st, 1)
        
    return population
    



def evolution(N_interactions, N_generation, populations, punishment, reward, controls, mutation_off):
    
    """
    Evolution of the various generations
    
    Parameters:
    
    -----------------------------
    
    N_interactions: int, how many interactions are iterated
    
    N_generation: int, how many generations are iterated
    
    populations: array (2, size of population), strategy (0-row) and sources (1-row) 

    of the 0-generation
   
    punishment: bool, to indicate if punishment is on
       
    reward: bool, to indicate if punishment is on
   
    N_controls: int, number of individuals to be controled for each interaction

    mutation_off: bool, if the mutations are presents
    
    -----------------------------
    
    Return array (N_generation, 2, size of population) with strategies and
    
    sources for each generation
    
    """  

    for generation in range(N_generation):
        
        old_sources, new_strategies = np.array(life_cycle(populations[generation], N_interactions, punishment, reward, controls, mutation_off), np.byte)
        
        populations[generation][1] = old_sources
        
        new_population = np.vstack((new_strategies, np.zeros_like(new_strategies)), dtype=np.byte)
        
        populations=np.append(populations, [new_population], axis=0)
        
        # visual aid to understand how proceed
        
        print('Generazione', generation)
        
    return populations