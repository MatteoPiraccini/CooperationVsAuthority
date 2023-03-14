import numpy as np

import simulation as sm

import analysis as an

import plot

#############################################
##TEST for simulation.py


def random_int(low_value, high_value, size, dtype):
    
    """
    This function is for generate fixed random number
    
    Parameters:

    -----------------------------
    low_value: int, inferior value (included)
        
    high_value: int, superior value (excluded)
        
    shape: int, shape of the values generated
        
    dtype: type of the generated values
    -----------------------------
    """

    np.random.seed(11)

    return np.random.randint(low_value, high_value, size, dtype)
	

def test_interaction_coop_sources():
    
    """
    This function is for testing if cooperation mechanism in interaction work well
    
    GIVEN: the strategy array, the donator and recipient indexes and image matrix
    WHEN: when I perform sm.interaction()
    THEN: The cooperation consequences on sources and reputation are applied
    """
    for size_pop in range(12, 200):

        strategy= np.arange(-5, 7, 1, dtype=np.byte)
        
        mod = (size_pop%12)
        
        quot = size_pop // 12
        
        if mod == 0:
            
            population = np.repeat(strategy, quot)
            
            flat_image = np.ravel(np.full(((size_pop),(size_pop)),population))
            
        else:
    
           population = np.hstack((np.repeat(strategy,quot), strategy[:mod]))
           
           flat_image = (np.ravel(np.full(((size_pop),(size_pop)),population)))

        sources=np.zeros(size_pop)
    
        for donator in range(size_pop):
        
            for recipient in range(size_pop):
            
                if donator == recipient:
                
                    continue
    
                for i in range(size_pop):
        
                    image = np.reshape(np.roll(flat_image, i), (size_pop,size_pop))
	
                    sm.interaction( donator, recipient, [], population, sources, image, False, False, [])
                    
                    assert (sources[recipient] == 1 if population[donator] < image[donator][recipient] else sources[recipient] == 0)
                    
                    sources[recipient] = 0
                    
def test_interaction_coop_reputation():
    
    """
    This function is for testing if reputation in interaction work well
    
    GIVEN: the strategy array, the donator, recipient and onlookers indexes and image matrix
    WHEN: when I perform sm.interaction()
    THEN: The cooperation consequences on reputation are applied
    """
    for size_pop in range(12, 200):

        strategy= np.arange(-5, 7, 1, dtype=np.byte)
        
        mod = (size_pop%12)
        
        quot = size_pop // 12
        
        if mod == 0:
            
            population = np.repeat(strategy, quot)
            
            flat_image = np.ravel(np.full(((size_pop),(size_pop)),population))
            
        else:
    
           population = np.hstack((np.repeat(strategy,quot), strategy[:mod]))
           
           flat_image = (np.ravel(np.full(((size_pop),(size_pop)),population)))

        sources=np.zeros(size_pop)
    
        for donator in np.arange((size_pop)):
        
            for recipient in np.arange((size_pop)):
            
                if donator == recipient:
                
                    continue
    
                for i in range(12):
                    
                    if (recipient >= i) & (recipient<i+12):
                        
                        continue
                    
                    if (donator > i) & (donator<i+12):
                        
                        continue
                    
                    if i+11 >= size_pop:
                        
                        continue
                    
                    onlookers = np.arange(i,i+11)
        
                    image = np.reshape(np.roll(flat_image, i), (size_pop,size_pop))
                    
                    image_copy = np.array(image)
	
                    sm.interaction( donator, recipient, onlookers, population, sources, image, False, False, [])

                    onlookers = np.append(onlookers, recipient)
                    
                    for j in range(len(onlookers)):
                        
                        assert (image[onlookers[j]][donator] == image_copy[onlookers[j]][donator]+1) if population[donator] < image[donator][recipient] else image[onlookers[j]][donator] == image_copy[onlookers[j]][donator]-1
                                        
                    image = np.array(image_copy)

def test_new_generation_one_offspring():
    
    """
    Testing new_generation if one individuals have sources and others not. 
    
    The result must be that the next generation is  composed only by its 
    
    offspring
    
    GIVEN: I have two arrays: strategy and sources
    WHEN: I perform the new_generation() function
    THEN: the new generation show the right offspring
    """

    fake_strategy=np.full(10, 0, np.byte)
    
    fake_sources=np.zeros(10, np.byte)
    
    fake_strategy[3] = 2
    
    fake_sources[3] = 1

    new_generation = sm.new_generation(fake_strategy, fake_sources, True)
    
    assert np.all(new_generation == np.full_like(fake_strategy, 2))

def test_new_generation_many_offspring():
    
    """
    Testing if new_generation give the correct results with a given array of 
    
    strategies and a given array with sources
    
    GIVEN: I have two arrays: strategy and sources
    WHEN: I perform the new_generation() function
    THEN: the new generation show the right offspring
    """

    fake_strategy= np.array( [-1, 3, -2, 0, 1, 1, 1, -2, 6, 3])
    
    fake_sources= np.array( [1, 0, 2, 0, 2, 5, 1, 3, 1, 0])
    
    new_generation = sm.new_generation(fake_strategy, fake_sources, True)
    
    assert np.all(new_generation == [-2, 1, 1, 1, 1, -2, -2, -1, 1, 6])

def test_new_generation_same():
    
    """
    Testing if new_generation return the same array if all individuals have the
    
    same sources
    
    GIVEN: I have two arrays: strategy and sources
    WHEN: I perform the new_generation() function
    THEN: the new generation show the right offspring
    """

    fake_strategy= np.array( [-1, 3, -2, 0, 1, 1, 1, -2, 6, 3])
    
    fake_sources= np.full_like(fake_strategy, 0)
    
    new_generation = sm.new_generation(fake_strategy, fake_sources, True)
    
    assert np.all(new_generation == fake_strategy)
    
    
    
#########################################################
## TEST for analysis.py
    
def test_an_strategy_freq():
    
    """
    This function is for testing if the right frequencies are well computed
    
    GIVEN: I have an array (n,2,m) with the strategies in [:,0,:]
    WHEN: The simulation is concluded
    THEN: The frequencies of the values of the given array
    """
    for j in range(1,10000):
        
        for i in range(1,13):
        
            N_generations = j
    
            size = i
    
            start = -5
    
            fake_data= np.full((N_generations,2, size), np.arange(start, start+size, 1))
    
            freq = an.frequency_strategies(fake_data)
    
            freq = freq[freq !=0]
    
            assert np.allclose( freq, np.full_like(freq, 1/size), atol=1e-03)
    
#########################################################
## TEST for plot.py   

    
def test_plot_reorganize():
    
    """
    This function is for test that plot.reorganize() exchanges the right columns
    
    GIVEN: I have an array 2D
    WHEN: I am about to plot data
    THEN: The array with data in the right order
    
    """
    
    fake_data=np.array([[0,1,2,3,4,5,6,-5,-4,-3,-2,-1] for i in range(10)])
    
    comparison = np.array([[-5,-4,-3,-2,-1,0,1,2,3,4,5,6] for i in range(10)])
    
    re_data = plot.reorganize_data(fake_data)
    
    assert np.all(re_data == comparison)

    