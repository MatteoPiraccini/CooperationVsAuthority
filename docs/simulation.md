## simulation.py

This library performes the simulations of the evolution of the population, given the parameters from '__main__.py'. It compute all the process inside and between the generations. It is used to return an array with all needed data from each generation.

## `init_simulation(population_size)`

Create the 0-generation with casual strategies and zero sources.

### Parameters:

-population_size: int, indicate numerosity of the population
	
Return an array with dimension (1,2,size_population), there will be store data along the simulation


## `random_int(low_value, high_value, size, dtype=np.byte)`

Generate an array of random int

#### Parameters:
        
-low_value: int, inferior value (included)
        
-high_value: int, superior value (excluded)
        
-shape: int, shape of the values generated
        
-dtype: type of the generated values, by default is np.byte

Return an array (size) with casual int values from [low_value, high_value)


## `interaction(donator, recipient, onlookers, strategy_array, sources_array, image_matrix, punishment, reward, controls)`

Simulation of a pair of individuals, donator-reipient, interact and donator decide whether cooperate

#### Parameters:
	
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

#### Example
(size of population is 30)
```python

import simulation as sm

donator = 3
recipient = 7
onlookers = [ 0, 1, 2, 5, 6, 8, 9, 10, 12, 20]
strategy_array = [ 0, -1, -2, 2 , ...]
sources_array =[ 0, ..., 0]
image_matrix = [ [ 0, ..., 0], ..., [ 0, ..., 0]]
punishement = False
reward = False
controls = [ 2, 3, 8]

sm.interaction( donator, recipient, onlookers, strategy_array, sources_array, image_matrix, punishment, reward, controls)
```
The strategy of the donator (k=2) is more than the donator's reputation s about the recipient (s=0) so we obtain that sources_array

0|1|...|7|...
---|---|---|---|---
0|0|...|1|...

and this image_matrix (row are the individual, column the image score about that individual)

.|0|1|...|3|...
---|---|---|---|---|---
0|0|0|...|1|---
1|0|...|...|1|---
...|...|...|...|...|---
28|0|...|...|0|---
29|0|0|...|0|---

In the case that
```python
reward = True
```
the donator will be controlled and rewarded.
So the source_array would be

0|1|...|3|...|7|...
---|---|---|---|---|---|---
0|0|...|1|...|1|...

and the image_matrix

.|0|1|...|3|...
---|---|---|---|---|---
0|0|0|...|1|---
1|0|...|...|1|---
...|...|...|1|...|---
28|0|...|...|1|---
29|0|0|...|1|---



## `new_generation(strategy, sources)`

Creation of the next generation; each indivuals has an offspring based on its sources.
    
#### Parameters:
        
-strategy: array (1, size of population), strategy of each individual
    
-sources: array (1, size of population), sources of each individual

    
Return an array (1, size of population) of the strategies of the individual of the new generation


## `life_cycle(population, N_interactions, punishment, reward, N_controls)`

Implemantation of a life cycle of a generation with interactions and the arise of the next generation based on sources
    
#### Parameters:
   
-population: array (2, size of population), strategy (0-row) and sources (1-row) of each individuals
    
-N_interactions: int, how many interactions are iterated
    
-punishment: bool, to indicate if punishment is on
        
-reward: bool, to indicate if punishment is on
    
-N_controls: int, number of individuals to be controled for each interaction

    
Return two arrays (size of population), first with the sources of the old generation, the other with strategies of the new one


## `evolution(N_interactions, N_generation, populations, punishment, reward, controls)`

Evolution of the various generations.
    
#### Parameters:
    
-N_interactions: int, how many interactions are iterated
    
-N_generation: int, how many generations are iterated
    
-populations: array (2, size of population), strategy (0-row) and sources (1-row) of the 0-generation
   
-punishment: bool, to indicate if punishment is on
       
-reward: bool, to indicate if punishment is on
   
-N_controls: int, number of individuals to be controled for each interaction

    
Return an array (N_generation, 2, size of population) with strategies and sources for each generation

