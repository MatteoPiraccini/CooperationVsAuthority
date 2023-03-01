import numpy as np

# implementare l'interruttore per attivare i controlli e quanto frequenti

# 

def init_simulation(population_size): # che parametri ci vanno? Probabilmente questa funzione è inutile

    """

    Create the 0-generation

    Parameters:

    -----------------------------
	
    -----------------------------

    Returns a tupla with a 3D array with data about the 0-generation, the matrix of reputation and an array that store the amount of every types of individual
	
    """

	#creation of the 0-generation

    population=np.zeros((1,2,population_size), np.byte) # 1°-dim: generation, 2°-dim: strategy/sources, 3°-dim: individual
	
    population[0][0] = np.array(random_int(-5, +7, (1, population_size), np.byte)) #7 is excluse from the random number

	#setup the matrix that will count the amount of every type related to generation

    #pop_count_type = np.array(count_population(population[0]))	

    return population

	########################################da rifare la le strutture dati siccome np.array è omogeneo quindi serve già una lista oppure la lista è fuori e copia i dati
		

def random_int(low_value, high_value, size, dtype=np.byte):# tengo la generazione randomica separate per il testing
    
    return np.random.randint(low_value, high_value, size, dtype)


def avoid_repetition(array_to_test):
    
    a=np.unique(array_to_test, return_counts=True)[1]
          
    b=np.ones_like(a)
          
    return np.array_equal(a,b)

   
def interaction(donator, recipient, onlookers, strategy_array, sources_array, image_matrix):
    
    """

    A pair of individuals, donator-reipient, interact and donator decide whether cooperate

    Parameters:

    -----------------------------
	
    donator: the index that rappresent an individual from the population that could cooperate

    recipient: the index that rappresent an individual from the population that maybe receive

    onlookers: an array 1x10 of indexes of indivuals that observe the interaction

    strategy_array: an array 1x100 with the strategies for each individuals

    sources_array: an array 1x100 with the sources for each individuals

    image_matrix: a matrix 100x100 with the image of each individuals (row) about other individuals (column)
    
    
    
    ###Returns a tupla with the updated population_array and the updated reputation_matrix

    -----------------------------

    
    """
     
    bonus=-1
    
    #print(strategy_array[donator], '>=', image_matrix[donator][recipient], '?')

    if strategy_array[donator]>=image_matrix[donator][recipient]:
		
        bonus=1

        sources_array[recipient]+=1
        
        #print(donator, 'ha cooperato con', recipient )

		
    image_matrix[recipient][donator]+=bonus
    
    for x in range(len(onlookers)):

        image_matrix[onlookers[x]][donator]+=bonus
        
    #print('La reputazione di ', donator, 'è cambiata di', bonus, 'per', recipient, onlookers)

    ###return (sources_array, image_matrix) (vale tenerlo con variabile locale?)

def new_generation(strategy, sources):
    
    
    """
    Creation of the next generation; each indivuals has an offspring
    
    based on its sources. Explain procedure. So no risk of outrange
    
    Parameters:
        
    -----------------------------
        
    strategy: 1x100 array with the strategy of each individual
    
    sources: 1x100 array with the sources of each individual
    
    
    
    Return the array of the strategies of the individual of the new 
    
    generation 

    -----------------------------
    

    
    """
    
    tot_sources=np.sum(sources)
    
    tot_pop=len(strategy) #total number of individuals
        
    inv_tot_sources=np.float16(1/tot_sources) #save time
    
    new_strategy=np.array([], dtype=np.byte)
    
    # array con le proporzioni dei pay-off
    
    proportions = np.float16(sources*inv_tot_sources)
    
    offspring = np.float16(tot_pop*proportions)
    
    #print(offspring)
    
    frac_offspring = np.array(np.modf(offspring)[0], np.float16)
    
    int_offspring = np.array(np.modf(offspring)[1], np.byte)
    
    #print(frac_offspring)
    
    #print(int_offspring)
    
    for individual in range(tot_pop):
        
        appendix=np.full(int_offspring[individual], strategy[individual], np.byte)
               
        new_strategy=np.append(new_strategy, appendix)


    while len(new_strategy) < tot_pop:
        
        # search the highest value among the frac_offspring
        
        appendix= strategy[np.argmax(frac_offspring)]
        
        new_strategy=np.append(new_strategy, appendix)
        
        frac_offspring[np.argmax(frac_offspring)]=0
        
    #print(new_strategy)
        
    np.random.shuffle(new_strategy)
            
    return new_strategy
            
    
def life_cycle(strategy, n_interactions):
    
    """
    Implemantation of a life cycle of a generation with ten encounters
    
    and the arise of the next generation based on sources
    
    Parameters:
    
    -----------------------------
    
    population: a 2x100 array with strategy (0-row) and sources (1-row) of
    
    each individuals
    
    image_matrix: a 100x100 matrix with the image scores of each individuals
    
    (0-row) about the others (1-row)
    
    -----------------------------
    
    Return
    
    """
    #print(strategy,)
    
    population_size=len(strategy)
    
    image_matrix = np.zeros((population_size,population_size), np.byte)
    
    sources = np.zeros_like(strategy, np.byte)
    
    population_size=len(strategy)
    
    x=0
              
    while x<n_interactions: #125 interactions
              
        #DRandO = Donator, Recipient and Onlookers
              
        DRandO=random_int( 0, population_size, 12, np.byte)
              
        if avoid_repetition(DRandO):
                  
            x+=1
            
            interaction(DRandO[0], DRandO[1], DRandO[-10:], strategy, sources, image_matrix)
            
    #print(sources, image_matrix, sep='\n')
    
    old_sources=np.array(sources)
    
    new_population=new_generation(strategy, sources)
    
    return old_sources, new_population #le risorse sono della vecchia generazione

def evolution(N_interactions, N_generation, populations):
    
    """
    Evolution of the various generations
    
    Parameters:
    
    -----------------------------
    
    n_generation: numero di generazione
    
    n_interactions: numero di interazioni in ogni life cycle
    
    population: populations[generazione][strategie/risorse finali][individui]
    
    shape iniziale (1,2,size of population)
    
    -----------------------------
    
    Return the data
    
    """  
    
    
    strategy = populations[0][0]
    
    for generation in range(N_generation):
        
        old_sources, new_strategies = np.array(life_cycle(strategy, N_interactions), np.byte)
        
        populations[generation][1]= old_sources
        
        new_population = np.vstack((new_strategies, np.zeros_like(new_strategies)), dtype=np.byte)
        
        populations=np.append(populations, [new_population], axis=0)
        
    return populations