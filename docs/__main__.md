## __main__.py

This library is to start and to manage all the execution of the code.


## `main()`

Call this functions if you want to start the program

First it extract value from the file `Parameters.csv` in the same directory. Then for each simulation it recall 
`simulation.py` and store the data in 'data_list'. After that it pass perform the analysis of data by `analysis.py`. Finally it plot the strategy for each simulation.


## `check_parameters(parameters)`

Control if the values passed to the program are valid
    
#### Parameters:
	
-parameters: array (N of simulations, 12), all the parameters from the csv file