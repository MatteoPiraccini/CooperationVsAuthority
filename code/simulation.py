import numpy as np

def init_simulation(): # che parametri ci vanno?
	"""
    	Create the 0-generation and initialize the structures that contains data
    	Parameters:
    	-----------------------------
	
   	-----------------------------
    	Returns
	
    	"""
	#creation of the 0-generation
	population=np.zeros((2,100))
	population[0]=np.array(generate_random_int(-5, +7, (1,100), np.short))
	#setup of the matrix of reputation
	reputation=np.zeros((100,100), np.byte)
	#setup the matrix that will count the amount of every type related to generation
	population_type=np.zeros((12, 1))
	return (population,reputation)
		

def generate_random_int(low_value, high_value, size, dtype):# tengo la generazione randomica separate per il testing
	return np.random.randint(low_value, high_value, size, dtype)

def count_population(array_pop):
	for x in range(-5,+7):
		count_row[x]=len(array_pop[array_pop==x])

	print(count_row)

	
		
	