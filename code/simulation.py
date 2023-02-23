import numpy as np

def init_simulation():# che parametri ci vanno?
	"""
    	Create the 0-generation and initialize the structures that contains data
    	Parameters:
    	-----------------------------
	
   	-----------------------------
    	Returns
    	"""
	#bisogna creare la popolazione e tutti gli oggetti per contenere le informazioni
	list=[]
	population=np.zeros((2,100))
	for x in range(100):
		list.append(generate_random_int(-5, +6))
	population[0]=lista
		

def generate_random_int(low_value, high_value):# tengo la generazione randomica separate per il testing
	np.random.randint(low_value, high_value, None, dtype=np.short)
		
	