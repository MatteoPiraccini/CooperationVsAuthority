## simulation.py

This library performes the simulations of the evolution of the population, given the parameters from '__main__.py'. It compute all the process inside and between the generations. It is used to return an array with all needed data from each generation.

## 'init_simulation(population_size)'

Create the 0-generation with casual strategies and zero sources.

### Parameters:

-population_size: int, indicate numerosity of the population
	
Return an array with dimension (1,2,size_population), there will be store data along the simulation

## 'random_int(low_value, high_value, size, dtype=np.byte)'

Generate an array of random int

### Parameters:
        
-low_value: int, inferior value (included)
        
-high_value: int, superior value (excluded)
        
-shape: int, shape of the values generated
        
-dtype: type of the generated values, by default is np.byte

Return an array (size) with casual int values from [low_value, high_value)

## 'interaction(donator, recipient, onlookers, 
                
                strategy_array, sources_array, image_matrix, 
                
                punishment, reward, controls):'

Simulation of a pair of individuals, donator-reipient, interact and donator decide whether cooperate

### Parameters:
	
-donator: int, index of an individual from the population that could cooperate

-recipient: int, index of an individual from the population that maybe receive

-onlookers: array (1,10), indexes of indivuals that observe the interaction

-strategy_array: array (1, size of population), the strategies for each individuals

-sources_array: array (1, size of population), the sources for each individuals

-image_matrix: array (size of poplutation)**2, matrix of image scores
    
-punishment: bool, to indicate if punishment is on
    
-reward: bool, to indicate if punishment is on
    
-controls: array 1-D, indexes of the people controlled

    
Return nothing.

