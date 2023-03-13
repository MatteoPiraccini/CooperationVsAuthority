## plot.py

In this library the data elaborated in `analysis.py` are plotted and visualized.


## `reorganize_data(data)`

Split and rearrange the array of frenquencies

#### Parameters:
	
-data: array (N of simulations, 12), frequencies

Returns an array (N of simulations, 12) rearrange

#### Example

We have a dataframe `data` like this

0|1|2|3|4|5|6|7|8|9|10|11
---|---|---|---|---|---|---|---|---|---|---|---
5|6|7|8|9|10|11|12|13|14|15|16

if we execute this

```python

 import plot

plot.reorganize_data(data)

```
We obtain this

7|8|9|10|11|0|1|2|3|4|5|6
---|---|---|---|---|---|---|---|---|---|---|---
12|13|14|15|16|5|6|7|8|9|10|11




## `draw_data(data, par)`

Generate a series of stem plot with the frequencies of strategies. Max 15 plot

#### Parameters:
	
-data: array (N of simulations, 12), frequencies