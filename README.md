# CooperationVsAuthority

In this project we try to find out how cooperation work in the presence of authority. We have take and manipulate the model form this article: [Evolution of indirect reciprocity by image scoring](https://www.nature.com/articles/31225) by Martin A. Nowak & Karl Sigmund. In this article they set up a simulation to control how the so-call inderect reciprocity work in order to cooperation uprise. This project implement a different version of the model.

### How the original model work

Each individuals are characterized by the strategy k, the sources p and the image score s.

The strategy is a integer value between -5 and +6, it reprenst the predisposition to cooperate. The sources are an integer that represent how many time someone cooperated with the individual. The image score is an integer that represent the own reputation that the others have about us.

At the beginnig of a generation there is some fixed aomunt of individuals, all with zero sources and zero image scores and random strategy. Some couples of individuals are randomly picked up. One take the role of the donator, the other of the recipient. If the strategy k of the donator is more or equal than the donator's image score about the recipient (k>=s_donator_recipient), then the donator cooperate, so the sources of the recipient increase by one. If donator decide to not cooperate, nothing change. In the meantime, there are ten onlookers, picked randomly, those are observing the interaction. If the donator has cooperate, the onlookers' and recipient's image score about him increase by one. If the donator has not cooperate, image score about him decrease by one.
After some interactions a new generation arise. Each individuals of the old generation has an offspring proportional to own sources. The offspring has the same strategy k of the old individual. The total size of population doesn't change.

So it repeat for some amount of population

### Differences respect the orginal model

In this project we had an unexplored topic about cooperation: authority.
For each simulation, one could decide if the authority will be punishing, rewarding or both, and how much pervasive wuold be (how much individuals checks).
During the interations some individuals will be controlled. Nothing happen until one of this is the donator or the recipient. In that case, if the the authority is punishing, it will punish the donator that not cooperate by decrease by one his sources and the image score of all the onthers individuals about him. Viceversa, if donator cooperate and the authority is rewarding, it will be rewarded by increase by one his sources and the image score of all the onthers individuals about him.

## How to use

First yuo have to download the repository.

Then check if you satisfy all requirements in `requirements.txt`

After that you have to give parameters for your programe.

Move to the subdirectory CoopAut. Here there is the `Parameters.csv`. In this csv file every writed line is a simulation, except for the first one. The first one is ignored by the program, it contains how are structured the data and what values are valid.
For each simulation that you want to perform you must write a line. The template for one simulation is

```
size_population,N_interactions,N_generations,punishment,reward,controls
```

For more simulation in the same run

```
size_population1,N_interactions1,N_generations1,punishment1,reward1,controls1
size_population2,N_interactions2,N_generations2,punishment2,reward2,controls2
size_population3,N_interactions3,N_generations3,punishment3,reward3,controls3
...
```

#### Parameters

-size_population: int, range: 12-255, how much individuals in each generation
-N_interactions: int, range: 1-255, how much interactions in each genearation
-N_generations: int, range: 1-255, how much generations in the simulation
-punishment: True/False, presence/absence of a punishing authority
-reward: True/False, presence/absence of a punishing authority
-controls: int, range: 1-size_population, how much individual are checked by the authority