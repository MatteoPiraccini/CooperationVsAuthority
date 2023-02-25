import numpy as np

import simulation as sm

def testing_init():
	# just a visual check
	zero=np.zeros((2,100))
	arrays_tupla=sm.init_simulation()
	print(arrays_tupla)
	assert arrays_tupla[0].shape==(1,2,100)
	assert arrays_tupla[1].shape==(100,100)
	assert arrays_tupla[2].shape==(12,)
##### controllare la dimensionalità

def random_int(low_value, high_value, size, dtype):# generazione randomica per il testing

	np.random.seed(1)

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
	

def testing_interaction(): ###siamo qui a indagare perché la reputazione non diminuisce


    fake_indexes=random_int(0,100, 12, np.byte)
    
    while not sm.avoid_repetition(fake_indexes):
        
        fake_indexes=random_int(0,100, 12, np.byte)       

    strategy=np.random.randint(-5,7,100)

    sources=np.array(np.random.randint(-2,4,100), float)

    image=np.zeros((100,100), np.byte)

    print(fake_indexes)

    print(sources, strategy, image, sep='\n')
	
    sm.interaction( fake_indexes[0], fake_indexes[1], fake_indexes[-10:], strategy, sources, image)

	#check if reputation change

    assert np.sum(image[image!=0]) == 11
    
    print(sources, strategy, image, sep='\n')


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
           
           
def testing_life_cycle():
    
    # no valore negativi all'image score
    
    size=13
    
    fake_population=[sm.random_int(-5, 7, size, np.byte), np.array(sm.random_int(-2, 10, size, np.byte), np.float16)]
    
    fake_image=np.zeros((size,size), np.byte)
    
    sm.life_cycle(fake_population, fake_image)
          
