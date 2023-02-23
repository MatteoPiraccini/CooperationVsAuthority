import numpy as np

import simulation as sm

def testing_init():
	zero=np.zeros((2,100))
	a=sm.init_simulation()[0]
	print(a)
	assert a.shape==zero.shape
	assert a==zero

def testing_count(min,max):
	a=np.array(np.random.randint(min, max, 100, byte))
	sm.count_population(a)
	# finire di creare il test