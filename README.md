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