import numpy as np

from collections import namedtuple

Data = namedtuple( 'Data', 
	[ 'population' , 
	'sources',
	'count_type'])

def init_simulation(): # che parametri ci vanno?

	"""

    	Create the 0-generation and initialize the structures that contains data

    	Parameters:

    	-----------------------------
	
   	-----------------------------

    	Returns
	
    	"""

	#creation of the 0-generation

	population=np.zeros(100, np.byte)
	
	population[0] = np.array(generate_random_int(-5, +7, (1,100), np.short)) #7 is excluse from the random number

	#setup of a separate array for the source of every individual, in order to save memory
	
	sources = np.zeros(100, np.half)

	#setup of the matrix of reputation

	reputation = np.zeros((100,100), np.byte)

	#setup the matrix that will count the amount of every type related to generation

	pop_count_type = np.array(count_population(population[0]))

	O_data=Data(population,reputation, pop_count_type)

	return O_data


############################################# controllare se tupla permette di memorizzare diversi tipi di array
		

def generate_random_int(low_value, high_value, size, dtype):# tengo la generazione randomica separate per il testing

	return np.random.randint(low_value, high_value, size, dtype)

def count_population(array_pop):

	count_row=np.zeros(12,np.byte)

	for x in range(-5,+7):

		count_row[x]=len(array_pop[array_pop==x])

	return count_row

	
		
	