import numpy as np

import simulation as sm

import analysis as an

# ricontrolare tutto, togliere tutti i print e i return, inserire if-else al posto di assertion e togliere la roba su dimensionalità
# riguardare pagina esame

def testing_init():
	# just a visual check
    
	arrays_tupla=sm.init_simulation()
    
	print(arrays_tupla)
    
	assert np.shape(arrays_tupla)==(1,2,100)
    
##### controllare la dimensionalità

def random_int(low_value, high_value, size, dtype):# generazione randomica per il testing

    np.random.seed(5)

    return np.random.randint(low_value, high_value, size, dtype)

def testing_count(min,max):
	# check if the counter work
	
	assert isinstance(min,int)

	assert isinstance(max,int)

	assert max>min

	a=np.array(np.random.randint(min, max, 100, np.byte))
		
	count_row=sm.count_population(a)

	print(count_row)
		
	print(a)
	

def testing_interaction():

    size_pop=20

    fake_indexes=np.random.randint(0,size_pop, 12, np.byte)
    
    while not sm.avoid_repetition(fake_indexes):
        
        fake_indexes=np.random.randint(0,size_pop, 12, np.byte)

    strategy=np.array(random_int(-5,7,size_pop, dtype=np.byte))

    sources=np.array(random_int(0,4,size_pop, np.byte))

    image=np.array(random_int(-4,7, (size_pop,size_pop), np.byte))

    print(fake_indexes)

    print(sources,)
    
    print(image[:, fake_indexes[0]])
	
    sm.interaction( fake_indexes[0], fake_indexes[1], fake_indexes[-10:], strategy, sources, image)

    
    print(sources, 
          
          strategy[fake_indexes[0]],
          
          ' >=', 
          
          image[fake_indexes[0]][fake_indexes[1]], 
          
          image[:, fake_indexes[0]], 
          
          sep='\n')
    
    # work (apparently)


def testing_no_repeat():

      x=0
      
      while x<10:
      
        #DRandO = Donator, Recipient and Onlookers
      
        DRandO=sm.random_int( 0, 100, 12, np.byte)
      
        a=np.unique(DRandO, return_counts=True)[1]
      
        b=np.ones_like(a)
      
        if np.array_equal(a,b):
          
           x+=1
           
           print(DRandO)

def testing_new_generation():
    
    fake_strategy=random_int(-5, 7, 10, np.byte)
    
    fake_sources=random_int(0, 5, 10, np.byte)
    
    print(fake_strategy)
    
    print(fake_sources)

    new_generation = sm.new_generation(fake_strategy, fake_sources)
    
    assert len(fake_strategy) == len(new_generation)
    
    print(new_generation)     
           
def testing_life_cycle():
    
    # no valore negativi all'image score
    
    size=100
    
    fake_population=[sm.random_int(-5, 7, size, np.byte), np.array(sm.random_int(0, 7, size, np.byte), np.byte)]
    
    fake_image=np.zeros((size,size), np.byte)
    
    print(sm.life_cycle(fake_population, fake_image, n_interactions= 125))
    
def not_a_mess_with_append():
    
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
    
def testing_an_strategy():
    
    fake_n_gen=3
    
    fake_size_pop=10
    
    fake_data= random_int(-5, 7, (fake_n_gen, 2, fake_size_pop), np.byte)
    
    print(fake_data)
    
    print(an.frequency_strategies(fake_data))