import numpy as np

from collections import namedtuple

Data = namedtuple( 'Data', 
	[ 'population' , 
	'sources',
	'count_type'])

##### Qui ci vuole una lista con tutti gli array con tutti i dati

def init_simulation(): # che parametri ci vanno?

	"""

    	Create the 0-generation and initialize the structures that contains data

    	Parameters:

    	-----------------------------
	
   	-----------------------------

    	Returns a tupla with a 3D array with data about the 0-generation, the matrix of reputation and an array that store the amount of every types of individual
	
    	"""

	#creation of the 0-generation

	population=np.zeros((1,2,100), np.byte) # 1°-dim: generation, 2°-dim: strategy/sources, 3°-dim: individual
	
	population[0][0] = np.array(random_int(-5, +7, (1,100), np.short)) #7 is excluse from the random number

	#setup of a separate array for the source of every individual, in order to save memory
	
	sources = np.zeros(100, np.half)

	#setup of the matrix of reputation

	image_matrix = np.zeros((100,100), np.byte)

	#setup the matrix that will count the amount of every type related to generation

	pop_count_type = np.array(count_population(population[0]))	

	return Data(population, image_matrix, pop_count_type)

	########################################da rifare la le strutture dati siccome np.array è omogeneo quindi serve già una lista oppure la lista è fuori e copia i dati
		

def random_int(low_value, high_value, size, dtype):# tengo la generazione randomica separate per il testing

	return np.random.randint(low_value, high_value, size, dtype)


def avoid_repetition(array_to_test):
    
    a=np.unique(array_to_test, return_counts=True)[1]
          
    b=np.ones_like(a)
          
    return np.array_equal(a,b)


    
def count_population(array_pop):

	count_row=np.zeros(12,np.byte)

	for x in range(-5,+7):

		count_row[x]=len(array_pop[array_pop==x])

	return count_row ##### [0 1 2 3 4 5 6 -5 -4 -3 -2 -1]


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

	if strategy_array[donator]>=image_matrix[donator][recipient]:
		
		bonus=1

		sources_array[donator]-=0.1

		sources_array[recipient]+=1

		
	image_matrix[recipient][donator]+=bonus


	for x in range(len(onlookers)):

		image_matrix[onlookers[x]][donator]+=bonus

	###return (sources_array, image_matrix) (vale tenerlo con variabile locale?)

def life_cycle(population, image_matrix):
    
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
    print(population[1], image_matrix, sep='\n')
    
    population_size=len(population[1])
    
    x=0
              
    while x<10: # si ripete all'infinito
              
        #DRandO = Donator, Recipient and Onlookers
              
        DRandO=random_int( 0, population_size, 12, np.byte)
              
        if avoid_repetition(DRandO):
                  
            x+=1
            
            interaction(DRandO[0], DRandO[1], DRandO[-10:], population[0], population[1], image_matrix)
            
    print(population[1], image_matrix, sep='\n')