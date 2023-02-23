import numpy as np

import simulation as sm

def testing_init():
	# just a visual check
	zero=np.zeros((2,100))
	a=sm.init_simulation()[0]
	print(a)
	assert a.shape==zero.shape
	assert a==zero

def testing_count(min,max):
	# check if the counter work
	a=np.array(np.random.randint(min, max, 100, np.byte))
	count_row=sm.count_population(a)
	print(count_row)
	print(a)
	if(min==-5 & max==7):
		assert np.sum(count_row)==100