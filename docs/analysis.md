## analysis.py

This library perform the data analysis of the data generated by `simulation.py` via `__main__.py`. It calculate the frequencies of the strategies in each simulation along the generations and the mean strategy for each simulation

## `frequency_strategies(data_simulation)`

Computation of the frequencies of strategies for a simulation

#### Parameters:
	
-data_simulation: array (N of generations, 2, size of population), data from the simulation

Returns an array (12,), frequencies of the strategies


## `analize_simulations(all_data)`

Create the dataframe of the frequencies of strategies for all the simulations and save the mean strategy into a file csv located in the same directory

#### Parameters:
	
-all_data: array (N of simulations, N of generations, 2, size of population) all the data generated by simulations

Returns:
        
 + stat_strategies: array (N of simulations, 12), frequencies of strategies in all simulation
    
 + mean_strategy: array (N of simulations), mean strategiy of each simulations

### Note

The organization of data for strategies are like this

index|0|1|2|3|4|5|6|7|8|9|10|11
---|---|---|---|---|---|---|---|---|---|---|---|---
strategy|0|1|2|3|4|5|6|-5|-4|-3|-2|-1
