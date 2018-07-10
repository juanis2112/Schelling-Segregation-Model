# Schelling-Segregation-Model

"In 1969, Thomas C. Schelling developed a simple but striking model of racial segregation. His model studies the dynamics of racially mixed neighborhoods. Like much of Schelling’s work, the model shows how local interactions can lead to surprising aggregate structure. In particular, it shows that relatively mild preference for neighbors of similar race can lead in aggregate to the collapse of mixed neighborhoods, and high levels of segregation."*(https://lectures.quantecon.org/jl/schelling.html)*

#The Project

This project shows an example of tge Shelling's Segregation Model under the following conditions: 
There is a town with 80 inhabitants and 100 houses. The houses are distributed in a grid of 10 by 10. There are 25 inhabitants of green color and 25 inhabitants of red color. We simulate a process of migration within the city. For this we are going to think about a total of 500 changes that are made sequentially.

Each moving process involves the following steps:

**1)** A citizen is chosen at random.
**2)** A vacant place is chosen at random.
**3)** The citizen completes his move if he is happier in the place where he arrives.

The happiness in this simulation is a real number between 0 and 1 and depends on the number of neighbors that have the same color as the citizen who wants to move. If all the neighbors are of the other color, happiness is 0. If there is a perfect balance between colors of the neighbors, happiness is 1. If all the neighbors are of the same color, happiness is 0.5. 
