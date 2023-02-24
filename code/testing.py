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

	np.random.seed(1)

	fake_indexes=np.random.randint(0,100, 12)


	for x in range(len(fake_indexes)):
		for y in range(len(fake_indexes)):

			if x==y:
				continue

			assert fake_indexes[x]!=fake_indexes[y]

	strategy=np.random.randint(-5,7,100)

	sources=np.array(np.random.randint(-2,4,100), float)

	image=np.zeros((100,100), np.byte)

	print(fake_indexes)

	print( sources)
	
	sm.interaction( fake_indexes[0], fake_indexes[1], fake_indexes[-10:], strategy, sources, image)

	#check if reputation change

	assert np.sum(image[image!=0]) == 11

	#interactions work
	






